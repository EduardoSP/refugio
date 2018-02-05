from django.conf.urls import url
from apps.adopcion.views import index_adopcion

app_name='adopcion'
urlpatterns = [
    url(r'^index$', index_adopcion, name='home')
]