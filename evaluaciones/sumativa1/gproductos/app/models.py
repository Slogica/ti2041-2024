from django.db import models

# Create your models here.

class Productos(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return self.nombre