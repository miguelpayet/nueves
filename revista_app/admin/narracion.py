from django.contrib import admin

from revista_app.models.narracion import Narracion


class NarracionAdmin(admin.ModelAdmin):
    fields = ('orden', 'pagina', 'titulo', 'contenido', 'autor', 'caratula', 'imagen', 'clase')
    list_display = ('orden', 'titulo', 'autor', 'caratula')
    ordering = ('orden',)


admin.site.register(Narracion, NarracionAdmin)
