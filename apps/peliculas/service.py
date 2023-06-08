from peliculas import repository
from peliculas.classes import Pelicula


def list():
    return repository.list()


def get(id: int) -> Pelicula:
    return repository.get(id)


def save(pelicula: Pelicula) -> int:
    return repository.save(pelicula)


def delete(id: int):
    repository.delete(id)
