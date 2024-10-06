from django.db import models
from django.views.decorators.http import condition


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=120)

    class Meta:
        abstract = True


class Customer(User):
    name = models.CharField(max_length=50, default='')
    surname = models.CharField(max_length=30, default='')


class Seller(User):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300, default='')
    website = models.URLField(default='')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    sellers = models.ManyToManyField(Seller, related_name='product', on_delete=models.CASCADE)
    available = models.BooleanField()

    class Meta:
        abstract = True
        constraints = [
            models.CheckConstraint(
                condition=models.Q(cost__gte=0) & models.Q(expensive_check=condition),
                name="check_product_cost",
            ),
        ]


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=10, decimal_places=2)


class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, on_delete=models.CASCADE, through=Order)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=10, decimal_places=2)


class Payment(models.Model):
    class PaymentMethod(models.TextChoices):
        ONLINE = "online"
        CREDIT_CARD = "credit_card"
        CASH = "cash"

    class PaymentStatus(models.IntegerChoices, models.Choices):
        FAILED = 0, "Failed"
        SUCCESS = 1, "Success"

    status = models.CharField(choices=PaymentStatus)
    order = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_method = models.CharField(choices=PaymentMethod)
    date = models.DateTimeField(auto_now_add=True)
