from django.contrib import admin
from django.urls import path, include
from core import views as views_cor
from login import views as views_log
from games import views as views_game
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns 


urlpatterns = [
    path('',views_cor.home,name='home'),
    path('admin/', admin.site.urls),
    # path('login/', views_log.log_in, name='login'),
    path('accounts/login/', views_log.log_in, name='accounts_login'),
    path('logout', views_log.exit, name='exit'),    
    path('register/', views_log.register, name='register'),
    path('productos/', views_game.productos, name='productos'),
    path('carrito/', views_cor.carrito, name='carrito'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    


    # estos son las url de django para la recuperacione de contraseña 
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="login/password_reset.html"), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="login/password_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="login/password_complete.html"), name='password_reset_complete'),

]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)




urlpatterns += i18n_patterns( path('admin/', admin.site.urls), )