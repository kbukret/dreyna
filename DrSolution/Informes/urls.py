from django.urls import path
from . import views
from Informes.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('informe/<int:pk>/<str:desc>',
         login_required(views.informes), name='Informes'),
    path('informesv',
         login_required(views.informesv), name='Informesv'),


]
