from django.contrib import admin
from .models import TipoMenu

@admin.register(TipoMenu)
class TipoMenuAdmin(admin.ModelAdmin):
   # list_display = ('name')
   # list_filter = ('name')
    search_fields = ('name',)