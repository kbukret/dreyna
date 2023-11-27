from django.contrib.auth.models import AbstractUser
from django.db import models
# from DrSolutionApp.models import Empresa
from Informes.models import GrupoInforme, Empresa


class UsuarioPersonalizado(AbstractUser):
    empresa = models.ForeignKey(
        Empresa, blank=True, null=True, on_delete=models.CASCADE)
    grupoinforme = models.ForeignKey(
        GrupoInforme, blank=True, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='imagen', blank=True, null=True)

    def _str_(self):
        return self


class AccessUser(models.Model):
    user = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=50)
    date_time = models.DateTimeField(
        auto_now_add=True, verbose_name="Login Fecha/Hora")

    def __str__(self):
        return self.ip_address

    class Meta:
        verbose_name = 'Acceso de Usuario'
        verbose_name_plural = 'Accesos de Usuarios'
        db_table = 'accessuser'
        ordering = ['date_time']
        default_permissions = ()
        permissions = (
            ('view_AccessUser', 'Can view Acceso de Usuario'), ('delete_AccessUser',
                                                                'Can delete Acceso de Usuario')
        )
