import json

from django.http import HttpResponse, JsonResponse
from usuarios import dto, service
from rest_framework.views import APIView
#esto no toco
class Proxy(APIView):

    def get(self, request, id=None):
        if id == None:
            return JsonResponse(service.list(), safe=False)

        usuarios = service.get(id)
        if not usuarios:
            return HttpResponse(status=204)
        return JsonResponse(dto.usuarioI_to_json(usuarios))

    def post(self, request):
        body = json.loads(request.body)
        id = service.save(dto.json_to_usuarioI(body))
        return JsonResponse({'id': id}, status=201)

    def delete(self, request, id):
        service.delete(id)
        return HttpResponse(status=204)
