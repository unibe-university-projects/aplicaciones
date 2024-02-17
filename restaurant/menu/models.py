from django.db import models
from producto.models  import Producto
from tipo_menu.models import TipoMenu

class Menu(models.Model):
    
    tipoMenu= models.ForeignKey(TipoMenu, on_delete=models.CASCADE)
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f"reserva {self.tipoMenu} - ${self.producto}"