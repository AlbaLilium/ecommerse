from rest_framework import serializers

class LoginRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotImplemented
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']


class SignupRequestSerializer(serializers.ModelSerializer):
    pass
