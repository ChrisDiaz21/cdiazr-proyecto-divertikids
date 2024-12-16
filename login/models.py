from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, rut, email, first_name, last_name, password=None, **extra_fields):
        if not rut:
            raise ValueError('El usuario debe tener un RUT')
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        email = self.normalize_email(email)
        user = self.model(rut=rut, email=email, first_name=first_name, last_name=last_name, username=rut, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('fecha_nacimiento', None)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(rut, email, first_name, last_name, password, **extra_fields)

class MyUser(AbstractUser):
    rut = models.CharField(max_length=12, unique=True, primary_key=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=15)

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = MyUserManager()

    # def __str__(self):
    #     return self.rut


    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.get_full_name()