from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

# Register your models here.
class MyUserAdmin(UserAdmin):
    model = MyUser
    list_display = ('rut', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('rut', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'fecha_nacimiento', 'telefono')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('rut', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('rut', 'email', 'first_name', 'last_name')
    ordering = ('rut',)

admin.site.register(MyUser, MyUserAdmin)