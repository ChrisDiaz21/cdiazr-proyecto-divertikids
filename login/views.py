from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login
from .forms import forms_login, CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth.decorators import login_required


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
                messages.error(request, "Las credenciales son incorrectas o el usuario no existe.")
    else:
        form = forms_login()
        
    return render(request, "login/log_in.html" , {'form': form})

def register(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        User_Creation_form = CustomUserCreationForm(data=request.POST)
        
        if User_Creation_form.is_valid():
            User_Creation_form.save()
            return redirect('log_in')  # Redirige a la página de login después de registrar

    else:
        form = CustomUserCreationForm()

    return render(request, "registration/register.html",data)