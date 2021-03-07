from django.conf import settings


def admin_media(request):
    return {'MEDIA_URL': settings.MEDIA_URL}
