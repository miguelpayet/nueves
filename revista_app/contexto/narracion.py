from revista_app.models.narracion import Narracion


def contexto_narracion(articulo):
    try:
        art = Narracion.objects.get(pagina__direccion=articulo)
    except Narracion.DoesNotExist:
        raise Exception('no hay artículo %s' % articulo)
    return {'articulo': art}
