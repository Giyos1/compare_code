from django.db import models
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from account.models import Account


class GroupCourse(models.Model):
    group_name = models.CharField(max_length=100)
    member = models.ManyToManyField(Account, related_name='member')
    subject = models.CharField(max_length=100)

    class Meta:
        unique_together = ('group_name', 'subject',)

    @property
    def tasks(self):
        return Task.objects.filter(group=self)

    def __str__(self):
        return self.group_name


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    group = models.ForeignKey(GroupCourse, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Result(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.IntegerField(default=0)
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
