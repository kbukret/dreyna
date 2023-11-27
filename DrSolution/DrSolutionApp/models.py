# from django.db import models
# from Informes.models import Informe, InformeGrupoEmpresa, GrupoInforme


# class Empresa(models.Model):
#     nombre = models.CharField(max_length=20)
#     descripcion = models.CharField(max_length=50)
#     direccion = models.CharField(max_length=50)
#     mail = models.CharField(max_length=50, blank=True, null=True)
#     logo = models.ImageField(upload_to='imagen', blank=True, null=True)
#     informes = models.ManyToManyField(Informe, through='InformeGrupoEmpresa')
#     grupos = models.ManyToManyField(GrupoInforme)

#     class Meta:
#         verbose_name = 'Empresa'
#         verbose_name_plural = 'Empresas'
#         db_table = 'empresa'
#         ordering = ['nombre']

#     def __str__(self):
#         return (self.descripcion)
