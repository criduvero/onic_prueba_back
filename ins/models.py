from django.db import models

# Create your models here.

class covid(models.Model):
  
    fecha_de_notificaci_n = models.DateTimeField()
    departamento = models.PositiveIntegerField()
    departamento_nom = models.CharField(max_length=30)
    ciudad_municipio = models.PositiveIntegerField(),
    ciudad_municipio_nom = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()
    unidad_medida = models.PositiveIntegerField()
    sexo = models.CharField(max_length=30)
    fuente_tipo_contagio = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    pais_viajo_1_cod = models.PositiveIntegerField()
    pais_viajo_1_nom = models.CharField(max_length=30)
    recuperado = models.CharField(max_length=30)
    fecha_inicio_sintomas = models.DateTimeField()
    fecha_diagnostico = models.DateTimeField()
    fecha_recuperado = models.DateTimeField()
    tipo_recuperacion = models.CharField(max_length=30)
    per_etn = models.PositiveIntegerField()