from revista_app.models.parametro import Parametro


def contexto_parametros():
    try:
        param = Parametro.objects.first()
    except Parametro.DoesNotExist:
        raise Exception('no hay registro de parámetros')
    return {'parametros': param}
