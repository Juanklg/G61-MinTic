from django.contrib import admin
from django.urls import path,include
from django61.views import *

urlpatterns = [
    path('', saludar),
    path('admin/', admin.site.urls),
    
    path('fecha/', fecha),

    path('calculo/<int:fechaNacimiento>/<int:FechaFutura>/',calculo),
    
    path('tasklist/', taskList),
    path('videos/', videos),
    path('articulo/', include('gestor.urls')),
]