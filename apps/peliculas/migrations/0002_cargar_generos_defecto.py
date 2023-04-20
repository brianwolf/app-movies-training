from django.db import migrations, models
import django.utils.timezone


def cargar_generos_default(apps, schema_editor):
    generos_peliculas_iniciales = [
        {"id": 1, "nombre": "Acción"},
        {"id": 2, "nombre": "Aventura"},
        {"id": 3, "nombre": "Comedia"},
        {"id": 4, "nombre": "Drama"},
        {"id": 5, "nombre": "Terror"},
        {"id": 6, "nombre": "Fantasía"},
        {"id": 7, "nombre": "Ciencia ficción"},
        {"id": 8, "nombre": "Animación"},
        {"id": 9, "nombre": "Documental"},
        {"id": 10, "nombre": "Musical"},
        {"id": 11, "nombre": "Romance"},
        {"id": 12, "nombre": "Crimen"},
        {"id": 13, "nombre": "Misterio"},
        {"id": 14, "nombre": "Guerra"},
        {"id": 15, "nombre": "Historia"},
        {"id": 16, "nombre": "Western"},
        {"id": 17, "nombre": "Biografía"},
        {"id": 18, "nombre": "De época"},
        {"id": 19, "nombre": "Superhéroes"},
        {"id": 20, "nombre": "Deportes"},
    ]
    GeneroEntity = apps.get_model("peliculas", "GeneroEntity")
    for genero in generos_peliculas_iniciales:
        GeneroEntity(id=genero["id"], nombre=genero["nombre"]).save()


class Migration(migrations.Migration):
    dependencies = [("peliculas", "0001_migracion_inicial")]
    operations = [migrations.RunPython(cargar_generos_default)]
