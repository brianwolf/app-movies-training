"""
Archivo donde se definen las clases para la CAPA DE NEGOCIOS

CAPA PRESENTACION<--dto.py-->CAPA NEGOCIO<--repository.py-->CAPA DE DATOS
     (jsons)                  clases.py                       models.py
                              (clases)                        (entities)
"""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Genero:
    nombre: str
    id: int = None

    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id


@dataclass
class Pelicula:
    nombre: str
    puntuacion: float
    fecha_estreno: datetime = field(default=datetime.now())
    generos: list[Genero] = field(default_factory=list)
    id: int = None

    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id
