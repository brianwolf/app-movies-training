from django.db import models
from django.utils import timezone

from usuarios.classes import Usuarios



class UsuariosEntity(models.Model):
   
    nick = models.CharField(max_length=200) 
    password = models.CharField(max_length=200)
    id_usuario=models.AutoField(primary_key=True)

    class Meta:
        db_table = 'USUARIOS'

    def to_class(self):
        return Usuarios(
            id_usuario= self.id_usuario,
            password=self.password,
            nick=self.nick,
        )

    @staticmethod
    def from_class(e: Usuarios) -> 'UsuariosEntity':
        return UsuariosEntity(
            
            nick=e.nick,
            id_usuarios=e.id_usuario,
            password=e.password
        )
    
 