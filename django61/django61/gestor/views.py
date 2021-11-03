from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from gestor.models import *
from django.contrib import messages
import datetime

def respuesta(request):
    nombre = request.GET['nombre']
    seccion = request.GET['seccion']
    precio = request.GET['precio']
    art1 = articulo.objects.create(nombre=nombre,seccion=seccion,precio=precio)
    if(art1):
        HttpResponse(art1)
    else:
        mensaje = f'Articulo {nombre} ha sido creado en la seccion {seccion} con un precio de {precio}'
        return HttpResponse(mensaje)

def addArticulo(request):
    nombre=request.GET['nombre']
    seccion=request.GET['seccion']
    precio=request.GET['precio']

    if len(nombre)>=30:
        messages.error(request, 'La longitud del elmento es mayor a 30 caracteres')
    else:
        art1 = Articulo.objects.create(nombre=nombre,seccion=seccion,precio=precio)
        messages.success(request, 'Elemento almacenado con exito')
    return HttpResponseRedirect('/articulo')

def articulo (request):
    fechaActual = datetime.datetime.now()
    secciones = []
    articulo = Articulo.objects.all()
    diccionario = {
        'fecha':fechaActual,
        'nombre':'Articulo',
        'title':'***Articulo***',
        # 'theme':'Quartz',
        # 'theme':'Sketchy',
        'articulo':articulo.values(),
        'seccion':secciones
    }
    return render(request,'Articulo.html',diccionario)
    # # tpl = loader.get_template('addArticulo.html')
    # docu = tpl.render(diccionario)
    # return HttpResponse(docu)
