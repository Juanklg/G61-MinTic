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

isLogin('Login')
#----------------------------------------------------------------------------
print('Corriendo la app')

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

texto = "Hola Grupo 61 desde python"
print("Lgt",len(texto))

# Se describe con corchetes
s = set(range(1,7))
detailArch(s)
#acepta varios tipos de variables
# s = {True,"Grupo 61",10.5,(1,4,"Hola")}
#no acepta listas ni diccionarios

cText = set(texto)
detailArch(cText)
cEst = set(Lestudiantes)
detailArch(cEst)

print('Maria' in cEst)

s2 = {9,2,6,8,0}

#s,cEst,cText
#dir
# print(dir(cEst))

#Hacemos una copia
s3 = s2.copy()
print('copy')
detailArch(s2)
detailArch(s3)
#Comparacion con iguales
#compara uno a uno los elementos del conjunto
print("son iguales",(s3==s2))

# # add elemento
print('add')
s3.add('Formador')
detailArch(s2)
detailArch(s3)
# # difference
# #retorna la diferencia q tiene el elemento inicial con el q entra como argumento
print('difference s3(s2)',s3.difference(s2))
print("s3-s2",s3-s2)
#en este caso todos los elementos del s5 se encuentarn en el s3
print('difference s2(s3)',s2.difference(s3))
print("s2-s3",s2-s3)

# #difference_update ->
print('difference_update',s3.difference_update(s2))
print("Nuevo s3",s3)
# #discard elimina si existe o si no continua normal
print('discard',s3.discard('Formador'))
print("Nuevo s3",s3)
# #remove elmina pero retorna error si el elemnto no existe
# print('remove',s3.remove('Formado'))
# # intersection retorna los elementos q se encuentra en ambos conjntos
detailArch(s)
detailArch(s2)
print('intersection',s3.intersection(s2))
print('intersection',(s2 & s3))
print('intersection',s2.intersection(s))
print('intersection',(s & s2))
# # isdisjoint
print('isdisjoint no comparten elementos?',s3.isdisjoint(s2))
print('isdisjoint no comparten elementos?',s.isdisjoint(s2))
# # intersection_update realiza la actualizacion de la variable
print('intersection_update compa',s2.intersection_update(s))
print("New s2",s2)
# # issubset
print('issubset s in s2',s.issubset(s2))
print('issubset s2 in s',s2.issubset(s))
# issuperset
print('issuperset s in s2',s.issuperset(s2))
print('issuperset s2 in s',s2.issuperset(s))

# symmetric_difference
print('symmetric_difference s y s2',s.symmetric_difference(s2))
print('symmetric_difference_update s3 con s2',s3.symmetric_difference_update(s2))
print('symmetric_difference_update s2 con s',s2.symmetric_difference_update(s))
print("nuevo s2",s2)
print("nuevo s3",s3)

# union
print('union s2(s3)',s2.union(s3))
print('union s2 | s3' ,(s2 | s3))
print('union',(s | s2 |cText))
# update
print('update',s.update(Lestudiantes))
print('before pop',s)
# pop
print('pop',s.pop())
print('pop',s.pop())
print('pop',s.pop())
print('after pop',s)
# clear
print('clear',s.clear())
print(s)

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
