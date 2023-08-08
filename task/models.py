from django.db import models
from django.contrib.auth.models import User


class GroupCourse(models.Model):
    group_name = models.CharField(max_length=100)
    member = models.ManyToManyField(User, related_name='member')
    subject = models.CharField(max_length=100)


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    group = models.ForeignKey(GroupCourse, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
