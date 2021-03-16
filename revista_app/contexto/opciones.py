from opciones.models.opcion import Opcion


def contexto_opciones():
    arr_opc = []
    try:
        opciones = Opcion.objects.order_by("posicion").select_related('pagina').all()
        for o in opciones:
            prefijo = obtener_clase(o)
            arr_opc.append({'posicion': o.posicion, 'titulo': o.titulo, 'direccion': prefijo + o.pagina.direccion})
    except Opcion.DoesNotExist:
        raise Exception('no hay opciones')
    return {"opciones": arr_opc}


def obtener_clase(opcion):
    prefijo = ''
    if hasattr(opcion.pagina, 'articulo_set'):
        art = opcion.pagina.articulo_set.first()
        if art is not None:
            prefijo = art.prefijo_url()
    # if hasattr(opcion.pagina, 'narracion_set'):
    #    nar = opcion.pagina.narracion_set.first()
    #    if nar is not None:
    #        prefijo = nar.prefijo_url()
    cadena = ('' if prefijo == '' else '/')
    return prefijo + ('' if prefijo == '' else '/')
