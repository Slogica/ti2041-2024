from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos, name='productos'),
    path('productos/registro/', views.registro, name='registro'),
    path('productos/resultado/', views.resultado, name='resultado'),
    path('productos/editar/<int:codigo>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:codigo>/', views.eliminar_producto, name='eliminar_producto'),
]
