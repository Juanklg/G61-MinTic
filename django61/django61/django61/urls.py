from django.contrib import admin
from django.urls import path,include
from django61.views import *

urlpatterns = [
    path('', videos,name='home'),
    path('admin/', admin.site.urls),
    path('fecha/', fecha),
    path('calculo/<int:fechaNacimiento>/<int:FechaFutura>/',calculo),
    path('tasklist/', taskList),
    path('videos/', videos),
    # login
    path('usuarioAdd/', usuarioAdd,name='signin'),
    path('usuarioLogin/', usuarioLogin, name='login'),
    path('usuarioLogout/', usuarioLogout, name='logout'),
    # gestor
    path('gestor/', include('gestor.urls')),
]