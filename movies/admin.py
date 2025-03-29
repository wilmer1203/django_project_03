from django.contrib import admin
from .models import Pelicula

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'año', 'genero', 'director')
    search_fields = ('titulo', 'director')
    list_filter = ('genero', 'año')