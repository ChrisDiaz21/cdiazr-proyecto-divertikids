from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('log_in/', views.log_in, name='log_in'),
    path('register/', views.register, name='register'),
    path('productos/', views.productos, name='productos'),
]
