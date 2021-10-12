from django.http import HttpResponse
import datetime

def saludar(request):
    return HttpResponse('Hola Grupo 61 desde django python')

def fecha(request):
    fechaActual = datetime.datetime.now()
    docu='''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <h1>Esto es un titulo generado %s</h1>
        <p>esto es un parrafo</p>
    </body>
    </html>
    ''' % fechaActual
    return HttpResponse(docu)