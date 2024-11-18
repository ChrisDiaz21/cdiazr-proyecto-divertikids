from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('log_in/', views.log_in, name='log_in'),
    path('register/', views.register, name='register'),
    path('productos/', views.productos, name='productos'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="core/password_reset.html"), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="core/password_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="core/password_complete.html"), name='password_reset_complete'),
]
