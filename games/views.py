from django.shortcuts import render
from .models import Products

# Create your views here.
def productos(request):
    productos=Products.objects.all()
    return render(request,"core/productos.html",{'productos':productos})
