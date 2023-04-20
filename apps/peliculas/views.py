import json

from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from peliculas import dto, service


class Proxy(APIView):
    def get(self, request, id=None):
        if id is None:
            return JsonResponse(service.list(), safe=False)

        movie = service.get(id)
        if not movie:
            return HttpResponse(status=204)
        return JsonResponse(dto.pelicula_a_json(movie))

    def post(self, request):
        body = json.loads(request.body)
        id = service.save(dto.json_a_pelicula(body))
        return JsonResponse({"id": id}, status=201)

    def delete(self, request, id):
        service.delete(id)
        return HttpResponse(status=204)
