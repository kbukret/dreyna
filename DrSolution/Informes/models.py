from django.db import models
# from DrSolutionApp.models import Empresa


class MenuInforme(models.Model):
    nombre = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'MenuInforme'
        db_table = 'menu'

    def __str__(self):
        return self.nombre


class GrupoInforme(models.Model):
    nombre = models.CharField(max_length=20)
    # empresa = models.ManyToManyField(Empresa)

    class Meta:
        verbose_name = 'GrupoInforme'
        verbose_name_plural = 'Grupos'
        db_table = 'grupo'

    def __str__(self):
        return self.nombre


class Informe(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    menu = models.ForeignKey(
        MenuInforme, null=True, blank=True, on_delete=models.CASCADE)
    grupos = models.ManyToManyField(GrupoInforme)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Creado Fecha")
    updated = models.DateTimeField(
        auto_now_add=True, verbose_name="Actualizado Fecha")
    # empresas = models.ManyToManyField(Empresa, through='InformeGrupoEmpresa')

    class Meta:
        verbose_name = 'Informe'
        db_table = 'informe'

    def __str__(self):
        return self.descripcion


class Empresa(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    mail = models.CharField(max_length=50, blank=True, null=True)
    logo = models.ImageField(upload_to='imagen', blank=True, null=True)
    informes = models.ManyToManyField(Informe, through='InformeEmpresa')
    grupos = models.ManyToManyField(GrupoInforme)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        db_table = 'empresa'
        ordering = ['nombre']

    def __str__(self):
        return (self.descripcion)


class InformeEmpresa(models.Model):
    empresa = models.ForeignKey(
        Empresa, null=True, blank=True, on_delete=models.CASCADE)
    informe = models.ForeignKey(Informe, null=True,
                                blank=True, on_delete=models.CASCADE)
    url = models.TextField(
        max_length=400, verbose_name="Iframe", blank=True, null=True)

    class Meta:
        verbose_name = 'Informe PowerBI'
        verbose_name_plural = 'Informes PowerBI'
        db_table = 'InformeUrl'

    def __str__(self):
        return self.informe.descripcion
