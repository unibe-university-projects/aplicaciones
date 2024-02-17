from django.db import models

class Producto(models.Model):
    description = models.CharField(max_length=230)


    def __str__(self):
        return f"reserva {self.description}"