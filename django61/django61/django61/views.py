# django
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.contrib import messages
# python
import datetime
# django forms
from django61.forms import UserRegisterForm
# django auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate

def usuarioAdd(req):
    if req.method == 'POST':
        form=UserRegisterForm(req.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            messages.success(req, f'Cliente {username} fue registrado con exito')
        else:
            messages.error(req, f'Hay errores en el formulario de registro')
    else:
        form=UserRegisterForm()
    diccionario = {
        'fecha':datetime.datetime.now(),
        'model':'usuarios',
        'header':'Usuarios',
        'form':form
    }
    return render(req,'Usuario.html',diccionario)

def usuarioLogin(req):
    diccionario = {
        'fecha':datetime.datetime.now(),
        'model':'usuarios',
        'header':'Login',
    }
    if req.method == 'POST':
        form=AuthenticationForm(req,req.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            usuario = authenticate(username=username,password=password)
            if usuario is not None:
                login(req,usuario)
                return redirect('home')
            else:
                messages.success(req, f'Usuario o contraseña incorrectas')
        else:
            messages.error(req, f'Usuario o contraseña incorrectas')
    else:
        form=AuthenticationForm()
    diccionario['form'] = form
    return render(req,'Login.html',diccionario)

def usuarioLogout(req):
    logout(req)
    messages.success(req, f'Vuelve pronto')
    return redirect('login')

# Old Learn django

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
    diccionario = {
        'title':'***Workbook***',
        'header':'Workbook',
        'fecha':datetime.datetime.now(),
    }
    return render(req,'videos.html',diccionario)
    tpl = loader.get_template('videos.html')
    docu = tpl.render(diccionario)
    return HttpResponse(req,docu)

