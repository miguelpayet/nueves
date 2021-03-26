from revista_app.models.narracion import Narracion
from .view_base import ViewBase


class NarracionView(ViewBase):
    prefijo_url = 'narracion'
    template_name = 'narracion.html'

    def get_context_data(self, **kwargs):
        self.pagina = kwargs["narracion"]
        s = super(NarracionView, self)
        s.get_context_data(**kwargs)
        self.contexto_narracion(kwargs['narracion'])
        return self.context

    def contexto_narracion(self, narracion):
        try:
            art = Narracion.objects.get(pagina__direccion=narracion)
        except Narracion.DoesNotExist:
            raise Exception('no hay narración %s' % narracion)
        self.context.update({'narracion': art})
