from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random
import string


def send_activation_email(instance, password):
    subject = 'Activation Link'

    html_message = render_to_string('activation_email.html', {
        'username': instance.username,
        'password': password,
    })

    plain_message = strip_tags(html_message)

    from_email = 'giyosoripov4@gmail.com'
    recipient_list = [instance.email]

    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message, fail_silently=False)


def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(8))

    return password
