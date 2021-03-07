from revista_app.contexto.articulo import contexto_articulo
from .view_base import ViewBase


class ArticuloView(ViewBase):
    nombre_clase = 'articulo'
    view_name = 'articulo'
    template_name = 'articulo.html'

    def get_context_data(self, **kwargs):
        s = super(ArticuloView, self)
        context = s.get_context_data(**kwargs)
        context.update(contexto_articulo(kwargs['articulo']))
        return context
