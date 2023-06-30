from core.exception import AppException
from usuarios.classes import Usuarios
from usuarios.error import UsuarioError
from usuarios.models import UsuariosEntity
from apps.example.repository import delete, save


def list() -> list[int]:
    search = UsuariosEntity.objects.all()

    if search.exists():
        return [e.id_usuario for e in search]
    return []


def get(id: int) -> Usuarios:
    search = UsuariosEntity.objects.filter(id_usuario=id)
    if search.exists():
        return search.get().to_class()
    return None


def save(usuario_info: Usuarios) -> int:
    entity = UsuariosEntity.from_class(usuario_info)
    entity.info.save()
    entity.save()
    return entity.id_usuario


def delete(id: int):
    usuario_entity = UsuariosEntity.objects.filter(id_usuario=id).first()
    print(usuario_entity)

    if usuario_entity is None:
        msj = f'UsuarioInfo with id {id} not exist'
        raise AppException(UsuarioError.USUARIO_OBJECT_NOT_EXIST, msj)
    
    usuario_entity.info.delete()
    usuario_entity.delete()
