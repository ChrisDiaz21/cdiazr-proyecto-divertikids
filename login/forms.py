from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date
import re

def validar_edad(fecha_nacimiento):#valida que se ingrese una fecha de nacimiento valida
    today = date.today()
    edad = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    
    if edad < 18:
        raise ValidationError("Ingrese una fecha correspondiente.")
    elif edad >110:
        raise ValidationError("Ingrese una fecha correspondiente.")
    
def validar_longitud_minima(value):#valida si el nombre u apellido tiene los caractares minimos que son 4
    if len(value) < 4:
        raise ValidationError('Este campo debe tener al menos 4 caracteres.')
    
def validar_telefono(value):#valida que solo ingrese valores numericos y que el largo sea 9
    if not re.match(r'^\d{9}$', value):
        raise ValidationError("El número de teléfono debe contener solo 9 dígitos numéricos.")





class forms_login(forms.Form):
    # esto es para cuando inicie sesion lo pueda hacer por el correo y no el nombre de ususario que esta por defecto
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")



class CustomUserCreationForm (UserCreationForm):#todo esto es para el registro de usuarios
    telefono = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
        label="Teléfono",
        validators=[validar_telefono]
    )


    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label="Fecha de Nacimiento",
        validators=[validar_edad]
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','telefono','fecha_nacimiento','password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['telefono', 'fecha_nacimiento']:
                field.widget.attrs.update({'class': 'form-control'})
                field.widget.attrs['placeholder'] = field.label

        self.fields['first_name'].required = True#digo que los elementos sean obligatorios 
        self.fields['last_name'].required = True
        self.fields['email'].required = True

        self.fields['first_name'].validators.append(validar_longitud_minima)
        self.fields['last_name'].validators.append(validar_longitud_minima)


    def clean_email(self):# esto valida que si el correo existe entonces no se podra registrar
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electrónico ya está registrado. Por favor, utiliza otro.")
        return email
    


