from django.contrib import admin
from .models import Gasto

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'monto', 'fecha', 'categoria')
    list_filter = ('fecha', 'categoria')
    search_fields = ('descripcion',)
    date_hierarchy = 'fecha'
