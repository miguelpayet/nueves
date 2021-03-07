from django.conf import settings
from django.urls import path
from django.urls import re_path
from django.views.static import serve

from revista_app.views import IndexView
from revista_app.views import ArticuloView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articulo/<str:articulo>/', ArticuloView.as_view()),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]
