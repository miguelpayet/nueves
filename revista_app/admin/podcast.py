from django.contrib import admin

from revista_app.models import Podcast


class PodcastAdmin(admin.ModelAdmin):
    model = Podcast
    fields = ('titulo', 'link', 'direccion', 'sumilla', 'descripcion')
    list_display = ('idpodcast', 'link')


admin.site.register(Podcast, PodcastAdmin)
