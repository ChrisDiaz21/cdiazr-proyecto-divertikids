from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,"core/index.html")



def productos(request):
    return render(request, "core/productos.html")

def carrito(request):
    return render(request, "core/carrito.html")
