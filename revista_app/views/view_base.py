from django.views.generic import TemplateView

from revista_app.models.parametro import Parametro
from opciones.models.pagina import Pagina
from opciones.models.opcion import Opcion
from revista_app.models.social import Social


def obtener_clase(opcion):
    prefijo = ''
    if hasattr(opcion.pagina, 'articulo_set'):
        art = opcion.pagina.articulo_set.first()
        if art is not None:
            prefijo = art.prefijo_url()
    return prefijo + ('' if prefijo == '' else '/')


class ViewBase(TemplateView):
    nombre_clase = ''
    secciones = []
    template_name = 'pagina.html'
    view_name = ''

    def __init__(self):
        self.pagina = ''
        super().__init__()
        self.context = {}

    def get_context_data(self, **kwargs):
        self.context.update({'vista': self.view_name})
        self.contexto_parametros()
        self.contexto_opciones()
        self.contexto_pagina()
        self.contexto_social()
        return self.context

    def contexto_pagina(self):
        try:
            pagina = Pagina.objects.get(direccion=self.pagina)
        except Pagina.DoesNotExist:
            raise Exception('no hay registro de página')
        self.context.update({'pagina': pagina})

    def contexto_parametros(self):
        try:
            param = Parametro.objects.first()
        except Parametro.DoesNotExist:
            raise Exception('no hay registro de parámetros')
        self.context.update({'parametros': param})

    def contexto_opciones(self):
        arr_opc = []
        try:
            opciones = Opcion.objects.order_by("posicion").select_related('pagina').all()
            for o in opciones:
                prefijo = obtener_clase(o)
                arr_opc.append({'posicion': o.posicion, 'titulo': o.titulo, 'direccion': prefijo + o.pagina.direccion})
        except Opcion.DoesNotExist:
            raise Exception('no hay opciones')
        self.context.update({"opciones": arr_opc})

    def contexto_social(self):
        arr_soc = []
        try:
            social = Social.objects.order_by("orden").all()
            for s in social:
                arr_soc.append(s)
        except Social.DoesNotExist:
            raise Exception('no hay social')
        self.context.update({"social": arr_soc})
