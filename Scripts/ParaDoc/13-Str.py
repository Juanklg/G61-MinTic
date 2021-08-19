def cualEsMayor(x,y):
    if x < y:
        print(f"x:{x} es menor q y:{y}")
    elif x > y:
        print(f"x:{x} es mayor q y:{y}")
    else:
        print(f"x:{x} es igual a y:{y}")

def detailVar(var:any):
    print("la var es de tipo : ",type(var))
    print("su valor es : ",var)
    print("su longitud es : ",len(var))
    for valor in range(0,len(var)):
        # if valor == 7 : break
        print("En la pos : {1}, el valor es : {0}".format( var[valor], valor ))

def splitText(texto:str):
    listaDePalabras = texto.split(' ')
    return listaDePalabras    

text = "Hola compañeros del grupo 61. feliz tarde del"

#los tipo int no son iterables
number = 15671

# los numeros converdios en str si son iterables
numberToStr = str(56975)

#split text and view detail
st = splitText(text)

#capturamos la penultima posicion del texto
print(text[-2])
#capturamos la ultima posicion del texto
print(text[-1])
print(text[len(text)-1])
#Capturar cualquier posicion
print(text[30])

#las posiciones deben ser numeros enteros (int)
nv = text[31]
#capturar rebanadas
nv = text[30:41]
nv = text[:20]
nv = text[30:]
# nv = text[3:3]

#Comparacion
otroText = "    hola     "
nv = text[:5]
#strip - elemina espacios al rpincipio y al final
nv = nv.strip()
print(len(nv))
if nv == otroText.strip(): print("Los textos son iguales")
else : print("Los textos son diferentes")

#orden alfabetico o comparacion -> python tiene en cuenta el peso de las letras mayusculas y minusculas
cualEsMayor("Hola","Hola")

#capitalize
otroText = "banana"
nv = otroText.capitalize()

#isalnum -> valida q sea alfanumerico si tiene un simbolo es false
otroText = "banana*"
nv = otroText.isalnum()

#isalpha -> valida que solo sean letras en le texto, arroja false si tiene numeros
otroText = "banana5"
nv = otroText.isalpha()

#isascii -> Valida que todos losm caracteres esten dentro de la tabla del ascci
otroText = "banana5"
nv = otroText.isascii()

#count -> cuenta la cantidad de veces que hay un caracater en todo el texto,
otroText = text
nv = otroText.count("a")
#busca la palabra 'del' desde la pos 0 hasta la pos 45
nv = otroText.count("del",0,45)
print(nv)
#tambien se puede agregar la posicion desde la cual empezar a contar
nv = otroText.count("a",10)

#find -> busca la posicion de el caracter
otroText = text
nv = otroText.find("a")

#pyede buscar desde la posicion que le indique en el segundo parametro
nv = otroText.find("a",10)

#endswith -> valida que termine con el texto incluido en los parentesis
nv = otroText.endswith("tarde")

#startswith -> valida que inicie con el texto incluido en los parentesis
nv = otroText.startswith("Hola")
#upper->Conviente todo a mayuscula
nv = otroText.upper()
#lower-> convierte todo a minuscula
nv = nv.lower()

#formato con %
numero = 0x31
otroText = "he visto "+str(numero)+" numeros"
# otroText = "he visto %x numeros" %numero
print(otroText)

#caracteres especiales -> ej \n genera un enter entre los strings
# otroText = "he visto "+str(numero)+" numeros"
otroText = "he visto \ntodos los numeros"

#replace -> replnaza cualquier arreglo de caracteres por otro arreglo de caracteres
otroText = text
nv = otroText.replace("a","A")
#seleccion al cantidad de remplazos
nv = otroText.replace("a","A",1)

#format() function para fromatear cualquier texto
# detailVar(text)
nv = text[20:25]
# print(nv)

#concatenar y multiplcar
tx = "palabra1"
tx2 = "hola "

tx+=tx2
print(tx+" "+tx2*5)
