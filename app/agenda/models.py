from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Persona(models.Model):
    idPersona = models.AutoField(primary_key=True, auto_created=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    email=models.EmailField()
    celular=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"