from revista_app.models.narracion import Narracion
from .view_base import ViewBase


class NarracionView(ViewBase):
    nombre_clase = 'articulo'
    view_name = 'narracion'
    template_name = 'narracion.html'
    prefijo_url = 'narracion'

    def get_context_data(self, **kwargs):
        s = super(NarracionView, self)
        context = s.get_context_data(**kwargs)
        self.contexto_narracion(kwargs['narracion'], context)
        return context

    @staticmethod
    def contexto_narracion(narracion, context):
        try:
            art = Narracion.objects.get(pagina__direccion=narracion)
            context.update({'narracion': art})
        except Narracion.DoesNotExist:
            raise Exception('no hay narración %s' % narracion)
        context.update({'narracion': art})
