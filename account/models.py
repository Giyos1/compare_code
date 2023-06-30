from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = models.TextField()
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    activ = models.BooleanField(default=False)

    def __str__(self):
        return self.username
