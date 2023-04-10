from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class UsuariosInfo:
    nombre: str 
    apellido: str
    email: str
    fecha: datetime = field(default=datetime.now()) 
    id: int = None
    
    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id
