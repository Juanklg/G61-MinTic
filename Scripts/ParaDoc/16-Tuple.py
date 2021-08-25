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

#imprimir porpiedades de la clase tupla
# print(dir(TPropsEst))
# 'count', para contar un elemento dentro de la tupla
print(TPropsEst.count('itera'))
# 'index' encontrar la pos de un elemento en la tupla
print(TPropsEst.index('apellido'))

#actualizar una tupla solo transformando a lista y luego retornando a tupla
detailVar(TPropsEst)
TPropsEst=list(TPropsEst)
detailVar(TPropsEst)
TPropsEst[4]="Apellido"
TPropsEst=tuple(TPropsEst)
printListOTupleConIndice(TPropsEst)

TPropsEst = ("proyecto",) + TPropsEst

printListOTupleConIndice(TPropsEst)

#comparacion
print("t1 < t2?",(0,1,6)<(0,3,4))
print("t1 < t2?",(0,1,6)<(0,1,6))

#Patron dsu
#Decorate
#tenemos una lista y la decoramos
printListOTupleConIndice(Lestudiantes)
listDecorate = list()
for est in Lestudiantes:
    listDecorate.append((len(est),est))
printListOTupleConIndice(listDecorate)
#Sort
listDecorate.sort(reverse=True)
printListOTupleConIndice(listDecorate)
#undecorate
finalList = list()
for lgt,est in listDecorate:
    finalList.append(est)

printListOTupleConIndice(finalList)

#desembalaje o unpackage
t1="Proyecto de grupo 61"
t1=t1.split(' ')

s1,s2,*s3=t1
s1,*s2,s3=t1

t1=tuple(t1)
s1,s2,*s3=t1
(s1,s2,s3,s4)=t1

print(s1)
print(s2)
print(s3)
print(s4)
print(t1)

#tuplas y diccionarios
d = {"a":10,"b":1,"c":22}
t = list(d.items())

t.sort(reverse=True)

l=list()
for k,v in t:
    l.append((v,k))
l.sort()

print(l)
