from itertools import islice

from revista_app.models.narracion import Narracion
from revista_app.models.texto import Texto
from revista_app.views.narracion_view import NarracionView
from revista_app.views.view_base import ViewBase


class IndexView(ViewBase):
    view_name = 'Inicio'
    template_name = 'narraciones.html'

    def get_context_data(self, **kwargs):
        self.pagina = ''
        super().get_context_data(**kwargs)
        self.lista_narraciones()
        self.lista_textos()
        return self.context

    def lista_narraciones(self):
        arr_art = []
        try:
            narraciones = Narracion.objects.order_by('orden').select_related('pagina').all()
            for n in narraciones:
                arr_art.append({'narracion': n})
            temp = iter(arr_art)
            split_list = [3, 3, 3]
            res = []
            for ele in split_list:
                res.append(list(islice(temp, 0, ele)))
            self.context.update({"narraciones": res, 'prefijo_url': NarracionView.prefijo_url})
        except Narracion.DoesNotExist:
            raise Exception('no hay narraciones')

    def lista_textos(self):
        arr_text = []
        textos = Texto.objects.order_by('orden').all()
        for t in textos:
            arr_text.append({'texto': t})
        self.context.update({'textos': arr_text})
