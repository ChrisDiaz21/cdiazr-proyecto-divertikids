from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout
from .forms import forms_login, CustomUserCreationForm
from .models import MyUser  # Importa tu modelo de usuario personalizado
from django.contrib import messages

# Create your views here.
def log_in(request):
    if request.method == "POST":
        form = forms_login(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = MyUser.objects.get(email=email)  # Encuentra el usuario por email
            except MyUser.DoesNotExist:
                user = None

            if user is not None and user.check_password(password):  # Verifica la contraseña
                login(request, user)  
                # Redirige según el tipo de usuario
                if user.is_superuser:
                    return redirect('/admin/')
                return redirect('home')  # Redirige al home si es un usuario normal
            else:
                messages.error(request, "Las credenciales son incorrectas o el usuario no existe.")
    else:
        form = forms_login()
        
    return render(request, "registration/login.html", {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.rut  # Asegúrate de que el campo username se llene con el RUT
            user.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
       
    data = {
        'form': form
    }

    return render(request, "registration/register.html", data)

def exit(request):
    logout(request)
    return redirect('home')
