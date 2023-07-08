from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    choices_role = (
        ('teacher', 'teacher'),
        ('student', 'student'),
    )
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, choices=choices_role)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    activ = models.BooleanField(default=True)

    def __str__(self):
        return self.username
