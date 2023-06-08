from dataclasses import dataclass, field
from usuariosInfo.classes import UsuariosInfo


@dataclass
class Usuarios:
    nick: str 
    password: str
    id_usuario: int
    info: UsuariosInfo 

    def __eq__(self, __o: object) -> bool:
        return self.id_usuario == __o.id_usuario
    

