from revista_app.models.articulo import Articulo
from .view_base import ViewBase

from revista_app.models import Podcast


class PodcastView(ViewBase):
    prefijo_url = 'podcast'
    template_name = 'podcast.html'

    def get_context_data(self, **kwargs):
        s = super(PodcastView, self)
        s.get_context_data(**kwargs)
        self.contexto_podcast()
        return self.context

    def contexto_podcast(self):
        try:
            art = Podcast.objects.all().first()
        except Articulo.DoesNotExist:
            raise Exception('no hay podcast')
        self.context.update({'articulo': art})
