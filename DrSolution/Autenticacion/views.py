from django.forms.forms import BaseForm
from django.shortcuts import render, redirect
from django.views.generic import View, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from Autenticacion.models import UsuarioPersonalizado, AccessUser
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView


# User = get_user_model()


@login_required
class Vlogin(LoginRequiredMixin, View):
    login_url = '/'
    # redirect_field_name = 'redirect_to'

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'autenticacion/autenticacion.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            AccessUser(user=form.get_user(),
                       ip_address=self.request.META['REMOTE_ADDR']).save()
            login(request, usuario)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request, 'autenticacion/autenticacion.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('/')


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'autenticacion/changePassword.html'
    success_url = reverse_lazy('login')


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'autenticacion/changePasswordDone.html'
