from django.db import models
from django.views.decorators.http import condition


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=120)

    class Meta:
        abstract = True

class Seller(User):
   website = models.URLField(default='')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    cost = models.DecimalField()
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


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ManyToManyField(Product, on_delete=models.CASCADE)

