from django.conf.urls import url
from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
MascotaList, MascotaCreate

app_name='mascota'
urlpatterns = [
    url(r'^$', index, name='index'), #^(significa donde inicia la cadena) y #$ (significa donde termina la cadena)
    url(r'^nuevo$', MascotaCreate.as_view(), name='mascota_crear'),
    url(r'^listar$', MascotaList.as_view(), name='mascota_listar'),
    url(r'^editar/(?P<id_mascota>\d+)$', mascota_edit, name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)$', mascota_delete, name='mascota_eliminar'),
]