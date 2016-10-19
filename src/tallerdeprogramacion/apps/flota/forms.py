from django.forms import ModelForm

from .models import Coche, Propietario


class PopietarioForm(ModelForm):
    class Meta:
        model = Propietario
        fields = ('nombre', 'telefono', 'externo')


class CocheForm(ModelForm):
    class Meta:
        model = Coche
        fields = ('numero', 'marca', 'modelo', 'año', 'capacidad', 'estado',
            'propietario', 'asientos')
