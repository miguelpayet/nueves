from revista_app.models.articulo import Articulo
from .view_base import ViewBase

from revista_app.models import Podcast


class PodcastView(ViewBase):
    nombre_clase = 'podcast'
    view_name = 'podcast'
    template_name = 'podcast.html'
    prefijo_url = 'podcast'

    def get_context_data(self, **kwargs):
        s = super(PodcastView, self)
        context = s.get_context_data(**kwargs)
        self.contexto_articulo(context)
        return context

    @staticmethod
    def contexto_articulo(context):
        try:
            art = Podcast.objects.all().first()
            context.update({'podcast': art})
        except Articulo.DoesNotExist:
            raise Exception('no hay podcast')
        context.update({'articulo': art})
