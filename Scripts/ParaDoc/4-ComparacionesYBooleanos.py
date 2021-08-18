#variables numericas y input(los input's siempre seran de type 'str')
x = int(input("Ingrese x : "))
y = int(input("Ingrese y : "))

print("x es de tipo = ",type(x))
print("y es de tipo = ",type(y))

#Variables type bool q surgen de comparaciones
miBool = x >= y
print(type(miBool))

#algunas delas comparaciones q nos retornan u valor booleano
resultado = x == y # pregunto si son iguales
print(f'Resultado == : {resultado}')

resultado = x != y # pregunto si son diferentes
print(f'Resultado != : {resultado}')

resultado = x > y # pregunto si la primera es mayor q la segunda
print(f'Resultado > : {resultado}')

resultado = x >= y # pregunto si la primera es mayor o igual q la segunda
print(f'Resultado >= : {resultado}')

resultado = x < y # pregunto si la primera es menor la segunda
print(f'Resultado < : {resultado}')

resultado = x <= y # pregunto si la primera es menor o igual q la segunda
print(f'Resultado <= :{resultado}')