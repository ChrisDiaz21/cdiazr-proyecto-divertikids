from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login,logout
from .forms import forms_login, CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def log_in(request):
    if request.method == "POST":
        form = forms_login(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)  # Encuentra el usuario por email
            except User.DoesNotExist:
                user = None

            if user is not None and user.check_password(password):  # Verifica la contraseña
                login(request, user)  
                # Redirige según el tipo de usuario
                if user.is_superuser:
                    return redirect('/admin/')
                return redirect('home')  # Redirige al home si es un usuario normal
            else:
                messages.error(request, "¡Ups! No pudimos encontrar una cuenta con ese correo electrónico o la contraseña ingresada es incorrecta. Por favor, verifica tus datos e inténtalo de nuevo.")
    else:
        form = forms_login()
        
    return render(request, "registration/login.html" , {'form': form})

def register(request):
    
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige a la página de login después de registrar

    else:
        form = CustomUserCreationForm()

    data={
        'form':form
    }

    return render(request, "registration/register.html",data)

def exit (request):
    logout(request)
    return redirect('home')