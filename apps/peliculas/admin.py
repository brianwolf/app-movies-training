"""
Archivo para la configuracion del administrador
"""
from django.contrib import admin

from .models import PeliculaEntity

admin.site.register(PeliculaEntity)
