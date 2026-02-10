from django.db import models
import datetime

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length = 60)
    apellidos = models.CharField(max_length = 60)
    organizacion = models.CharField(max_length = 100)
    nacimiento = models.DateField()
    
    def __str__(self):
        return "{0} {1}".format(
            self.nombres, self.apellidos)

    def es_menor(self):
        return ((datetime.date.today()
                 - self.nacimiento).days / 365.25) < 18

class Localizador(models.Model):
    persona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    tipo = models.IntegerField(default = 0)
    valor = models.CharField(max_length = 200)

    def __str__(self):
        return "{0} {1}".format(
            self.tipo, self.valor)
