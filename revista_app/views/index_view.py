from revista_app.contexto import contexto_lista_articulos
from revista_app.views.view_base import ViewBase


class IndexView(ViewBase):
    nombre_clase = 'inicio'
    view_name = 'Inicio'
    template_name = 'articulos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(contexto_lista_articulos())
        return context
