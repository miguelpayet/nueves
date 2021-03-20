from django.views.generic import TemplateView
import json
from revista_app.models import Suscripcion


class SuscripcionView(TemplateView):

    def post(self, request):
        bytess = request.body
        my_json = bytess.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        susc = Suscripcion()
        susc.email = data['email']
        susc.save()
