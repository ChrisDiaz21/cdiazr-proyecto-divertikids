from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'created_at')
    ordering = ('-created_at',)

def get_list_display(self, request): 
    return ('Mensaje', 'Fecha') 
    
def get_ordering(self, request): 
    return ('-Fecha',)
