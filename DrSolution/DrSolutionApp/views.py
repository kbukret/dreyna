from django.views.generic import TemplateView
from django.views import View
from Informes.models import Informe, GrupoInforme, MenuInforme, Empresa
from django.shortcuts import render
# from DrSolutionApp.models import Empresa
from Informes.models import Informe, MenuInforme, GrupoInforme, InformeEmpresa
from Autenticacion.models import UsuarioPersonalizado
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template import loader, RequestContext
import os

user = get_user_model()


@login_required
def separaDatos(request):
    lista = []
    grupoinforme = ''
    menuinforme = []
    if user.is_authenticated:
        grupoinforme = request.user.grupoinforme
        menuinforme = InformeEmpresa.objects.filter(
            informe__grupos__nombre=request.user.grupoinforme, empresa__descripcion=request.user.empresa)

        for menu in menuinforme:
            lista.append(menu.informe.menu)

    return {'informes': menuinforme, 'grupoinforme': grupoinforme, 'menu': set(lista)}


@login_required
def home(request):
    lista = []
    grupoinforme = ''
    menuinforme = []
    # if request.user.is_authenticated:
    si = True
    grupoinforme = request.user.grupoinforme
    menuinforme = InformeEmpresa.objects.filter(
        informe__grupos__nombre=request.user.grupoinforme, empresa__descripcion=request.user.empresa)

    for menu in menuinforme:
        lista.append(menu.informe.menu)

    return render('Home.html', {'informes': menuinforme, 'grupoinforme': grupoinforme, 'menu': set(lista), 'si': si})

    # t = loader.get_template('Home.html')
    # c = RequestContext(request, processors=[separaDatos])
    # return t.render(c)
