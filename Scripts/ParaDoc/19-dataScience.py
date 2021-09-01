import pandas as pd
from pandas.core.frame import DataFrame

print("Contruyendo la primera serie".center(50,'-'))

ventas = pd.Series([15,12,21],index=["Ene","Feb","Mar"])

print(ventas)

print(ventas[2])
print(ventas['Feb'])

print(ventas.dtype)
print(ventas.values)

ventas.name = "pruebas pandas"
ventas.index.name = "Meses"
print(ventas.index)

print(ventas.axes)
print(ventas.shape)

print("Contruyendo DataFrame".center(50,'-'))
datos = {
    "manzanas":[3,2,0,1],
    "naranjas":[0,3,7,2]
}

# compras = pd.DataFrame(datos)
compras = DataFrame(datos,index=['Juno',"Roberto","Lily","David"])
print(compras)
print(compras.columns)
print(compras.index)
compras.index.name = "Clientes"
compras.columns.name = "Frutas"

print(compras.axes)
print(compras.shape)

print(compras.values)
print(compras)

print("Contruyendo Series".center(50,'-'))
s = pd.Series([7,3,5],index=['Ene','Feb','Mar'])

d = {
    'Ene':9,
    'Feb':6,
    'Mar':7
}

s2 = pd.Series(d,index=['Ene','Feb','Mar'],dtype=int)


print(s2)
