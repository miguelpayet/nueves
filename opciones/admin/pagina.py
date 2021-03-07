from django.contrib import admin

from opciones.models import Pagina


class PaginaAdmin(admin.ModelAdmin):
    fields = ('titulo', 'nombre', 'direccion', 'descripcion')
    list_display = ('nombre', 'direccion')
    ordering = ('nombre',)


admin.site.register(Pagina, PaginaAdmin)
