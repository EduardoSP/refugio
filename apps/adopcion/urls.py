from django.conf.urls import url
from apps.adopcion.views import index_adopcion, SolicitudList

app_name='adopcion'
urlpatterns = [
    url(r'^index$', index_adopcion, name='home'),
    url(r'^solicitud/listar$', SolicitudList.as_view(), name='solicitud_listar')
]