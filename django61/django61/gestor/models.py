from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ciudad=models.CharField(max_length=50,blank=False,default="nulo")
    telefono = models.CharField(max_length=20, blank=True)
    web = models.URLField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

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