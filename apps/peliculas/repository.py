"""
Archivo donde se define la interfaz entre las capas de NEGOCIOS
y DATOS,

CAPA PRESENTACION<--dto.py-->CAPA NEGOCIO<--repository.py-->CAPA DE DATOS
     (jsons)                  clases.py                       models.py
                              (clases)                        (entities)
"""
# TODO: si se borra algo, la enumeracion de IDs continua desde el ultimo borrado. Ej: borro ID5, el siguiente elmento va a tener ID6 en vez de 5
from core.exception import AppException
from peliculas.classes import Genero, Pelicula
from peliculas.error import PeliculasError
from peliculas.models import GeneroEntity, PeliculaEntity


def list() -> list[int]:
    search = PeliculaEntity.objects.all()
    return [pelicula.id for pelicula in search] if search.exists() else []


def get(id: int) -> Pelicula:
    search = PeliculaEntity.objects.filter(id=id)
    return search.get().to_class() if search.exists() else None


def save(pelicula: Pelicula) -> int:
    # Primero se guarda la pelicula
    # TODO: Si rompe algo de genero,la pelicula se guarda. Creo que no deberia guardarse...
    pelicula_entity = PeliculaEntity.from_class(pelicula)
    pelicula_entity.save()
    # Segundo se guardan los generos
    for genero in pelicula.generos:
        genero_entity = GeneroEntity.get_by_object(genero)
        if not genero_entity:
            genero.id = None
            genero_entity = GeneroEntity.from_class(genero)
            genero_entity.save()
        # Tercero se gurda la relacion Many to many
        pelicula_entity.generos.add(genero_entity)
    return pelicula_entity.id


def delete(id: int):
    search = PeliculaEntity.objects.filter(id=id)
    if not search.exists():
        msj = f"Example with id {id} not exist"
        raise AppException(PeliculasError.PELICULA_OBJECT_NOT_EXIST, msj)
    search.delete()
