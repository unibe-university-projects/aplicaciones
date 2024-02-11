from django.contrib import admin
from .models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'direccion', 'telefono')
    search_fields = ('nombre', 'direccion', 'telefono')
