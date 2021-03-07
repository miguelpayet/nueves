from django.contrib import admin

from revista_app.models.social import Social


class SocialAdmin(admin.ModelAdmin):
    model = Social
    fields = ('nombre', 'direccion', 'imagen', 'texto', 'orden')
    list_display = ('idsocial', 'orden', 'nombre')
    ordering = ('orden',)


admin.site.register(Social, SocialAdmin)
