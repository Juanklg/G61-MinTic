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

def printListOTuple(lt):
    for x in lt:
        print(x)
    else: print('----------------------------')

def printListOTupleConIndice(lt):
    for x in range(0,len(lt)):
        print("Valor en pos",x," = ",lt[x])
    else: print('----------------------------')

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

# 'clear', limpia toda la lista
Lestudiantes.clear()
# printListOTupleConIndice(Lestudiantes)


#imprimir porpiedades de la clase tupla
# print(dir(TPropsEst))
# 'count', para contar un elemento dentro de la tupla
print(TPropsEst.count('itera'))
# 'index' encontrar la pos de un elemento en la tupla
print(TPropsEst.index('apellido'))

TPropsEst=list(TPropsEst)
detailVar(TPropsEst)
TPropsEst[4]="Apellido"
TPropsEst=tuple(TPropsEst)
printListOTupleConIndice(TPropsEst)

#Actualiacion de variabloes en lista
listaAux = ['Camilo','Jose']

lista2 = [Lestudiantes,listaAux]
print(lista2)

# Lestudiantes += 'Mariana' # de esta forma agrega cada caracter a la lista como si fuera un nuevo nombre
Lestudiantes += ['Mariana']
listaAux += ['Mariana']
print(lista2)

# funcion de sort con listas de tuplas
# Asignación de tupla
# set()






# #creamos un diccionario para estudiantes desde la lista de estudiantes
# dictEstudiantes = dict.fromkeys(listEstudiantes)
# #creamos un diccionario desde la tupla con las caracteristicas de un estudiante
# dictInfoEstudiante = dict.fromkeys(tuplaEstudiantes)

# #creo un copia de mi diccioario de estudiantes y recorro el diccinario de estudiantes y les asigno asl propiedas de los estudiantes a todos
# dictEstudiantesCopy = dictEstudiantes.copy()
# for estudiante in dictEstudiantesCopy.keys():
#     dictEstudiantes[estudiante]=dictInfoEstudiante
# printDict(dictEstudiantes)    

# for estudiante in dictEstudiantesCopy.keys():
#     print(estudiante)
#     dictEstudiantes[estudiante]['nombre']=str(estudiante)
#     dictEstudiantes[estudiante]['edad']=15
#     dictEstudiantes[estudiante]['grupo']=61
#     dictEstudiantes[estudiante]['apellido']=''
#     dictEstudiantes[estudiante]['nota']=0.0

# Estudiantes = [
#     {'nombre': 'Andres', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
#     {'nombre': 'Brayan', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
#     {'nombre': 'Jhon', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
#     {'nombre': 'Juan', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
#     {'nombre': 'Karen', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
#     {'nombre': 'Maria', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
#     {'nombre': 'Nicolas', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
#     {'nombre': 'Stuart', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
#     {'nombre': 'Valentina', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0}
# ]

# dictEstudiants = {
#     "Andres":{'nombre': 'Andres', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
#     "Brayan":{'nombre': 'Brayan', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
#     "Jhon":{'nombre': 'Jhon', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
#     "Juan":{'nombre': 'Juan', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
#     "Karen":{'nombre': 'Karen', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
#     "Maria":{'nombre': 'Maria', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
#     "Nicolas":{'nombre': 'Nicolas', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
#     "Stuart":{'nombre': 'Stuart', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
#     "Valentina":{'nombre': 'Valentina', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0}
# }

# pr='nombre'
# if Estudiantes['Juan'][pr] == Estudiantes['Maria'][pr]:
#     print('La propiedad es igual')
# else:
#     print('La propiedad es diferente')

# # set
# tipoSet = {}
