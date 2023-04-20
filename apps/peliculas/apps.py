"""
Archivo par ala configuracion particular de la aplicacion peliculas
"""
from django.apps import AppConfig


class PeliculasConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "peliculas"
