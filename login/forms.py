from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class forms_login(forms.Form):
    # esto es para cuando inicie sesion lo pueda hacer por el correo y no el nombre de ususario que esta por defecto
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")


class CustomUserCreationForm (UserCreationForm):
    # estos campos se agregaran a la tabla user de django ya que no lo posee por defecto
    # rut = forms.CharField(max_length=12, required=True)
    # telefono = forms.CharField(max_length=9, required=True)
    # fecha_nacimiento = forms.DateField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
# ,'rut','telefono','fecha_nacimiento'


