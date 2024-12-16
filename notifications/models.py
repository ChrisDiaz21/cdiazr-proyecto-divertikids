from django.db import models

class Notification(models.Model):
    message = models.TextField(verbose_name="Mensaje")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")

    def __str__(self):
        return f"{self.message} - {self.created_at}"
            
    class Meta: 
        verbose_name = "Notificación" 
        verbose_name_plural = "Notificaciones"
