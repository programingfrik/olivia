from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length = 60)
    apellidos = models.CharField(max_length = 60)
    organizacion = models.CharField(max_length = 100)
    nacimiento = models.DateField()

class Localizador(models.Model):
    persona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    tipo = models.IntegerField(default = 0)
    valor = models.CharField(max_length = 200)
