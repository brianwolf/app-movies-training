from datetime import datetime

from usuariosInfo.classes import UsuariosInfo


def usuarioI_to_json(e: UsuariosInfo) -> dict[str, object]:
    return {
        'id': e.id,
        'nombre': e.nombre,
        'apellido':e.apellido,
        'email': e.email,
        'fecha': e.fecha.isoformat(), #y esto que era ya me olvide
    }


def json_to_usuarioI(d: dict[str, object]) -> UsuariosInfo:
    return UsuariosInfo(
        id=d.get('id', None),
        nombre=d['nombre'],
        apellido=d['apellido'],
        email=d['email'],
        fecha=datetime.fromisoformat(d['fecha']),
    )
