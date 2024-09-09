from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('productos/registro/', views.registro, name='registro'),
    path('productos/resultado/', views.resultado, name='resultado')
]
