from django.contrib import admin

from revista_app.models.poema import Poema


class PoemaAdmin(admin.ModelAdmin):
    fields = ('orden', 'titulo', 'contenido', 'autor', 'imagen', 'clase')
    list_display = ('orden', 'titulo', 'autor')
    ordering = ('orden',)


admin.site.register(Poema, PoemaAdmin)
