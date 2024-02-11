from django.contrib import admin
from .models import Pago

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('monto', 'fecha', 'usuario', 'factura')
    list_filter = ('fecha', 'usuario')
    search_fields = ('usuario__nombre_usuario', 'factura__numero')
    date_hierarchy = 'fecha'
