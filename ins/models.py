from django.db import models

# Create your models here.

class covid(models.Model):
  
    fecha_de_notificaci_n = models.DateField(null=True)
    departamento = models.PositiveIntegerField(null=True)
    departamento_nom = models.CharField(null=True, max_length=30)
    ciudad_municipio = models.PositiveIntegerField(null=True),
    ciudad_municipio_nom = models.CharField(null=True, max_length=30)
    edad = models.PositiveIntegerField(null=True)
    unidad_medida = models.PositiveIntegerField(null=True)
    sexo = models.CharField(null=True, max_length=30)
    fuente_tipo_contagio = models.CharField(null=True, max_length=30)
    ubicacion = models.CharField(null=True, max_length=30)
    estado = models.CharField(null=True, max_length=30)
    pais_viajo_1_cod = models.PositiveIntegerField(null=True)
    pais_viajo_1_nom = models.CharField(null=True, max_length=30)
    recuperado = models.CharField(null=True, max_length=30)
    fecha_inicio_sintomas = models.DateField(null=True)
    fecha_diagnostico = models.DateField(null=True)
    fecha_recuperado = models.DateField(null=True)
    tipo_recuperacion = models.CharField(null=True, max_length=30)
    nom_grupo = models.CharField(null=True, max_length=200)
    fecha_muerte = models.DateField(null=True, default=None)