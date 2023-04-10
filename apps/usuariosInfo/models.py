from django.db import models
from django.utils import timezone

from usuariosInfo.classes import UsuariosInfo



class UsuariosInfoEntity(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200) 
    apellido = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=timezone.now) 

    class Meta:
        db_table = 'USUARIOS_INFO'

    def to_class(self):
        return UsuariosInfo(
            id=self.id,
            nombre=self.nombre,
            apellido=self.apellido,
            email=self.email,
            fecha=self.fecha,
        )

    @staticmethod
    def from_class(e: UsuariosInfo) -> 'UsuariosInfoEntity':
        return UsuariosInfoEntity(
            id=e.id,
            nombre=e.nombre,
            apellido=e.apellido,
            email=e.email,
            fecha=e.fecha,
        )
    
 