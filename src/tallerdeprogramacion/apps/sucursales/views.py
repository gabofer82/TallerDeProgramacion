from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,\
    DetailView

from .models import Departamento, Localidad, Parada, Sucursal, Telefono

###############################################################################
##                             Las Sucursales                                ##
###############################################################################
class SucursalesListView(ListView):
    pass


class SucursalDetalleView(DetailView):
    pass


class SucursalAltaView(CreateView):
    pass


class SucursalActualizarView(UpdateView):
    pass


class SucursalEliminarView(DeleteView):
    pass


###############################################################################
##                               Las Paradas                                 ##
###############################################################################
class ParadasListView(ListView):
    pass


class ParadaDetalleView(DetailView):
    pass
    

class ParadaAltaView(CreateView):
    pass


class ParadaActualizarView(UpdateView):
    pass


class ParadaEliminarView(DeleteView):
    pass
