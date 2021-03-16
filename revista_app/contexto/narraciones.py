from itertools import islice

from revista_app.models.narracion import Narracion


def contexto_lista_narraciones():
    arr_art = []
    try:
        narraciones = Narracion.objects.order_by("orden").select_related('pagina').all()
        for n in narraciones:
            arr_art.append({'narracion': n})
        temp = iter(arr_art)
        split_list = [3, 3, 3]
        res = []
        for ele in split_list:
            res.append(list(islice(temp, 0, ele)))
    except Narracion.DoesNotExist:
        raise Exception('no hay narraciones')
    return {"narraciones": res}
