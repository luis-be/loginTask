from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('correo_electronico', 'password')}),
        (_('Personal info'), {'fields': ('nombre_de_usuario', 'edad')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'fecha_union')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('correo_electronico', 'nombre_de_usuario', 'password1', 'password2'),
        }),
    )
    list_display = (
        'correo_electronico',
        'nombre_de_usuario',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    search_fields = ('correo_electronico', 'nombre_de_usuario')
    ordering = ('correo_electronico',)

admin.site.register(CustomUser, UserAdmin)
