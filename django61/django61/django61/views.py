from os import read
from django.http import HttpResponse
import datetime
from django.template import loader,Template,Context

def calculo(request,fechaNacimiento,FechaFutura):
    fechaActual = datetime.datetime.now().year
    edadActual = fechaActual-fechaNacimiento
    edadFutura = FechaFutura-fechaNacimiento
    docu = f'''
        <h1>Mi edad es {edadActual}</h1>
        <h1>En el {FechaFutura} voy a tener una edad de {edadFutura}</h1>
    '''
    return HttpResponse(docu)

def saludar(request):
    file = open(r'C:\Users\MakeDream\Desktop\Ruta1\G61-MinTic\templates\layout.html')
    tpl = Template(file.read())
    file.close()
    ctx = Context()
    docu = tpl.render(ctx)
    return HttpResponse(docu)

def fecha(request):
    fechaActual = datetime.datetime.now()
    tpl = loader.get_template('layout.html')
    docu = tpl.render({'fecha':fechaActual})
    return HttpResponse(docu)