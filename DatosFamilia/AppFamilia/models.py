from django.db import models

# Create your models here.

class Datos_familiares(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    cumpleaños = models.DateField()
    