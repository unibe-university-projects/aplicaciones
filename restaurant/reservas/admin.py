from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('ingreso', 'salida', 'confirmacion', 'caducidad','estado','usuario')
    list_filter = ('ingreso', 'usuario')
    search_fields = ('usuario',)
    date_hierarchy = 'ingreso'