from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    telefono=models.CharField(max_length=15)

class Articulo(models.Model):
    nombre=models.CharField(max_length=30,unique=True)
    seccion=models.CharField(max_length=30)
    precio=models.IntegerField()

class Pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

class Seccion(models.Model):
    nombre=models.CharField(max_length=15,unique=True)