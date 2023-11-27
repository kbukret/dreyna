from django.contrib import admin
from .models import Informe, GrupoInforme, MenuInforme, InformeEmpresa, Empresa
from django.utils.html import format_html


class InformeAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'menu')
    list_filter = ['menu']
    ordering = ['descripcion']
    readonly_fields = ('created', 'updated')


class MenuInformeAdmin(admin.ModelAdmin):
    ordering = ['nombre']


class GrupoInformeAdmin(admin.ModelAdmin):
    ordering = ['nombre']


class InformeEmpresaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'informe', 'url')
    list_filter = ['empresa', 'informe']
    ordering = ['empresa', 'informe']


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'mail', 'foto')

    def foto(self, obj):
        return format_html('<img src={} style= "height:30px" />', obj.logo.url)


admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Informe, InformeAdmin)
admin.site.register(MenuInforme, MenuInformeAdmin)
admin.site.register(GrupoInforme, GrupoInformeAdmin)
admin.site.register(InformeEmpresa, InformeEmpresaAdmin)
