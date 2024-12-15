from django.urls import path
from . import views
from .api import api

urlpatterns = [
    path('', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('productos/', views.productos, name='productos'),
    path('productos/registro/', views.registro, name='registro'),
    path('productos/resultado/', views.resultado, name='resultado'),
    path('productos/editar/<int:codigo>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:codigo>/', views.eliminar_producto, name='eliminar_producto'),
    path('api/', api.urls)
]
