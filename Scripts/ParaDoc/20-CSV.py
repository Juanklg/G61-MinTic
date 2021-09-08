import pandas as pd

print("definiendo la data".center(50,'-'))
data = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}
#construir un dataframe desde un dic

print("Creando CSV con data".center(50,'-'))
datosDataFrame = pd.DataFrame(data)
print(datosDataFrame)
datosDataFrame.to_csv('example.csv',sep=';')

print("Leyendo sin header".center(50,'-'))
df = pd.read_csv('example.csv', sep=';',header=None)
print(df)

print("Leyendo CSV con header y skiprows;".center(50,'-'))
df = pd.read_csv('example.csv', sep=';',skiprows = 2)
print(df)

print("Leyendo CSV con names,skiprow header, na_values para ?;".center(50,'-'))
df = pd.read_csv('example.csv', sep=';',names=['UID', 'First Name', 'Last Name', 'Age', 'Sales #1', 'Sales #2'],skiprows=1,na_values='?')
print(df)

print("Leyendo CSV con names,skiprow header, na_values para ?; y la columna UID como index".center(50,'-'))
df = pd.read_csv('example.csv', 
                            sep=';',
                            names=['UID', 'First Name', 'Last Name', 'Age', 'Sales #1', 'Sales #2'],
                            skiprows=1,
                            na_values='?',
                            index_col ='UID'
                            )
print(df)
print("generando exel desde dataframe".center(50,'-'))
print(df.to_excel(r'C:\Users\MakeDream\Desktop\Ruta1\G61-MinTic\DataBase\desdeCSV.xlsx',sheet_name='example'))


print("leyendo exel en python".center(50,'-'))
df = pd.read_excel('desdeCSV.xlsx', sheet_name='example',index_col='UID')
print(df)





