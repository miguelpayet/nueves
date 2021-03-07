from django.contrib import admin

from revista_app.models.articulo import Articulo


# class ArticuloImagenInline(nested_admin.NestedTabularInline):
#    extra = 1
#    fields = ('imagen', 'texto',)
#    model = ArticuloImagen


class ArticuloAdmin(admin.ModelAdmin):
    model = Articulo
    # inlines = [ArticuloImagenInline]
    fields = ('orden', 'pagina', 'autor', 'titulo', 'imagen', 'clase', 'contenido')
    list_display = ('idarticulo', 'orden', 'titulo', 'autor')
    ordering = ('orden',)


admin.site.register(Articulo, ArticuloAdmin)
