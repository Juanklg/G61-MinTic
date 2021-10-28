import pandas as pd
import numpy as np

print("Construyendo la primera serie".center(50,'-'))

ventas = pd.Series([15,12,21],index=["Ene","Feb","Mar"])

print(ventas)
print("Indexar serie".center(50,'-'))
print(ventas[2])
print(ventas['Feb'])
print("dtype y values".center(50,'-'))
print(ventas.dtype)
print(ventas.values)
print("atributo name".center(50,'-'))
ventas.name = "pruebas pandas"
ventas.index.name = "Meses"
print(ventas.index)
print("atributo axes y shape".center(50,'-'))
print(ventas.axes)
print(ventas.shape)

print("Construyendo DataFrame".center(50,'-'))
datos = {
    "manzanas":[3,2,0,1],
    "naranjas":[0,3,7,2]
}
# compras = pd.DataFrame(datos)
compras = pd.DataFrame(datos,index=['Juno',"Roberto","Lily","David"])
print(compras)
print(compras.columns)
print(compras.index)
compras.index.name = "Clientes"
compras.columns.name = "Frutas"
print("DataFrame axes y shape".center(50,'-'))
print(compras.axes)
print(compras.shape)
print("DataFrame values".center(50,'-'))
print(compras.values)
print("DataFrame completo".center(50,'-'))
print(compras)

print("Construyendo Series".center(50,'-'))
s = pd.Series([7,3,5],index=['Ene','Feb','Mar'])
print(s)

print("Construyendo Series desde dict".center(50,'-'))
d = {'Ene':9,'Feb':6,'Mar':7}
s2 = pd.Series(d,index=['Ene','Feb','Mar','Abr'],dtype=int)
print(s2)

print("Construyendo Series desde dict".center(50,'-'))
elementos = {
    'Numero Atomico':[1,6,47,88],
    'Masa atomica':[1.008,12.485,107.34,124],
    'familia':['No metal','metal','metal','metal']
}
tp = pd.DataFrame(elementos)
print(tp)

print("Construyendo Series desde lista de dict".center(50,'-'))
uni = [
    {"Ag":2, "Au":5, "Cu":3, "Pt":2},
    {"Ag":4, "Au":6, "Cu":7, "Pt":2},
    {"Ag":3, "Pb":2, "Cu":4, "Pt":1}
]

unidades = pd.DataFrame(uni,index=[2015,2016,2017])
print(unidades)

print("Construyendo dataframe completo desde series".center(50,'-'))
meses = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago","sep", "oct", "nov", "dic"]
entrada = [11, 18, 12, 16, 9, 16, 22, 28, 31, 29, 30, 12]
salida = [9, 26, 18, 15, 6, 22, 19, 25, 34, 22, 21, 14]

print("Entradas".center(60,'-'))
entradas = pd.Series(entrada,index = meses)
print(entradas)

print("Salidas".center(60,'-'))
salidas = pd.Series(salida,index = meses)
print(salidas)

print("Almacen".center(60,'-'))
objeto = {
    "entradas":entradas,
    "salidas":salidas,
}
almacen = pd.DataFrame(objeto)
almacen['neto'] = almacen.entradas-almacen.salidas
print(almacen)

print("Metodo Head, tail y sample".center(60,'-'))
print("Head".center(60,'-'))
print(almacen.head(2))#Entre parentesis captura la cantidad e elementos q quiero capturar
print("tail".center(60,'-'))
print(almacen.tail(2))#Entre parentesis captura la cantidad e elementos q quiero capturar
print("sample".center(60,'-'))
print(almacen.sample(3))

print("Metodo describe e info".center(60,'-'))
print("describe".center(60,'-'))
print(almacen.describe())
print("info".center(60,'-'))
print(almacen.info())

print("Metodo value_counts".center(60,'-'))
s = pd.Series([3, 1, 2, 1, 1, 4, 1, 2, np.nan])
print(s.value_counts(dropna=False))#dropna false incluye los NaN
print("Metodo value_counts bins".center(60,'-'))
print(s.value_counts())
print(s.value_counts(bins = 4))


print("Series uso de rango".center(60,'-'))
print(ventas)
print("".center(60,'-'))
print(ventas[1:])
print("".center(60,'-'))
print(ventas[:1])
print("".center(60,'-'))
print(ventas['Ene':'Feb'])
print("Series uso de rango iloc".center(60,'-'))
print(ventas.iloc[1])
print(ventas.iloc[-1])
print(ventas.iloc[[-1,0]])
print(ventas.iloc[0:2])

print("subseries por medio de arrays y bools".center(60,'-'))
s = pd.Series([5, 2, -3, 7, 8, 4])
print(s)
print(s[[True, False, False, True, True, False]])
print(s)
print(s[s>2])
print("sub series por medio de arrays y bools (loc e iloc)".center(60,'-'))
print(s.loc[[True, False, False, True, True, True]])
print(s.loc[s>2])
# print(s.iloc[s>2]) genera eeror por ser iloc
res = (s>2).values
print(res)
print(s.iloc[res])

print("Seleccion indices y etiquetas".center(60,'-'))
df = pd.DataFrame(np.arange(18).reshape([6, 3]),
                 index = ["a", "b", "c", "d", "e", "f"],
                 columns = ["A", "B", "C"])

print(df)
print("get indice columnas".center(60,'-'))
print(df.columns.get_loc("B"))
print(df.columns.get_indexer(["A", "C"]))
print("get indice index(Rows)".center(60,'-'))
getLoc = df.index.get_loc("d")
getIndexer = df.index.get_indexer(["c", "e"])
print(getLoc)
print(getIndexer)
print("combinando metodos".center(60,'-'))
co = df.iloc[df.index.get_loc("c"), 2]
print(co)
co = df.iloc[[5, 3], df.columns.get_indexer(["C", "A"])]
print(co)

print("DataFrame uso de listas de booleanos".center(60,'-'))
df = pd.DataFrame(np.arange(18).reshape([6, 3]),
                 index = ["a", "b", "c", "d", "e", "f"],
                 columns = ["A", "B", "C"])

print(df)
# mask = [True, False, True,False, False,True]
mask = (df.A>7)
print(mask)
print(df[mask])
print("uso de listas de booleanos con loc".center(60,'-'))
print(df.loc[df.B>6])
print("uso de listas de booleanos con iloc".center(60,'-'))
print(df.iloc[(df.B>6).values])

print("DataFrame seleccion aleatoria ".center(60,'-'))
print(df)
print("En las filas ".center(60,'-'))
dfSample = df.sample(3, random_state = 18)
print(dfSample)
print("En las columnas".center(60,'-'))
dfSample = df.sample(2, random_state = 16, axis = 1)#axis 1 es = a columnas
print(dfSample)

print("Metodo DataFrame pop".center(60,'-'))
df = pd.DataFrame(np.arange(15).reshape([3, 5]),
                  index = ["a", "b", "c"],
                  columns = ["A", "B", "C", "D", "E"])
print(df)
diccionario = df.to_dict()
print(diccionario)
print(df.pop('B'))
print(df)
print(df.drop(["a", "c"], axis = 0))
print(df)

print("Series Metodo Series pop y drop".center(60,'-'))
s = pd.Series([1,2,3,4,5],index=["a", "b", "c","d", "e"])
print(s)
print(s.drop("b"))
print(s)
print(s.drop(["d","a"]))
print(s)
print(s.pop("b"))
print(s)

print("Serie Metodo Where".center(60,'-'))
s = pd.Series(np.arange(0, 10))
print(s)
# print(s.where(s%2==0))
print(s.where(s%2==0,0))

print("Edicion DataFrame".center(60,'-'))
print(df)
df.iloc[1,2] = -1
print(df)
df['A'] = 10
print(df)
df['A'] = [10,20,30]
print(df)
print("Edicion DataFrame otro".center(60,'-'))
df = pd.DataFrame(np.arange(12).reshape([4, 3]),
                  index = ["a", "b", "c", "d"],
                  columns = ["A", "B", "C"])

print(df)
df.loc["b":"c", "A":"B"] = [[-1, -2], [-3, -4]]
print(df)
df.loc["b":"c", "A":"B"] = -1
print(df)

print("Edicion DataFrame where".center(60,'-'))
df = pd.DataFrame(np.arange(12).reshape(-1, 3), columns=["A", "B", "C"])
print(df)
print(df.where(df % 2 == 0,-df))

print("Union de series".center(60,'-'))
s = pd.Series([1, 2, 3, 4, 5,], index = ["a", "b", "c", "d", "e"])
r = pd.Series([10, 11, 12], index = ["f", "g", "h"])

print(s)
print(r)
t = pd.concat([s, r])
print(type(t))
print(t)

print("Union de series con axis".center(60,'-'))

a = pd.Series([1, 2, 3, 4, 5,], index = ["a", "b", "c", "d", "e"])
b = pd.Series([10, 11, 12], index = ["a", "b", "f"])
r = pd.concat([a, b], axis = 1)
print(r)

s = pd.Series([1, 2, 3, 4], index = ["a", "b", "c", "d"])
r = pd.Series([10, 11, 12], index = ["a", "c", "e"])
print(pd.concat([s, r]))

print("append de series ".center(60,'-'))
a = pd.Series([1, 2, 3, 4, 5], index = ["a", "b", "c", "d", "e"])
b = pd.Series([10, 11, 12], index = ["f", "g", "h"])

print(a)
print(b)
print(a.append(b))