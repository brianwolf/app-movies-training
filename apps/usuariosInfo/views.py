import json

from django.http import HttpResponse, JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from usuariosInfo import dto, service


class Root(APIView):

    @swagger_auto_schema(tags=['usuariosInfo'])
    def get(self, _):
        return JsonResponse(service.list(), safe=False)

    @swagger_auto_schema(tags=['usuariosInfo'])
    def post(self, request):
        body = json.loads(request.body)
        id = service.save(dto.json_to_usuarioI(body))
        return JsonResponse({'id': id}, status=201)


class ById(APIView):

    @swagger_auto_schema(tags=['usuariosInfo'])
    def get(self, _, id):
        usuario_info = service.get(id)
        if not usuario_info:
            return HttpResponse(status=204)
        return JsonResponse(dto.usuarioI_to_json(usuario_info))

    @swagger_auto_schema(tags=['usuariosInfo'])
    def delete(self, _, id):
        service.delete(id)
        return HttpResponse(status=204)
