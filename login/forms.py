from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser  # Importa tu modelo de usuario personalizado
from django.core.exceptions import ValidationError
from datetime import date
import re


############ validaciones ############
def validar_edad(fecha_nacimiento):
    today = date.today()
    edad = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    
    if edad < 18:
        raise ValidationError("Debe ser mayor de 18 años.")
    elif edad > 110:
        raise ValidationError("Ingrese una fecha válida.")
    
def validar_longitud_minima(value):
    if len(value) < 4:
        raise ValidationError('Este campo debe tener al menos 4 caracteres.')
    if not value.isalpha():
        raise ValidationError('Este campo solo puede contener letras.')
    
def validar_telefono(value):
    if not re.match(r'^\d{9}$', value):
        raise ValidationError("El número de teléfono debe contener solo 9 dígitos numéricos.")
    
def validar_rut(value):
    rut_pattern = re.compile(r'^\d{1,8}-[\dkK]$')
    if not rut_pattern.match(value):
        raise ValidationError("El RUT ingresado es incorrecto")
    

################## los datos que se piden para iniciar sesion ########################
class forms_login(forms.Form):
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")



################### los datos que se guardaran del ususario ###########################
class CustomUserCreationForm(UserCreationForm):
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
    rut = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT'}),
        label="RUT",
        validators=[validar_rut]
    )

    class Meta:
        model = MyUser
        fields = ['rut', 'first_name', 'last_name', 'email', 'telefono', 'fecha_nacimiento', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['telefono', 'fecha_nacimiento']:
                field.widget.attrs.update({'class': 'form-control'})
                field.widget.attrs['placeholder'] = field.label

        self.fields['rut'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

        self.fields['first_name'].validators.append(validar_longitud_minima)
        self.fields['last_name'].validators.append(validar_longitud_minima)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if MyUser.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electrónico ya está registrado. Por favor, utiliza otro.")
        return email

