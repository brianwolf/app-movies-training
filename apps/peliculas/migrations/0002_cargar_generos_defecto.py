from django.db import migrations, models
import django.utils.timezone


def cargar_generos_default(apps, schema_editor):
    generos_peliculas_iniciales = [
        {"id": 1, "nombre": "accion"},
        {"id": 2, "nombre": "aventura"},
        {"id": 3, "nombre": "comedia"},
        {"id": 4, "nombre": "drama"},
        {"id": 5, "nombre": "terror"},
        {"id": 6, "nombre": "fantasia"},
        {"id": 7, "nombre": "ciencia ficcion"},
        {"id": 8, "nombre": "animacion"},
        {"id": 9, "nombre": "documental"},
        {"id": 10, "nombre": "musical"},
        {"id": 11, "nombre": "romance"},
        {"id": 12, "nombre": "crimen"},
        {"id": 13, "nombre": "misterio"},
        {"id": 14, "nombre": "guerra"},
        {"id": 15, "nombre": "historia"},
        {"id": 16, "nombre": "western"},
        {"id": 17, "nombre": "biografia"},
        {"id": 18, "nombre": "de epoca"},
        {"id": 19, "nombre": "superheroes"},
        {"id": 20, "nombre": "deportes"},
    ]
    genero_entity = apps.get_model("peliculas", "GeneroEntity")
    for genero in generos_peliculas_iniciales:
        genero_entity(id=genero["id"], nombre=genero["nombre"]).save()


class Migration(migrations.Migration):
    dependencies = [("peliculas", "0001_migracion_inicial")]
    operations = [migrations.RunPython(cargar_generos_default)]
