import pandas as pd
import sys
rutatotal = sys.path[0].split('\\')[:-2]
ruta = ''
for e in rutatotal:
        ruta+=e+'\\'

rutaCsv = ruta+'DataBase\\csv\\'
rutaXls = ruta+'DataBase\\xls\\'


print("definiendo la data".center(50,'-'))

data = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}

print("Dataframe desde IDct".center(50,'-'))
datosDataFrame = pd.DataFrame(data)
print(datosDataFrame)

print("Creando CSV con data".center(50,'-'))
datosDataFrame.to_csv(rutaCsv+'example.csv',sep=';')

print("Leyendo sin header".center(50,'-'))
df = pd.read_csv(rutaCsv+'example.csv', sep=';',
                                header=None)
print(df)

print("Leyendo CSV con header y skiprows;".center(50,'-'))
df = pd.read_csv(rutaCsv+'example.csv', sep=';',
                                skiprows = 1)
print(df)

print("Leyendo CSV con names,skiprow header, na_values para ?; y la columna UID como index".center(50,'-'))
df = pd.read_csv(rutaCsv+'example.csv', 
                            sep=';',
                            names=['UID', 'First Name', 'Last Name', 'Age', 'Sales #1', 'Sales #2'],
                            skiprows=1,
                            na_values='?',
                            index_col ='UID'
                            )
print(df)

print("Excel desde DataFrame".center(50,'-'))
df.to_excel(rutaXls+'primero.xlsx',sheet_name='example')

print("DataFrame desde excel".center(50,'-'))

dfx = pd.read_excel(rutaXls+'primero.xlsx',sheet_name='example',index_col='UID')

print(dfx)


# print("leyendo exel en python".center(50,'-'))
# df = pd.read_excel('desdeCSV.xlsx', sheet_name='example',index_col='UID')
# print(df)





