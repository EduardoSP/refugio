from django.conf.urls import url
from apps.mascota.views import index, mascota_view, mascota_list

app_name='mascota'
urlpatterns = [
    url(r'^$', index, name='index'), #^(significa donde inicia la cadena) y #$ (significa donde termina la cadena)
    url(r'^nuevo$', mascota_view, name='mascota_crear'),
    url(r'^listar$', mascota_list, name='mascota_listar'),
]