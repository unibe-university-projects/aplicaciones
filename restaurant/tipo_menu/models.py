from django.db import models

class TipoMenu(models.Model):
    name = models.CharField(max_length=230)


    def __str__(self):
        return f"reserva {self.name}"