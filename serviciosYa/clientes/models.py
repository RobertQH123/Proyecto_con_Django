from django.db import models
from django.urls import reverse

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length = 50)
    fecha = models.DateField()

    def get_absolute_url(self):
        return reverse('clientes:cliente-detail', kwargs = {'pk' : self.id})
