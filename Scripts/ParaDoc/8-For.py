
def informacionDeLaVariable(var):
    print("las longitud es :",len(var),"y su tipo o clase es :",type(var))
    for valor in var:
        # sleep(.5)
        # if valor == 7 : break
        print("Estamos en la iteracion de la variable",valor)
    print("Se termino dentro del else")
    print("Se termino sin else")

def splitText(texto:str):
    listaDePalabras = texto.split(' ')
    return listaDePalabras

#Primer flujo ----------------------------------------------------------

# Login
login = True

print("estado del login",validadorUsuario(login))

text = "Hola compañeros del grupo 61. feliz tarde"
#los typo int no son iterables
number = 15671
# los numeros converdios en str si son iterables
numberToStr = str(56975)
x=range(10)
y=range(5,10)
z=range(0,10,2)

st = splitText(text)
print(st)
informacionDeLaVariable(st)

print(text[-2])

# print(st[5])

informacionDeLaVariable(numberToStr)
informacionDeLaVariable(text)
informacionDeLaVariable(x)
informacionDeLaVariable(y)
informacionDeLaVariable(z)


# -----------------------------------simplificando------------------------
# print(x)
# print(y)
# print(z)

# print("las longitudes son :",len(x),"y su tipo es :",type(x))
# print("las longitudes son :",len(y),"y su tipo es :",type(y))
# print("las longitudes son :",len(z),"y su tipo es :",type(z))

# for valor in x:
#     sleep(.5)
#     print("estamos en la iteracion de x",valor)

# for valor in y:
#     sleep(.5)
#     print("estamos en la iteracion de y",valor)

# for valor in z:
#     sleep(.5)
#     print("estamos en la iteracion de z",valor)
# ------------------------------------------------------------

