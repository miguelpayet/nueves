from revista_app.models.articulo import Articulo
from .view_base import ViewBase


class ArticuloView(ViewBase):
    nombre_clase = 'articulo'
    prefijo_url = 'articulo'
    template_name = 'articulo.html'
    view_name = 'articulo'

    def get_context_data(self, **kwargs):
        self.pagina = kwargs['articulo']
        s = super(ArticuloView, self)
        s.get_context_data(**kwargs)
        self.contexto_articulo(kwargs['articulo'])
        return self.context

    def contexto_articulo(self, articulo):
        try:
            art = Articulo.objects.get(pagina__direccion=articulo)
        except Articulo.DoesNotExist:
            raise Exception('no hay narración %s' % articulo)
        self.context.update({'articulo': art})
