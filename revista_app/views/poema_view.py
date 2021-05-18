from itertools import islice

from revista_app.models.poema import Poema
from revista_app.views.view_base import ViewBase


class PoemasView(ViewBase):
    view_name = 'Poema'
    template_name = 'poemas.html'

    def get_context_data(self, **kwargs):
        self.pagina = ''
        super().get_context_data(**kwargs)
        self.lista_poemas()
        return self.context

    def lista_poemas(self):
        arr_poemas = []
        try:
            poemas = Poema.objects.order_by("orden").all()
            for p in poemas:
                arr_poemas.append({'poema': p})
            self.context.update({"poemas": arr_poemas, 'prefijo_url': Poema.prefijo_url})
        except Poema.DoesNotExist:
            raise Exception('no hay narraciones')
