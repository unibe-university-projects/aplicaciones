from django.db import models
from django.contrib.auth.models import User
# from   import Usuario
# from gestion_facturas.models import Factura

class Reserva(models.Model):
    ingreso = models.DateTimeField()
    salida = models.DateTimeField()
    confirmacion = models.BooleanField()
    caducidad = models.DateTimeField()
    estado = models.BooleanField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # factura = models.ForeignKey('gestion_facturas.Factura', on_delete=models.CASCADE)



# class reserva_cliente(models.Model):

    def __str__(self):
        return f"reserva {self.usuario} - ${self.salida}"