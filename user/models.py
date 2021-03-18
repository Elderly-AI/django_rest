from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from user.managers import CustomAccountManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField()
    username = models.CharField(max_length=128, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    user_type = models.IntegerField(choices=[(1, 'Child'), (2, 'Parent'), (3, 'Teacher')], default=0)

    REQUIRED_FIELDS = ['email', 'password']
    USERNAME_FIELD = 'username'

    objects = CustomAccountManager()

    def get_short_name(self):
        return self.email

    def natural_key(self):
        return self.username

    def __str__(self):
        return self.email
