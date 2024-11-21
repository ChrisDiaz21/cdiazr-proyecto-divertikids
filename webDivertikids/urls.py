from django.contrib import admin
from django.urls import path
from core import views as views_cor
from login import views as views_log
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views_cor.home,name='home'),
    path('admin/', admin.site.urls),
    path('log_in/', views_log.log_in, name='log_in'),
    path('register/', views_log.register, name='register'),
    path('productos/', views_cor.productos, name='productos'),
    path('carrito/', views_cor.carrito, name='carrito'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="login/password_reset.html"), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="login/password_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="login/password_complete.html"), name='password_reset_complete'),
]
