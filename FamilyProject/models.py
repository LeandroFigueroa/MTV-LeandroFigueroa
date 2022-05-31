from errno import EDEADLK
from django.db import models

# Create your models here.
class ModeloFamilia(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    edad = models.IntegerField(null=False)
    fdn = models.DateField()
    parentesco = models.CharField(max_length=20)

