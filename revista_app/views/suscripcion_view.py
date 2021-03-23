from django.views.generic import TemplateView
import json
from revista_app.models import Suscripcion

from django.http import HttpResponse


class SuscripcionView(TemplateView):

    @staticmethod
    def post(request):
        bytess = request.body
        my_json = bytess.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        susc = Suscripcion()
        susc.email = data['email']
        susc.save()
        respuesta = {'resultado': 'Correo registrado existosamente'}
        return HttpResponse(json.dumps(respuesta), content_type='application/json')
