from os import read
from django.http import HttpResponse
import datetime
from django.template import loader,Template,Context

def calculo(request,fechaNacimiento,FechaFutura):
    añoActual = datetime.datetime.now().year
    edadActual = añoActual-fechaNacimiento
    edadFutura = FechaFutura-fechaNacimiento
    diccionario = {
        'nombre':'Pagina de calculo',
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