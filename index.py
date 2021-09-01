from numpy.core.records import array
import funciones as fn
from flask import Flask , render_template

fn.isLogin('Login')
print('Corriendo la app',__name__)
#Configura la app
app = Flask(__name__)

# Crea las diferentes rutas -------------------------------------
@app.route("/")
def hello_world():    
    return "Hola Grupo 61"

@app.route("/home")
def index():
    return render_template("index.html")
# Crea las diferentes rutas -------------------------------------    

# Aca inicia la aplicacion si es el archivo principal
if __name__ == "__main__":
    print("Main".center(50,'-'))
    # ventas = pd.Series([15,12,21],index=["Ene","Feb","Mar"])
    # print(ventas)
    
    
    






    
    #debug=True me permite trabajar en desarrollo y actualizar el servidor cada vez que se hagan cambios
    # app.run(debug=True)



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
