from core.exception import AppException
from usuariosInfo.classes import UsuariosInfo
from usuariosInfo.error import UsuarioInfoError
from usuariosInfo.models import UsuariosInfoEntity


def list() -> list[int]:
    search = UsuariosInfoEntity.objects.all()

    if search.exists():
        return [e.id for e in search]
    return []


def get(id: int) -> UsuariosInfo:
    search = UsuariosInfoEntity.objects.filter(id=id)

    if search.exists():
        return search.get().to_class()
    return None


def save(usuario_info: UsuariosInfo) -> int:
    entity = UsuariosInfoEntity.from_class(usuario_info)
    entity.save()
    return entity.id


def delete(id: int):
    search = UsuariosInfoEntity.objects.filter(id=id)

    if not search.exists():
        msj = f'UsuarioInfo with id {id} not exist'
        raise AppException(UsuarioInfoError.USUARIO_OBJECT_NOT_EXIST, msj)
    search.delete()
