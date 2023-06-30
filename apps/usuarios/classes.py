from dataclasses import dataclass, field
from usuariosInfo.classes import UsuariosInfo


@dataclass
class Usuarios:
    id_usuario: int
    nick: str 
    password: str
    info: UsuariosInfo 

    def __eq__(self, __o: object) -> bool:
        return self.id_usuario == __o.id_usuario
    

