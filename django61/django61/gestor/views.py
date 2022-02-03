from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect,HttpResponse
from gestor.models import *
from django.contrib import messages
import datetime

def articuloAdd(request):
    nombre=request.GET['nombre']
    seccion=request.GET['seccion']
    precio=request.GET['precio']

    if len(nombre)>=30:
        messages.error(request, 'La longitud del elmento es mayor a 30 caracteres')
    else:
        art1 = Articulo.objects.create(nombre=nombre,seccion=seccion,precio=precio)
        messages.success(request, 'Elemento almacenado con exito')
    return HttpResponseRedirect('/articulo')

def articulos (request):
    fechaActual = datetime.datetime.now()
    secciones = []
    articulo = Articulo.objects.all()
    diccionario = {
        'fecha':fechaActual,
        'model':'articulos',
        'header':'Articulos',
        'articulo':articulo.values(),
        'seccion':secciones
    }
    return render(request,'Articulo.html',diccionario)
    # # tpl = loader.get_template('addArticulo.html')
    # docu = tpl.render(diccionario)
    # return HttpResponse(docu)

def valid(nombre,direccion,email,telefono,password,passwordRep):
    errorDict = {}

    # Nombre
    if len(nombre)>30 or len(nombre)<3:
        errorDict['enombre']='El nombre no cumple con una logitud valida'
    # direccion
    
    # email
    if len(email)==0:
        errorDict['eemail']='Debe ingresar un correo'

    emailBase = Cliente.objects.filter(email=email)
    if not len(emailBase)==0:
        errorDict['eemail']='Correo electronico no esta disponible'
    
    # telefono
    if not(len(telefono)==10):
        errorDict['etelefono']='Debe tener 10 digitos'
    for i in telefono:
        if ord(i) < 48 or ord(i) > 58:
            errorDict['etelefono']='El telefono no puede contener letras ni caracateres'
            break
    
    # password
    if len(password)>20 or len(password)<8:
        errorDict['epassword']='La contraseña debe ser mayor a 8 y menor a 20 caracteres'
    # passwordRep
    if len(passwordRep)>20 or len(passwordRep)<8:
        errorDict['epasswordRep']='La contraseña debe ser mayor a 8 y menor a 20 caracteres'
    if not password==passwordRep:
        errorDict['epasswordRep']='Las contraseñas no coinciden'
    return errorDict

def clientes(request):
    fechaActual = datetime.datetime.now()
    clientes = Cliente.objects.all()
    diccionario = {
        'fecha':fechaActual,
        'model':'clientes',
        'header':'Clientes',
        # 'theme':'Quartz',
        # 'theme':'Sketchy',
        'clientes':clientes.values()
    }
    return render(request,'Cliente.html',diccionario)

def clientesAdd(req):
    
    # crea las variables con la data del formulario
    nombre=req.POST['nombre']
    direccion=req.POST['direccion']
    email=req.POST['email']
    telefono=req.POST['telefono']
    password=req.POST['password']
    passwordRep=req.POST['passwordRep']
    
    # ejecuta funcion de validacion y retora un diccionario con los errores
    status=valid(nombre,direccion,email,telefono,password,passwordRep)
    
    if len(status)>0:
        # Si hay errores envia mensaje y 
        diccionario = {'status':status,
            'cliente':{'nombre':nombre,'direccion':direccion,'email':email,'telefono':telefono,'password':password}
        }
        messages.error(req, 'Error en formularios de registro')
        return render(req,'Cliente.html',diccionario)
    else:
        cliente = Cliente.objects.create(nombre=nombre,direccion=direccion,email=email,telefono=telefono,password=password)
        messages.success(req, 'Cliente registrado con exito')        
        return HttpResponseRedirect('/gestor/clientes')
