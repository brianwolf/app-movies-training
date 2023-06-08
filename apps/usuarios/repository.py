from core.exception import AppException
from usuarios.classes import Usuarios
from usuarios.error import UsuarioError
from usuarios.models import UsuariosEntity


def list() -> list[int]:
    search = UsuariosEntity.objects.all()

    if search.exists():
        return [e.id for e in search]
    return []


def get(id: int) -> Usuarios:
    search = UsuariosEntity.objects.filter(id=id)

    if search.exists():
        return search.get().to_class()
    return None


def save(usuario_info: Usuarios) -> int:
    entity = UsuariosEntity.from_class(usuario_info)
    entity.save()
    return entity.id


def delete(id: int):
    search = UsuariosEntity.objects.filter(id=id)

    if not search.exists():
        msj = f'UsuarioInfo with id {id} not exist'
        raise AppException(UsuarioError.USUARIO_OBJECT_NOT_EXIST, msj)
    search.delete()
