from django.forms import ModelForm

from .models import Localidad, Parada, Sucursal


class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = ('nombre', 'tipo', 'departamento',)


class ParadaForm(ModelForm):
    class Meta:
        model = Parada
        fields = ('direccion', 'localidad',)



class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = ('direccion', 'pisos', 'localidad',)  # y telefonos? con formset
