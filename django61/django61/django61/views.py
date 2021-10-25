from django.http import HttpResponse
import datetime
from django.template import loader
from django.shortcuts import render

def respuesta(request):
    nombre = request.GET['nombre']
    mensaje = f'Articulo {nombre} ha sido creado'
    print(mensaje)
    return HttpResponse(mensaje)

def addArticulo (request):
    fechaActual = datetime.datetime.now()
    diccionario = {
        'fecha':fechaActual,
        'nombre':'Articulos',
        'title':'***Articulo***'
    }
    return render(request,'addArticulo.html')  
    # # tpl = loader.get_template('addArticulo.html')
    # docu = tpl.render(diccionario)
    # return HttpResponse(docu)


def calculo(request,fechaNacimiento,FechaFutura):
    fecha = datetime.datetime.now()
    añoActual = fecha.year
    edadActual = añoActual-fechaNacimiento
    edadFutura = FechaFutura-fechaNacimiento
    diccionario = {
        'nombre':'Pagina de calculo',
        'fecha':fecha,
        'actual':añoActual,
        'edadActual':edadActual,
        'edadFutura':edadFutura,
        'fechaNacimiento':fechaNacimiento,
        'FechaFutura':FechaFutura,
    }
    tpl = loader.get_template('calculo.html')
    docu = tpl.render(diccionario)
    return HttpResponse(docu)    

def saludar(request):
    fechaActual = datetime.datetime.now()
    diccionario = {
        'fecha':fechaActual,
        'nombre':'Pagina de Bienvenida',
        'title':'***Welcome***'
    }
    tpl = loader.get_template('layout.html')
    docu = tpl.render(diccionario)
    return HttpResponse(docu)

def fecha(request):
    fechaActual = datetime.datetime.now()
    
    diccionario = {
        'fecha':fechaActual,
        'nombre':'Pagina 1',
    }

    tpl = loader.get_template('layout.html')
    docu = tpl.render(diccionario)
    return HttpResponse(docu)

def taskList(req):
    fechaActual = datetime.datetime.now()
    diccionario = {
        "fecha":fechaActual,
        "nombre":'Lista de tareas',
        "nameList":'Tareas django',
        "tareas":[
            'Crear el html del header',
            'Modularizar el header',
            'Hacer los mimo con el footer',
        ]
    }
    tpl = loader.get_template('tasklist.html')
    docu = tpl.render(diccionario)
    return HttpResponse(docu)

def videos(req):
    fechaActual = datetime.datetime.now()
    diccionario = {
        'title':'***Videos***',
        'nombre':'Videos Youtube',
        'fecha':fechaActual,
    }
    tpl = loader.get_template('videos.html')
    docu = tpl.render(diccionario)
    return HttpResponse(docu)

