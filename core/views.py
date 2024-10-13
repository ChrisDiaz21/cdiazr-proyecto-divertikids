from django.shortcuts import render, redirect, HttpResponse

def home(request):
    return render(request,"core/index.html")

def log_in(request):
    return render(request, "core/log_in.html")

def register(request):
    return render(request, "core/register.html")
