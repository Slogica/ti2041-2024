from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Productos, Categoria, Marca
from .forms import ProductosForm

productos_registrados = []
# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('resultado')
        else:
            error = "Todos los campos son requeridos."
            return render(request, 'productos/registro.html', {'form': form,'error': error})
    
    else:
        form = ProductosForm()
        
    return render(request, 'productos/registro.html', {'form': form})

def editar_producto(request, codigo):
    producto = get_object_or_404(Productos, codigo=codigo)

    if request.method == 'POST':
        form = ProductosForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
        else:
            form = ProductosForm(instance=producto)
    
    else:
        form = ProductosForm(instance=producto)
        
    return render(request, 'productos/editar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, codigo):
    producto = get_object_or_404(Productos, codigo=codigo)

    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    
    return render(request, 'productos/eliminar.html', {'producto': producto})

def resultado(request):
    ultimo_producto = Productos.objects.latest('codigo')
    return render(request, 'productos/resultado.html', {'productos': ultimo_producto})

def productos(request):
    # Obtener todos los productos registrados
    productos_registrados = Productos.objects.all()

    # Filtrar por tamaño
    tamaño = request.GET.get('tamaño')
    if tamaño:
        productos_registrados = productos_registrados.filter(tamaño=tamaño)

    # Filtrar por categoria
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        productos_registrados = productos_registrados.filter(categoria_id=categoria_id)
    
    # Filtrar por marca
    marca_id = request.GET.get('marca')
    if marca_id:
        productos_registrados = productos_registrados.filter(marca_id=marca_id)

    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()

    context = {
        'productos': productos_registrados,
        'categorias': categorias,
        'marcas': marcas,
        'filtros': {
            'tamaño': tamaño,
            'categoria': categoria_id,
            'marca': marca_id,
        }
    }
    return render(request, 'productos/consulta.html', context)