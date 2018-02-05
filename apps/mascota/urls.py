from django.conf.urls import url
from apps.mascota.views import index

app_name='mascota'
urlpatterns = [
    url(r'^$', index, name='home'), #^(significa donde inicia la cadena) y #$ (significa donde termina la cadena)
]