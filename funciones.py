#Este es el archivo principal de nuestro proyecto

#Variables {int,float,str,bool}
#iterables o colecciones = {dict,list,tuple,set,range}
#funciones {propias,python,class}
#bucles o sentencias de control = {if,while,for}


def detailVar(var:any):
    print("El valor es :",var)
    print("Es de tipo :",type(var))
    print("Su longitud es :",len(var))
    print("-----------------------------")

def printDict(dc):
    for termino, valor in dc.items():
        print(termino, valor)
    else: print('----------------------------')

def detailArch(el):
    print('---------------------------------')
    print(el)
    print("len = ",len(el))
    for i,e in zip(range(len(el)),el):
        print(f"Pos : {i} - Elemento : {e}")

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