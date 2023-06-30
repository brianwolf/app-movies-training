from django.db import models
from django.utils import timezone

from usuarios.classes import Usuarios
from usuariosInfo.models import UsuariosInfoEntity


class UsuariosEntity(models.Model):

    id_usuario = models.AutoField(primary_key=True)
    nick = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    info = models.OneToOneField(UsuariosInfoEntity, on_delete=models.CASCADE)

    class Meta:
        db_table = 'USUARIOS'

    def to_class(self):
        print(self)
        return Usuarios(
            id_usuario=self.id_usuario,
            nick=self.nick,
            password=self.password,
            info=self.info.to_class(),
        )

    @staticmethod
    def from_class(e: Usuarios) -> 'UsuariosEntity':
        return UsuariosEntity(
            id_usuario=e.id_usuario,
            nick=e.nick,
            password=e.password,
            info=UsuariosInfoEntity.from_class(e.info)
        )
