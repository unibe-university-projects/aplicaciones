from django.db import models
from gestion_personas.models import Persona

class Factura(models.Model):
    numero = models.CharField(max_length=20)
    fecha_emision = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return f"Factura {self.numero} - ${self.total}"
