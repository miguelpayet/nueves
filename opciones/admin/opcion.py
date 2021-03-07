import nested_admin
from django.contrib import admin

from opciones.models import Opcion


class OpcionAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    fields = ('pagina', 'nombre', 'tipo', 'posicion', 'padre', 'titulo')
    model = Opcion
    list_display = ('nombre', 'titulo', 'posicion', 'tipo',)
    ordering = ('tipo', 'posicion',)


admin.site.register(Opcion, OpcionAdmin)
