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