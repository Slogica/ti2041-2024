from django.shortcuts import render, redirect
from datetime import datetime

productos_registrados = []
# Create your views here.

def index(request):
    return render(request, 'index.html')

def registro(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        marca = request.POST['marca']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        print(codigo, nombre, marca, fecha_vencimiento)

        if codigo and nombre and marca and fecha_vencimiento:
            try:
                fecha_vencimiento = datetime.strptime(fecha_vencimiento, '%Y-%m-%d')
                producto = {
                    'codigo': codigo,
                    'nombre': nombre,
                    'marca': marca,
                    'fecha_vencimiento': fecha_vencimiento,
                }
                productos_registrados.append(producto)
                return redirect('resultado')
            except ValueError:
                error = "Formato de fecha incorrecto. Use el formato YYYY-MM-DD."
                return render(request, 'productos/registro.html', {'error': error})
        else:
            error = "Todos los campos son requeridos."
            return render(request, 'productos/registro.html', {'error': error})
        
    return render(request, 'productos/registro.html')

def resultado(request):
    return render(request, 'productos/resultado.html', {'productos': productos_registrados[-1]})

def productos(request):
    return render(request, 'productos/consulta.html', {'productos': productos_registrados})