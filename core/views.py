from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "core/index.html")

@login_required
def carrito(request):
    # Lógica para el carrito
    return render(request, 'core/carrito.html')  # Asegúrate de que la ruta sea correcta
