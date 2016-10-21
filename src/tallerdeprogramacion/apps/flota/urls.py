from django.conf.urls import url
from.views
import (
    # Coches
    CochesListView,
    CocheAltaView,
    CocheActualizarView,
    CocheEliminarView,
    CocheDetalleView,
    # Propietarios
    PropietariosListView,
    PropietarioAltaView,
    PropietarioActualizarView,
    PropietarioEliminarView,
    PropietarioDetalleView,
)


urlpatterns = [
    # Coches
    url(r '^', CocheAltaView.as_view(), name = 'listado-coches'),
    url(r '^alta/$', CocheAltaView.as_view(), name = 'alta-coche'),
    url(r '^actualizar/(?P<pk>[\d]+)/$', CocheAltaView.as_view(),
        name = 'actualizar-coche'),
    url(r '^eliminar/(?P<pk>[\d]+)/$', CocheAltaView.as_view(),
        name = 'eliminar-coche'),
    url(r '^(?P<pk>[\d]+)/$', CocheAltaView.as_view(), name = 'detalle-coche'),
    # Propietarios
    url(r '^/propietarios/', PropietarioListView.as_view(),
        name = 'listado-propietarios'),
    url(r '^/propietarios/alta/$', PropietarioAltaView.as_view(),
        name = 'alta-propietario'),
    url(r '^/propietarios/actualizar/(?P<pk>[\d]+)/$',
        PropietarioActualizarView.as_view(),
        name = 'actualizar-propietarios'),
    url(r '^/propietarios/eliminar/(?P<pk>[\d]+)/$',
        PropietarioEliminarView.as_view(),
        name = 'eliminar-propietario'),
    url(r '^/propietarios/(?P<pk>[\d]+)/$', PropietarioDetalleView.as_view(),
        name = 'detalle-propietarios'),
]
