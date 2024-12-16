# # from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Notification
# from django.contrib.auth import get_user_model
# User = get_user_model()


# @receiver(post_save, sender=get_user_model)
# def user_registered_handler(sender, instance, created, **kwargs):
#     if created:
#         Notification.objects.create(message=f"Nuevo usuario registrado: {instance.first_name} {instance.last_name}")

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification

User = get_user_model()

@receiver(post_save, sender=User)
def user_registered_handler(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(message=f"Nuevo usuario registrado: {instance.first_name} {instance.last_name}")



