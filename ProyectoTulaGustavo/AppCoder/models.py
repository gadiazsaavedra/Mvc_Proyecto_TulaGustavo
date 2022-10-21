from django.db import models
from dataclasses import field
# Create your models here.
class Familiares(models.Model):

    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fechaDeNac = models.IntegerField()
