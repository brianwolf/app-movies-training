from datetime import datetime

from usuarios.classes import Usuarios
from usuariosInfo.classes import UsuariosInfo
from usuariosInfo.dto import usuarioI_to_json, json_to_usuarioI

def usuario_to_json(e: Usuarios) -> dict[str, object]:
    return {
        'nick': e.nick,
        'password':e.password,
        'id_usuario': e.id_usuario,
        'info': usuarioI_to_json(e.info)
    }


def json_to_usuario(d: dict[str, object]) -> Usuarios:
    return Usuarios(

        id_usuario=d.get('id', None),
        nick=d['nick'],
        password=d['password'],
        info= json_to_usuarioI(d['info'])
       
    )
