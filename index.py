#Este es el archivo principal de nuestro proyecto

#Variables {int,str,bool,list}
#funciones {propias,python}
#bucles {while,for}

def detailVar(var:any):
    print("El valor es :",var)
    print("Es de tipo :",type(var))
    print("Su longitud es :",len(var))

def isLogin(user)->bool:
    login = None
    if user=="Login":
        login = True
        print("Usuario esta logueado")
    else:
        login = False
        print("Usuario no esta logueado, Chao")
        exit()
    return login

isLogin('Login')
#----------------------------------------------------------------------------
print('Corriendo la app')

