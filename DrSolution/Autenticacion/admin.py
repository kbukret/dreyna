from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado, AccessUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.html import format_html


class UsuarioPersonalizadoAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UsuarioPersonalizado
    list_display = [
        "username",
        "grupoinforme",
        "empresa",
        'avatar',
    ]
    fieldsets = UserAdmin.fieldsets + \
        ((None, {"fields": ("grupoinforme", "empresa", "avatar")}),)
    add_fieldsets = UserAdmin.add_fieldsets + \
        ((None, {"fields": ("grupoinforme", "empresa", "avatar")}),)

    def avatar(self, obj):
        return format_html('<img src={} style= "height:30px" />', obj.avatar.url)


class AccessUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'date_time')
    readonly_fields = ('user', 'ip_address', 'date_time')
    list_filter = ['user']
    ordering = ['ip_address']


admin.site.register(UsuarioPersonalizado, UsuarioPersonalizadoAdmin)
admin.site.register(AccessUser, AccessUserAdmin)
