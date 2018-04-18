from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from apps.usuario.views import RegistroUsuario

app_name='usuario'
urlpatterns = [
    url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
]
