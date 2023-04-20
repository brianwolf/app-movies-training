from django.test import TestCase
from usuariosInfo import service
from usuariosInfo.classes import UsuariosInfo
import json

from core.exception import AppException #que hace esto?


class UsuarioServiceTest(TestCase):
    #esto no toco
    def test_usuario_save_and_get(self):

        id = service.save(UsuariosInfo(
            string='asd',
            integer=12,
            decimal=1.5 #TENGO Q PREGUNTAR A LOBI
        ))

        usuario = service.get(id)
        usuario_none = service.get(123)

        self.assertEqual(usuario.id, id)
        self.assertEqual(usuario_none, None)

    def test_usuario_list(self):

        list_empty = service.list()

        service.save(UsuariosInfo(
            string='asd',
            integer=12,
            decimal=1.5
        ))

        list_not_empty = service.list()

        self.assertEqual(list_empty, [])
        self.assertEqual(len(list_not_empty), 1)

    def test_usuario_delete(self):

        id = service.save(UsuariosInfo(
            string='asd',
            integer=12,
            decimal=1.5
        ))

        service.delete(id)
        list_empty = service.list()

        self.assertEqual(list_empty, [])
        self.assertRaises(AppException, service.delete, 123)


class UsuariosClassTest(TestCase):

    def test_equals_class(self):

        usuario_1 = UsuariosInfo(
            string='asd',
            integer=1,
            decimal=1.5,
            id=1
        )

        usuario_2 = UsuariosInfo(
            string='qwe',
            integer=2,
            decimal=2.5,
            id=1
        )

        self.assertEquals(usuario_1, usuario_2)


class UsuarioViewTest(TestCase):

    def test_list(self):

        response = self.client.get('/api/v1/usuariosInfo/', follow=True)

        self.assertEquals(response.status_code, 200)

    def test_get(self):

        id = service.save(UsuariosInfo(
            string='asd',
            integer=12,
            decimal=1.5
        ))

        response = self.client.get(f'/api/v1/usuariosInfo/{id}', follow=True)
        response_not_exist = self.client.get(
            f'/api/v1/usuariosInfo/123', follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()['id'], id)
        self.assertEquals(response_not_exist.status_code, 204)

    def test_post(self):

        body = {
            'string': 'asd',
            'integer': 12,
            'decimal': 1.5,
            'date': '2020-12-12T12:12:12.000'
        }
        response = self.client.post(
            f'/api/v1/usuariosInfo/', data=body, follow=True, content_type='application/json')

        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.json()['id'], 1)

    def test_delete(self):

        id = service.save(UsuariosInfo(
            string='asd',
            integer=12,
            decimal=1.5
        ))

        response = self.client.delete(f'/api/v1/usuariosInfo/{id}', follow=True)
        response_error = self.client.delete(f'/api/v1/usuariosInfo/123', follow=True)

        self.assertEquals(response.status_code, 204)
        self.assertEquals(response_error.status_code, 409)
