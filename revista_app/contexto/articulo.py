from revista_app.models.articulo import Articulo


def contexto_articulo(articulo):
    try:
        art = Articulo.objects.get(pagina__direccion=articulo)
    except Articulo.DoesNotExist:
        raise Exception('no hay artículo %s' % articulo)
    return {'articulo': art}
