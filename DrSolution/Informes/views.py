from django.shortcuts import render, HttpResponse, get_object_or_404
from django.utils.safestring import mark_safe
from .models import InformeEmpresa, Informe
from Autenticacion.models import UsuarioPersonalizado
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.

user = get_user_model()


@login_required
def informes(request, pk, desc):
    lista = []
    grupoinforme = ''
    menuinforme = []
    try:
        grupoinforme = request.user.grupoinforme
        empresa = request.user.empresa
        menuinforme = Informe.objects.prefetch_related().filter(
            grupos=request.user.grupoinforme)

        for menu in menuinforme:
            lista.append(menu.menu)

        # info = get_object_or_404(InformeEmpresa, id=pk)
        info = InformeEmpresa.objects.filter(
            informe=pk, empresa=request.user.empresa).values_list('url')
        url = None
        if info:
            url = mark_safe(info[0])

        return render(request, 'informes/informe.html', {'informes': menuinforme, 'grupoinforme': grupoinforme, 'menu': set(lista), 'iframe': url, 'titulo': desc})
    except:
        return render(request, 'informes/informe.html', {'informes': menuinforme, 'grupoinforme': grupoinforme, 'menu': set(lista), 'iframe': 'None', 'titulo': ''})


@login_required
def informesv(request):
    lista = []
    grupoinforme = request.user.grupoinforme
    menuinforme = Informe.objects.prefetch_related().filter(
        grupos=request.user.grupoinforme)

    for menu in menuinforme:
        lista.append(menu.menu)
    return render(request, 'Informes/informev.html',  {'informes': menuinforme, 'grupoinforme': grupoinforme, 'menu': set(lista)})
