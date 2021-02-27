from django.db import models
from user.models import CustomUser


class ChildProfile(models.Model):
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, default="")
    age = models.PositiveSmallIntegerField(default=0)
    sex = models.BooleanField(default=False)

    def __str__(self):
        return str(self.main_user)


class ParentProfile(models.Model):
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, default="")
    last_name = models.CharField(max_length=32, default="")
    patronymic = models.CharField(max_length=32, default="")
    phone_number = models.CharField(max_length=32, default="")
    sex = models.BooleanField(default=False)

    def __str__(self):
        return str(self.main_user)


class TeacherProfile(models.Model):
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, default="")
    last_name = models.CharField(max_length=32, default="")
    patronymic = models.CharField(max_length=32, default="")
    phone_number = models.CharField(max_length=32, default="")
    sex = models.BooleanField(default=False)
    about = models.CharField(max_length=1024, default="")
    specialization = models.CharField(max_length=32, default="")

    def __str__(self):
        return str(self.main_user)
