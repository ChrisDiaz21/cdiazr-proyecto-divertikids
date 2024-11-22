from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class forms_login(forms.Form):
    
    # esto es para cuando inicie sesion lo pueda hacer por el correo y no el nombre de ususario que esta por defecto
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")


class CustomUserCreationForm (UserCreationForm):
    telefono = forms.CharField(max_length=15, required=True)
    fecha_nacimiento = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label="Fecha de Nacimiento"
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','telefono','fecha_nacimiento','password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}), label="Nombre de usuario")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre(s)'}), label="Nombre(s)")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido(s)'}), label="Apellido(s)")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}), label="Correo electrónico")
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}), label="Teléfono")
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), label="Fecha de Nacimiento")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}), label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}), label="Confirmar contraseña")


