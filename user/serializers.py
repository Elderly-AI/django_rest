from rest_framework import serializers
from user.models import CustomUser


class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    def save(self, *args, **kwargs):
        email = self.validated_data['email']
        password = self.validated_data['password']
        user = CustomUser.objects.create_user(email, password)
        return user
