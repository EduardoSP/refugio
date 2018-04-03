from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView

from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import PersonaForm, SolicitudForm
# Create your views here.

def index_adopcion(request):
    return HttpResponse("Soy la pagina principal de la app adopcion")

class SolicitudList(ListView):
    model           = Solicitud
    template_name   = 'adopcion/solicitud_list.html'

class SolicitudCreate(CreateView):
    model               = Solicitud
    template_name       = 'adopcion/solicitud_form.html'
    form_class          =  SolicitudForm
    second_form_class   = PersonaForm
    #success_url         = reverse_lazy('')


