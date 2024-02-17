from django.contrib import admin
from .models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('tipoMenu', 'producto')
    list_filter = ('tipoMenu', 'producto')
    search_fields = ('producto',)