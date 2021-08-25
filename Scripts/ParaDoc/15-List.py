def printListOTuple(lt):
    for x in lt:
        print(x)
    else: print('----------------------------')

def printListOTupleConIndice(lt):
    for x in range(0,len(lt)):
        print("Valor en pos",x," = ",lt[x])
    else: print('----------------------------')

# list
#Creamos una lista con los nombres de los estudiantes
Lestudiantes = [
    'Andres',
    'Brayan',
    'Jhon',
    'Juan',
    'Karen',
    'Maria',
    'Nicolas',
    'Stuart',
    'Valentina',
    'Juan',
]

#creamos una tupla con las caracteristicas de los estudiantes
# tuple
TPropsEst = (
    'nombre',
    'user',
    'edad',
    'grupo',
    'apellido',
    'nota',
)
# TPropsEst = list(TPropsEst)

# imprimir lista indexada
printListOTupleConIndice(Lestudiantes)
printListOTupleConIndice(TPropsEst)

# tanto las listas como las tuplas tiene indexacion
props = TPropsEst[2:4]
print(props)
props = Lestudiantes[2:4]
print(props)
props = TPropsEst[-1]
print(props)
props = Lestudiantes[-1]
print(props)

#imprimir porpiedades de la clase lista
# print(dir(Lestudiantes))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
detailVar(Lestudiantes)

# 'append', Agrega un neuvo elemento al final de la lista
Lestudiantes.append('mariana')
# 'insert', agrega un elemento a la lista en una pos especifica
Lestudiantes.insert(5,'maira')
printListOTupleConIndice(Lestudiantes)

# 'pop', remueve un valor de la lista segun su pos
Lestudiantes.pop()
# 'remove', remueve un valor de la lista segun su valor
Lestudiantes.remove('maira')
printListOTupleConIndice(Lestudiantes)

# 'count', cuenta cuenates veces encuentra un valor en la lista
print("El count de Juan me retorna",Lestudiantes.count('Juan'))
# 'extend', extiende una lista con una segunda lista o una tupla
Lestudiantes.extend(TPropsEst)
# 'index',  captura la pos (index) de primera aparicion de un valor de la lista
primer = Lestudiantes.index('Juan')
print("El primer Juan esta en", primer)
print("El Segundo Juan esta en la pos",Lestudiantes.index('Juan',primer+1))

# 'copy', crea una copia de la lista
copyList = Lestudiantes.copy()
print(copyList)
# 'reverse', organiza la lista en sentido contrario
Lestudiantes.reverse()
# printListOTupleConIndice(Lestudiantes)
# 'sort' organiza la lista de mayor a menor
Lestudiantes.sort(reverse=True)
# printListOTupleConIndice(Lestudiantes)
Lestudiantes.sort()
printListOTupleConIndice(Lestudiantes)

#Modificar por indexacion
Lestudiantes[10]='Nuevo Valor'
printListOTupleConIndice(Lestudiantes)

#Actualiacion de variables en lista
listaAux = ['Camilo','Jose']
listaDeListas = [Lestudiantes,listaAux]
print(listaDeListas)

# Lestudiantes += 'Mariana' # de esta forma agrega cada caracter a la lista como si fuera un nuevo nombre
Lestudiantes += ['Mariana']
listaAux += ['Mariana']
print(listaDeListas)
print(listaAux)
print(Lestudiantes)


# 'clear', limpia toda la lista
Lestudiantes.clear()
# printListOTupleConIndice(Lestudiantes)