from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,\
    DetailView

from .models import Coche, Propietario, ProporcionAsientos


###############################################################################
##                              Propietarios                                 ##
###############################################################################
class PropietariosListView(ListView):
    model = Propietario
    paginate_by = 10
    context_object_name = 'col_propietarios'
    template_name = 'flota/propietarios/listado.html'


class PropietarioDetalleView(DetailView):
    pass


class PropietarioAltaView(CreateView):
    pass


class PropietarioActualizarView(UpdateView):
    pass


class PropietarioEliminarView(DeleteView):
    pass


###############################################################################
##                               Los Coches                                  ##
###############################################################################
class CochesListView(ListView):
    model = Propietario
    paginate_by = 10
    context_object_name = 'col_coches'
    template_name = 'flota/listado.html'


class CocheDetalleView(DetailView):
    pass


class CocheAltaView(CreateView):
    pass


class CocheActualizarView(UpdateView):
    pass


class CocheEliminarView(DeleteView):
    pass
