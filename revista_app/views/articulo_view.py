from revista_app.models.articulo import Articulo
from .view_base import ViewBase


class ArticuloView(ViewBase):
    nombre_clase = 'articulo'
    view_name = 'articulo'
    template_name = 'articulo.html'
    prefijo_url = 'articulo'

    def get_context_data(self, **kwargs):
        s = super(ArticuloView, self)
        context = s.get_context_data(**kwargs)
        self.contexto_articulo(kwargs['articulo'], context)
        return context

    @staticmethod
    def contexto_articulo(articulo, context):
        try:
            art = Articulo.objects.get(pagina__direccion=articulo)
            context.update({'articulo': art})
        except Articulo.DoesNotExist:
            raise Exception('no hay narración %s' % articulo)
        context.update({'articulo': art})
