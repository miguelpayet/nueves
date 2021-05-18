from django.contrib import admin

from revista_app.models.texto import Texto


class TextoAdmin(admin.ModelAdmin):
    fields = ('contenido', 'imagen', 'orden', 'texto_url', 'titulo', 'url',)
    list_display = ('orden', 'titulo')
    ordering = ('orden',)


admin.site.register(Texto, TextoAdmin)
