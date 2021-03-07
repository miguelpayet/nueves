from itertools import islice

from revista_app.models.articulo import Articulo


def contexto_lista_articulos():
    arr_art = []
    try:
        articulos = Articulo.objects.order_by("orden").select_related('pagina').all()
        for a in articulos:
            arr_art.append({'articulo': a})
        temp = iter(arr_art)
        split_list = [3, 3, 3]
        res = [list(islice(temp, 0, ele)) for ele in split_list]
    except Articulo.DoesNotExist:
        raise Exception('no hay artículos')
    return {"articulos": res}
