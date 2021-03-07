from django.views.generic import TemplateView

from revista_app.contexto import contexto_opciones
from revista_app.contexto import contexto_parametros
from revista_app.contexto import contexto_social


class ViewBase(TemplateView):
    nombre_clase = ''
    secciones = []
    template_name = 'pagina.html'
    view_name = ''

    def __init__(self):
        self.pagina = None
        super().__init__()

    def get_context_data(self, **kwargs):
        context = {'vista': self.view_name}
        context.update(contexto_parametros())
        context.update(contexto_opciones())
        context.update(contexto_social())
        return context
