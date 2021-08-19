# Inicio documentacion for
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
def detailVar(var:any):
    print("la var es de tipo : ",type(var))
    print("su valor es : ",var)
    print("su longitud es : ",len(var))
    for valor in var:
        # if valor == 7 : break
        print("Capturamos valor de variable en cada posicion : ",valor)

x=range(10) # de 0 a 9
y=range(5,10) #de 5 a 9
z=range(0,10,2) #salta de 2 en 2
detailVar(x)
detailVar(y)
detailVar(z)
