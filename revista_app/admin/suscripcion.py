from django.contrib import admin

from revista_app.models.articulo import Articulo

from revista_app.models.suscripcion import Suscripcion


class SuscripcionAdmin(admin.ModelAdmin):
    model = Articulo
    fields = ('email',)
    readonly_fields = ('creacion',)
    list_display = ('email', 'creacion',)
    ordering = ('email',)


admin.site.register(Suscripcion, SuscripcionAdmin)
