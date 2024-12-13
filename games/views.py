from django.shortcuts import render
from .models import Products

# Vista para mostrar los productos
def productos(request):
    productos = Products.objects.all()
    return render(request, "core/productos.html", {'productos': productos})
