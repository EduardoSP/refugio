from django import forms
from apps.adopcion.models import Persona, Solicitud


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona #indica de que modelo va a crear el formulario
        
        fields = [
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]
        labels = {
            'nombre'            : 'Nombre',
            'apellidos'         : 'Apellidos',
            'edad'              : 'Edad',
            'telefono'          : 'Telefono',
            'email'             : 'Correo electrónico',
            'domicilio'         : 'Domicilio'
        }
        widgest = {
            'nombre'            : forms.TextInput(attrs={'class':'form-control'}),#clase de bootstrap
            'apellidos'         : forms.TextInput(attrs={'class':'form-control'}),
            'edad'              : forms.TextInput(attrs={'class':'form-control'}),
            'telefono'          : forms.TextInput(attrs={'class':'form-control'}),
            'email'             : forms.TextInput(attrs={'class':'form-control'}),
            'domicilio'         : forms.Textarea(attrs={'class' :'form-control'}),

        } 

class SolicitudForm(forms.ModelForm):
    class Meta:
        model   = Solicitud
        fields  = [
            'numero_mascotas',
            'razones',
        ]
        labels = {
            'numero_mascotas'   : 'Numero de mascotas',
            'razones'           : 'Razones para adoptar'
        }
        widgest = {
            'numero_mascotas'   : forms.TextInput(attrs={'class':'form-control'}),
            'razones'           : forms.Textarea(attrs={'class': 'form-control'})
        }