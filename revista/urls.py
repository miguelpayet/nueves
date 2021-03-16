from django.conf import settings
from django.urls import path
from django.urls import re_path
from django.views.static import serve

from revista_app.views import ArticuloView
from revista_app.models.articulo import Articulo
from revista_app.models.narracion import Narracion
from revista_app.views import IndexView
from revista_app.views import NarracionView

url_narracion = ('%s/<str:narracion>/' % Narracion.prefijo_url())
url_articulo = ('%s/<str:articulo>/' % Articulo.prefijo_url())

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path(url_articulo, ArticuloView.as_view()),
    path(url_narracion, NarracionView.as_view()),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]
