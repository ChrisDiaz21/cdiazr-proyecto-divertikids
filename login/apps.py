# from django.apps import AppConfig
# from .signals import *

# class LoginConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'login'

#     def ready(self):
#         import logout_previous_sessions

from django.apps import AppConfig

class LoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login'

    def ready(self):
        from . import signals
