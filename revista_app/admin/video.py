from django.contrib import admin

from revista_app.models.video import Video


class VideoAdmin(admin.ModelAdmin):
    model = Video
    fields = ('pagina', 'titulo', 'subtitulo', 'autor', 'imagen', 'clase', 'contenido', 'direccion')
    list_display = ('titulo', 'autor',)
    ordering = ('titulo',)


admin.site.register(Video, VideoAdmin)
