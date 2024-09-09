from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos/consulta.html')

def registro(request):
    return render(request, 'productos/registro.html')

def resultado(request):
    return render(request, 'productos/resultado.html')
