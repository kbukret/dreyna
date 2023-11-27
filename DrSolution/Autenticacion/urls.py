from django.urls import path
from .views import Vlogin, cerrar_sesion, MyPasswordChangeView, MyPasswordResetDoneView
from django.contrib.auth import views as auth_views

from django.contrib.auth.views import LoginView


urlpatterns = [
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('', LoginView.as_view(
        template_name='autenticacion/login.html'), name='login'),
    path('autenticacion/changePassword/',
         MyPasswordChangeView.as_view(), name='changePass'),
    path('autenticacion/changePasswordDone/', MyPasswordResetDoneView.as_view(), name='changePassDone')]
