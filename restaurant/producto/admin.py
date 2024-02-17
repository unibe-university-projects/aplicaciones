from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoMenuAdmin(admin.ModelAdmin):
   # list_display = ('name')
   # list_filter = ('name')
    search_fields = ('description',)