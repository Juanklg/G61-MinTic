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

#conjunto o estructuras de datos es un grupo de elementos que tienen unas caracteristicas especificas

# dict
#se puede definir
usuario={}
car=dict()

diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}

# list
#Creamos una lista con los nombres de los estudiantes
listEstudiantes = [
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

#creamos una tupla con als caracteristicas de los estudiantes
# tuple
tuplaEstudiantes = (
    'nombre',
    'edad',
    'grupo',
    'apellido',
    'nota',
)

#creamos un diccionario para estudiantes desde la lista de estudiantes
dictEstudiantes = dict.fromkeys(listEstudiantes)
#creamos un diccionario desde la tupla con als caracteristicas de un estudiante
dictInfoEstudiante = dict.fromkeys(tuplaEstudiantes)

#creo un copia de mi diccioario de estudiantes y recorro el diccinario de estudiantes y les asigno asl propiedas de los estudiantes a todos
dictEstudiantesCopy = dictEstudiantes.copy()
for estudiante in dictEstudiantesCopy.keys():
    dictEstudiantes[estudiante]=dictInfoEstudiante
printDict(dictEstudiantes)    

for estudiante in dictEstudiantesCopy.keys():
    print(estudiante)
    dictEstudiantes[estudiante]['nombre']=str(estudiante)
    dictEstudiantes[estudiante]['edad']=15
    dictEstudiantes[estudiante]['grupo']=61
    dictEstudiantes[estudiante]['apellido']=''
    dictEstudiantes[estudiante]['nota']=0.0

Estudiantes = {
    "Andres":{'nombre': 'Andres', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
    "Brayan":{'nombre': 'Brayan', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
    "Jhon":{'nombre': 'Jhon', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
    "Juan":{'nombre': 'Juan', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
    "Karen":{'nombre': 'Karen', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
    "Maria":{'nombre': 'Maria', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
    "Nicolas":{'nombre': 'Nicolas', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
    "Stuart":{'nombre': 'Stuart', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0},
    "Valentina":{'nombre': 'Valentina', 'edad': 15, 'grupo': 61, 'apellido': '', 'nota': 0.0}
}

pr='nombre'
if Estudiantes['Juan'][pr] == Estudiantes['Maria'][pr]:
    print('La propiedad es igual')
else:
    print('La propiedad es diferente')

# set
tipoSet = {}
