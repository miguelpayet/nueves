from django.contrib import admin

from revista_app.models.autor import Autor


class AutorAdmin(admin.ModelAdmin):
    model = Autor
    fields = ('biografia', 'foto', 'nombre')
    list_display = ('nombre',)
    ordering = ('nombre',)


admin.site.register(Autor, AutorAdmin)
