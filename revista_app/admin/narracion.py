from django.contrib import admin

from revista_app.models.narracion import Narracion


class NarracionAdmin(admin.ModelAdmin):
    model = Narracion
    fields = ('orden', 'pagina', 'titulo', 'contenido', 'autor', 'biografia', 'caratula', 'imagen', 'foto', 'clase')
    list_display = ('idnarracion', 'orden', 'titulo', 'autor', 'caratula')
    ordering = ('orden',)


admin.site.register(Narracion, NarracionAdmin)
