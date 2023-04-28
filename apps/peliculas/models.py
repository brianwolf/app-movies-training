"""
Archivo donde se definen las entidades para la CAPA DE DATOS
y donde se configuran las bases para crear el primer archivo
de migracion.

CAPA PRESENTACION<--dto.py-->CAPA NEGOCIO<--repository.py-->CAPA DE DATOS
     (jsons)                  clases.py                       models.py
                              (clases)                        (entities)
"""
from django.db import models
from django.utils import timezone
from typing import Optional

from peliculas.classes import Genero, Pelicula


class GeneroEntity(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = "GENEROS"

    def __str__(self) -> str:
        return f"id: {self.id}, nombre: {self.nombre}"

    def to_class(self) -> "Genero":
        return Genero(
            id=self.id,
            nombre=self.nombre,
        )

    @classmethod
    def buscar_genero_en_DB(cls, genero: Genero) -> Optional["GeneroEntity"]:
        try:
            genero_query = GeneroEntity.objects.filter(
                models.Q(nombre=genero.nombre) | models.Q(id=genero.id)
            )
            assert (
                genero_query.count() <= 1
            ), f"Se encontro mas de un genero para el id y nombre dado: {genero_query}"
            return genero_query.get()
        except cls.DoesNotExist:
            return None

    @staticmethod
    def from_class(genero: Genero) -> "GeneroEntity":
        return GeneroEntity(id=genero.id, nombre=genero.nombre)


class PeliculaEntity(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    fecha_estreno = models.DateTimeField(default=timezone.now)
    puntuacion = models.DecimalField(decimal_places=2, max_digits=4)
    generos = models.ManyToManyField(GeneroEntity)

    class Meta:
        db_table = "PELICULAS"

    def __str__(self) -> str:
        return f"id: {self.id}, nombre: {self.nombre}"

    def extraer_nuevos_generos(self):
        pass

    def to_class(self) -> "Pelicula":
        return Pelicula(
            id=self.id,
            nombre=self.nombre,
            fecha_estreno=self.fecha_estreno,
            generos=[genero for genero in self.generos.all()],
            puntuacion=self.puntuacion,
        )

    @staticmethod
    def from_class(movie: Pelicula) -> "PeliculaEntity":
        return PeliculaEntity(
            id=movie.id,
            nombre=movie.nombre,
            fecha_estreno=movie.fecha_estreno,
            puntuacion=movie.puntuacion,
        )
