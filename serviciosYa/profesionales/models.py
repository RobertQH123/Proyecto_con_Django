from django.db import models
from django.urls import reverse

# Create your models here.

class Profesional(models.Model):
  nombre = models.CharField(max_length = 30)
  apellido = models.CharField(max_length = 30)
  fechaNac = models.DateField()
  telefono = models.IntegerField()
  profesion = models.CharField(max_length = 30)
  foto = models.ImageField(upload_to='img/')

  def get_absolute_url(self):
      return reverse('profesionales:profesional-detail', kwargs = {'pk': self.id})
