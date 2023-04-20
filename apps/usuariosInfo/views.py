import json

from django.http import HttpResponse, JsonResponse
from usuariosInfo import dto, service
from rest_framework.views import APIView
#esto no toco
class Proxy(APIView):

    def get(self, request, id=None):
        if id == None:
            return JsonResponse(service.list(), safe=False)

        usuario_info = service.get(id)
        if not usuario_info:
            return HttpResponse(status=204)
        return JsonResponse(dto.usuarioI_to_json(usuario_info))

    def post(self, request):
        body = json.loads(request.body)
        id = service.save(dto.json_to_usuarioI(body))
        return JsonResponse({'id': id}, status=201)

    def delete(self, request, id):
        service.delete(id)
        return HttpResponse(status=204)
