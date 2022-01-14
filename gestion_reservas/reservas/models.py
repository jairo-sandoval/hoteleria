from django.db import models
import datetime

METODOS_DE_PAGO = (
    ('mastercard', 'mastercard'),
    ('visa', 'visa'),
)

class Pago(models.Model):
    numero_targeta = models.IntegerField()
    metodo_pago = models.CharField(max_length=100, choices= METODOS_DE_PAGO)
    cvc = models.IntegerField()

    def __str__(self):
        return f'{self.metodo_pago} {self.cvc}'

class Facturacion(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_emision = datetime.datetime.now()
    no_identificacion = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    

class Reserva(models.Model):
    no_noches = models.IntegerField()
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE, null= True)
    facturacion = models.ForeignKey(Facturacion, on_delete=models.CASCADE, null= True)









