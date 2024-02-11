from django.contrib import admin
from .models import Factura

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha_emision', 'total', 'persona')
    list_filter = ('fecha_emision', 'persona')
    search_fields = ('numero', 'persona__nombre')
    date_hierarchy = 'fecha_emision'
