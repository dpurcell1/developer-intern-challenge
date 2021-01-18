from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Image(models.Model):
    upload = models.ImageField(null=True, blank='True')
    author = models.ForeignKey(MyUser, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.upload