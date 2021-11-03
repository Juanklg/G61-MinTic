from django.urls import path
from gestor.views import *

urlpatterns = [
    # rutas agregadas para creacion de articulos
    path('', articulo),
    path('add/', addArticulo)
    # path('update/', addArticulo)
    # path('delete/', addArticulo)
]
     
    