import sys
rutatotal = sys.path[0].split('\\')[:-2]
ruta = ''
for e in rutatotal:
        ruta+=e+'\\'

rutaTxt = ruta+'DataBase\\txt\\'

print("Txt".center(50,'-'))
print("Abrir archivo y si no eiste lo crea".center(50,'-'))
file = open(rutaTxt+'estudiantes.txt','w')
file.write('Estudiantes')
file.close()


print("Escribiendo con el print".center(50,'-'))
file = open(rutaTxt+'estudiantes.txt','a')
print('\nKaren',file=file)
file.close()

estudiantes = ['Valentina','Stuart','Dayanna','Nicolas','Andres']

print("Escribiendo linea a linea ".center(50,'-'))
file = open(rutaTxt+'estudiantes.txt','a')
# for estudiante in estudiantes:
#     file.write(estudiante)
#     file.write('\n')
for estudiante in estudiantes:
    print(estudiante,file=file)
file.close()

print("Escribiendo toda la lista ".center(50,'-'))
file = open(rutaTxt+'estudiantes.txt','a')
print('',file=file)
file.writelines("%s\n" % s for s in estudiantes)
file.close()

print("Leer todo el archivo de texto ".center(50,'-'))
file = open(rutaTxt+'estudiantes.txt','r')
lines = file.readlines()
file.close()
lines = [s.rstrip('\n') for s in lines]
print(lines)

print("Leer linea por linea del archivo de texto ".center(50,'-'))
file = open(rutaTxt+'estudiantes.txt','r')
lines2=[]
for line in file:
    lines2.append(line)
file.close()
lines2 = [s.rstrip('\n') for s in lines2]
print(lines2)





