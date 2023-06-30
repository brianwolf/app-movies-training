import json

from django.http import HttpResponse, JsonResponse
from usuarios import dto, service
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

class Root(APIView):

    @swagger_auto_schema(tags=['usuarios'])
    def get(self, _):
        return JsonResponse(service.list(), safe=False)

    @swagger_auto_schema(tags=['usuarios'])
    def post(self, request):
        body = json.loads(request.body)
        _id = service.save(dto.json_to_usuario(body))
        return JsonResponse({'id': _id}, status=201)


class ById(APIView):

    @swagger_auto_schema(tags=['usuarios'])
    def get(self, _, id):
        usuarios = service.get(id)
        if not usuarios:
            return HttpResponse(status=204)
        return JsonResponse(dto.usuario_to_json(usuarios))

    @swagger_auto_schema(tags=['usuarios'])
    def delete(self, _, id):
        service.delete(id)
        return HttpResponse(status=204)