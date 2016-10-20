from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Localidad, Parada, Sucursal, Telefono


class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = ('nombre', 'tipo', 'departamento',)


class ParadaForm(ModelForm):
    class Meta:
        model = Parada
        fields = ('direccion', 'localidad',)



# class SucursalForm(ModelForm):
#     class Meta:
#         model = Sucursal
#         fields = ('direccion', 'pisos', 'localidad',)  # y telefonos? con formset


SucursalFormSet = inlineformset_factory(Sucursal, Telefono, extra=1)
