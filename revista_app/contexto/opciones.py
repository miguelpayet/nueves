from opciones.models.opcion import Opcion


def contexto_opciones():
    arr_opc = []
    try:
        opciones = Opcion.objects.order_by("posicion").select_related('pagina').all()
        for o in opciones:
            arr_opc.append({'posicion': o.posicion, 'titulo': o.titulo, 'direccion': o.pagina.direccion})
    except Opcion.DoesNotExist:
        raise Exception('no hay opciones')
    return {"opciones": arr_opc}
