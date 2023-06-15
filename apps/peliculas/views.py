import json

from django.http import HttpResponse, JsonResponse
from drf_yasg.utils import swagger_auto_schema
from peliculas import dto, service
from rest_framework.views import APIView


class Root(APIView):

    @swagger_auto_schema(tags=['peliculas'])
    def get(self, request, id=None):
        if id is None:
            return JsonResponse(service.list(), safe=False)

    @swagger_auto_schema(tags=['peliculas'])
    def post(self, request):
        body = json.loads(request.body)
        _id = service.save(dto.json_a_pelicula(body))
        return JsonResponse({"id": _id}, status=201)


class ById(APIView):

    @swagger_auto_schema(tags=['peliculas'])
    def get(self, _, id):
        movie = service.get(id)
        if not movie:
            return HttpResponse(status=404)
        return JsonResponse(dto.pelicula_a_json(movie))

    @swagger_auto_schema(tags=['peliculas'])
    def delete(self, _, id):
        service.delete(id)
        return HttpResponse(status=204)
