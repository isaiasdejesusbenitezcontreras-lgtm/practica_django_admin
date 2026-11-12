from django.contrib import admin
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'lugar')
    search_fields = ('titulo', 'lugar', 'descripcion')
    list_filter = ('fecha', 'lugar')
    date_hierarchy = 'fecha'
    ordering = ('-fecha',)
    list_per_page = 10

