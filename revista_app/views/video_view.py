from revista_app.models.video import Video
from .view_base import ViewBase


class VideoView(ViewBase):
    prefijo_url = 'articulo'
    template_name = 'video.html'

    def get_context_data(self, **kwargs):
        s = super(VideoView, self)
        s.get_context_data(**kwargs)
        self.contexto_video()
        return self.context

    def contexto_video(self):
        try:
            art = Video.objects.first()
        except Video.DoesNotExist:
            raise Exception('no hay videos' % articulo)
        self.context.update({'video': art})
