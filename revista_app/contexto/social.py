from revista_app.models.social import Social


def contexto_social():
    arr_soc = []
    try:
        social = Social.objects.order_by("orden").all()
        for s in social:
            arr_soc.append(s)
    except Social.DoesNotExist:
        raise Exception('no hay social')
    return {"social": arr_soc}
