"""
Archivo donde se define la interfaz entre las capas de 
PRESENTACION y NEGOCIOS

CAPA PRESENTACION<--dto.py-->CAPA NEGOCIO<--repository.py-->CAPA DE DATOS
     (jsons)                  clases.py                       models.py
                              (clases)                        (entities)
"""
from datetime import datetime

from peliculas.classes import Genero, Pelicula


def genero_a_json(genero: Genero) -> dict[str, object]:
    return {
        "id": genero.id,
        "nombre": genero.nombre,
    }


def json_a_genero(genero_dict: dict[str, object]) -> Genero:
    return Genero(
        nombre=genero_dict["nombre"].lower(),
    )


def pelicula_a_json(pelicula: Pelicula) -> dict[str, object]:
    return {
        "id": pelicula.id,
        "nombre": pelicula.nombre,
        "fecha_estreno": pelicula.fecha_estreno,
        "generos": [genero_a_json(genero) for genero in pelicula.generos],
        "puntuacion": pelicula.puntuacion,
    }


def json_a_pelicula(pelicula_dict: dict[str, object]) -> Pelicula:
    return Pelicula(
        nombre=pelicula_dict["nombre"],
        fecha_estreno=pelicula_dict["fecha_estreno"],
        generos=[json_a_genero(genero) for genero in pelicula_dict["generos"]],
        puntuacion=pelicula_dict["puntuacion"],
    )
