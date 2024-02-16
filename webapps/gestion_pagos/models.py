from django.db import models
from gestion_usuarios.models import Usuario
from gestion_facturas.models import Factura

class Pago(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    factura = models.ForeignKey('gestion_facturas.Factura', on_delete=models.CASCADE)

    def __str__(self):
        return f"Pago de {self.usuario} - ${self.monto}"
