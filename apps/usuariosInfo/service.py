from usuariosInfo import repository
from usuariosInfo.classes import UsuariosInfo


def list():
    return repository.list()


def get(id: int) -> UsuariosInfo : 
    return repository.get(id)


def save(usuario_info: UsuariosInfo) -> int:
    return repository.save(usuario_info)


def delete(id: int):
    repository.delete(id)
