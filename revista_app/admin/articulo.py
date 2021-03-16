from django.contrib import admin

from revista_app.models.articulo import Articulo


class ArticuloAdmin(admin.ModelAdmin):
    model = Articulo
    fields = ('pagina', 'titulo', 'subtitulo', 'autor', 'imagen', 'clase', 'sumilla', 'contenido')
    list_display = ('titulo', 'autor',)
    ordering = ('titulo',)


admin.site.register(Articulo, ArticuloAdmin)
