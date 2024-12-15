from ninja import NinjaAPI, Schema
from django.contrib.auth import authenticate
from django.http import HttpRequest, Http404
from django.shortcuts import get_object_or_404
from pydantic import ValidationError
from .models import Productos
from .utils import generar_token, JWTAuth

api = NinjaAPI(
    title="API de productos",
    description="Aquí están los productos de la tienda",
    version="1.0.0"
)

# Crea el objeto auth
auth = JWTAuth()

# Manejadores de Errores
@api.exception_handler(Http404)
def error_404(request, ex):
    return api.create_response(request, 
                               {'response': 'Recurso no encontrado'},
                               status=404)

@api.exception_handler(ValidationError)
def error_validacion(request, ex):
    return api.create_response(request,
                               {
                                   'response': 'Error de Formato de Entrada',
                                   'errores': ex.errors()
                               },
                               status=422)

# Servicios de la API
class AuthRequest(Schema):
    username: str
    password: str

@api.post(path="/token", tags=["Auth"])
def get_token(request, data: AuthRequest):
    user = authenticate(username=data.username, password=data.password)
    if not user:
        return { "error": "Credenciales inválidas" }
    token = generar_token(user)
    return { "token": token }


@api.get(path="productos/", auth=auth, tags=["Productos"])
def get_productos(request):
    all_posts = Productos.objects.all().values()
    return list(all_posts)

@api.get(path="productos/{productos_codigo}", auth=auth, tags=["Productos"])
def get_producto(request, productos_codigo: int):
    producto = Productos.objects.filter(codigo=productos_codigo).values()
    return list(producto)

class PostSchema(Schema):
    nombre: str
    precio: int
    tamaño: str
    peso: float
    categoria_id: int
    marca_id: int

@api.post(path="productos/", auth=auth, tags=["Productos"])
def add_productos(request, data: PostSchema):
    producto = Productos.objects.create(**data.dict())
    return { "id":producto.codigo, "title":producto.nombre }

@api.put(path="productos/{productos_codigo}", auth=auth, tags=["Productos"])
def update_productos(request, productos_codigo: int, data: PostSchema):
    producto = get_object_or_404(Productos, codigo=productos_codigo)
    for attr, value in data.dict().items():
        setattr(producto, attr, value)
    producto.save()
    return { "id":producto.codigo, "title":producto.nombre }