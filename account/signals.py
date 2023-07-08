from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from account.models import Account
from account.utils import generate_password, send_activation_email


@receiver(post_save, sender=Account)
def creat_employee(sender, instance, created, **kwargs):
    if created:
        password = generate_password()
        s1 = User.objects.create_user(username=instance.username,
                                      first_name=instance.first_name,
                                      last_name=instance.last_name,
                                      email=instance.email,
                                      password=password,
                                      is_active=True)
        g = Group.objects.get(name=instance.role)
        s1.groups.add(g)
        send_activation_email(instance, password)
        Account.objects.filter(username=instance.username).update(user=s1)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if not created:
        Account.objects.filter(user=instance).update(username=instance.username,
                                                     first_name=instance.first_name,
                                                     last_name=instance.last_name,
                                                     email=instance.email)
