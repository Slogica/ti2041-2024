from django.db import models
from django.utils import timezone

# Create your models here.
class Tipo(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    

class Mascota(models.Model):
    GENERO_MASCOTA = {
        "M": "Macho",
        "H": "Hembra"
    }

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, default="Sin nombre")
    tipo = models.CharField(Tipo, null=False)
    raza = models.CharField(max_length=50)
    tamano = models.FloatField(null=False)
    peso = models.FloatField(null=False)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    genero = models.CharField(max_length=1, choices=GENERO_MASCOTA)
    descripcion = models.TextField()
    fecha_registro = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.nombre
