from django.db import models

class Habitacion(models.Model):
    precio_noche = models.IntegerField()
    no_dormitorios = models.IntegerField()
    descripcion = models.CharField(max_length=255)
    
