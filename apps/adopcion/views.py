from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import PersonaForm, SolicitudForm
# Create your views here.

def index_adopcion(request):
    return HttpResponse("Soy la pagina principal de la app adopcion")

class SolicitudList(ListView):
    model           = Solicitud
    template_name   = 'adopcion/solicitud_list.html'

class SolicitudCreate(CreateView):
    #create para dos formularios
    model               = Solicitud
    template_name       = 'adopcion/solicitud_form.html'
    form_class          =  SolicitudForm
    second_form_class   = PersonaForm
    success_url         = reverse_lazy('adopcion:solicitud_listar')

    def get_context_data(self, **kwargs):
        #sobreescribo el metodo para agregar los dos formularios en el contexto
        context =super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            #si el form no esta en el contexto se lo asignamos
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
        
    #para que los dos formularios se guarden y se cree la relacion
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        #recojo la informacion de los formularios
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud           = form.save(commit=False)  #No guarde hasta que se guarde el segundo formulario
            solicitud.persona   = form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            #si no es valido devuelvo el contexto
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class SolicitudUpdate(UpdateView):
    #update para dos formularios
    model               = Solicitud
    second_model        = Persona
    template_name       = 'adopcion/solicitud_form.html'
    form_class          = SolicitudForm
    second_form_class   = PersonaForm
    success_url         = reverse_lazy('adopcion:solicitud_listar')

    def get_context_data(self, **kwargs):
        context         =   super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk              =   self.kwargs.get('pk',0)
        solicitud       = self.model.objects.get(id=pk)
        persona         = self.second_model.objects.get(id=solicitud.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2']    = self.second_form_class(instance=persona)
        context['id']           = pk
        return context
    
    def post(self, request, *args, **kwargs):
        self.object     = self.get_object
        id_solicitud    = kwargs['pk']
        solicitud       = self.model.objects.get(id=id_solicitud)
        persona         = self.second_model.objects.get(id= solicitud.persona_id)
        form            = self.form_class(request.POST, instance=solicitud)
        form2           = self.second_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class SolicitudDelete(DeleteView):
    model           = Solicitud
    template_name   = 'adopcion/solicitud_delete.html'
    success_url     = reverse_lazy('adopcion:solicitud_listar')
            

        


