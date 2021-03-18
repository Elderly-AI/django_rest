import hashlib
from django.contrib.auth.models import BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        username = self.__get_username(email, password)
        user = self.model(username=username, email=email, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_active = True
        user.is_superuser = False
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password, **kwargs):
        username = self.__get_username(email, password)
        user = self.model(username=username, email=email, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

    def get_by_natural_key(self, username_):
        return self.get(username=username_)

    def __get_username(self, email, password):
        string = (str(email) + str(password)).encode('utf-8')
        return hashlib.sha512(string).hexdigest()
