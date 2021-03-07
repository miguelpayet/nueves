from django.contrib import admin

from revista_app.models.parametro import Parametro


class ParametroAdmin(admin.ModelAdmin):
    model = Parametro
    fields = (
        'logo', 'texto_logo', 'logo_pucp', 'texto_logo_pucp', 'url_pucp', 'logo_maestria', 'texto_logo_maestria', 'url_maestria', 'descripcion',)
    list_display = ('idparametro',)


admin.site.register(Parametro, ParametroAdmin)
