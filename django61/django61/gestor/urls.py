from django.urls import path
from gestor.views import *

urlpatterns = [
    # Articulos
    path('articulos/', articulos),
    path('articuloAdd/', articuloAdd),
    
    path('clientes/', clientes),
    path('clienteAdd/', clientesAdd),
]
