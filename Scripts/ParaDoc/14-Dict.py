def detailVar(var:any):    
    print("El valor es :",var)
    print("Es de tipo :",type(var))
    print("Su longitud es :",len(var))
    print("-----------------------------")

# dict
#se puede definir
usuario={}
car=dict()

diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}

#acceder a un elemento
print(diccionario['IDE'])
print(diccionario.get('OOP'))
#actualizar un elemento con la llave o el key
diccionario['IDE']='integrated development environment'
#Puedo ver las caracteristicas de la variable diccionario
detailVar(diccionario)
#recorrer los elementos de un diccionario
print(diccionario.items())

elementos = []
for key, valor in diccionario.items():
    elementos.append((key, valor))
else: print('----------------------------')
print(elementos)
for elemento in elementos:
    print(elemento)
elementos.sort(reverse=True)
print('----------------------------')
for elemento in elementos:
    print(elemento)

for termino in diccionario.keys():
    print(termino)
else: print('----------------------------')

for valor in diccionario.values():
    print(valor)
else: print('----------------------------')

#valiar si contiene una llave especifica return true o false
print('IDE' in diccionario)

# agregar un elemento al diccionario
diccionario['PK'] = 'Primary Key'
diccionario.update(API='Application Programming Interface')
print(diccionario)

#usar funciones de la clase
#optener las funciones de la clase
# print(dir(diccionario))

#esta e sla lista de funciones de el elemento diccionario capturadas con la funcion 'Dir'
# 'copy', 'fromkeys', 'popitem', 'setdefault'

# remover un elemento del diccionario por la key
diccionario.pop('DBMS')
print(diccionario)

# limpiar -> 'clear',borra todo el contenido del diccionario
diccionario.clear()
print(diccionario)

# eliminar el diccionario
del diccionario
print(diccionario)