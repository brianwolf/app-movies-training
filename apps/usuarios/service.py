from usuarios import repository
from usuarios.classes import Usuarios


def list():
    return repository.list()


def get(id: int) -> Usuarios : 
    return repository.get(id)


def save(usuario: Usuarios) -> int:
    return repository.save(usuario)


def delete(id: int):
    repository.delete(id)
