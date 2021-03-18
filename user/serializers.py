from rest_framework import serializers
from user.models import CustomUser


class CustomUserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'user_type']

    def validate(self, data):
        print(data)
        self._validate_copy(data['email'], data['password'])
        self._validate_child(data['email'], data['user_type'])
        self._validate_parent(data['email'], data['user_type'])
        return data

    def validate_user_type(self, user_type):
        if user_type < 1 or user_type > 3:
            raise serializers.ValidationError({'user_type': 'User type is invalid'})
        return user_type

    def _validate_copy(self, email, password):
        if CustomUser.objects.filter(email=email, password=password).count() != 0:
            raise serializers.ValidationError({'email': 'User already exists'})

    def _validate_child(self, email, user_type):
        if user_type == 1 and CustomUser.objects.filter(email=email, user_type=2).count() == 0:
            raise serializers.ValidationError({'email': 'Parent with this email does not exist'})

    def _validate_parent(self, email, user_type):
        if (user_type == 2 or user_type == 3) and \
                CustomUser.objects.filter(email=email).count() != 0:
            raise serializers.ValidationError({'email': 'This email is already in use'})

    def save(self, *args, **kwargs):
        user = CustomUser.objects.create_user(self.validated_data['email'],
                                              self.validated_data['password'])
        user.user_type = self.validated_data['user_type']
        user.save()
        return user




