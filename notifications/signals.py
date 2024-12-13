from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification

@receiver(post_save, sender=User)
def user_registered_handler(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(message=f"Nuevo usuario registrado: {instance.username} {instance.last_name}")
