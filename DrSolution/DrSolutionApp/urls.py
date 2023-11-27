from DrSolutionApp import views
from django.urls import path, include
from django.contrib.auth.decorators import login_required
# from .views import home

urlpatterns = [
    path('', include('Autenticacion.urls')),
    path('home/', login_required(views.home), name='Home'),
]
