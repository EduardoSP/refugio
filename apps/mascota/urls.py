from django.conf.urls import url
from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

app_name='mascota'
urlpatterns = [
    url(r'^$', index, name='index'), #^(significa donde inicia la cadena) y #$ (significa donde termina la cadena)
    url(r'^nuevo$', MascotaCreate.as_view(), name='mascota_crear'),
    url(r'^listar$', MascotaList.as_view(), name='mascota_listar'),
    url(r'^editar/(?P<pk>\d+)$', MascotaUpdate.as_view(), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', MascotaDelete.as_view(), name='mascota_eliminar'),
]