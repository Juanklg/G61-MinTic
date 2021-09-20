import pandas as pd

def casos(ruta_archivo: str)-> dict:
    df = pd.read_csv(ruta_archivo)

    #con esto consulto el nombre de las columnas    # print(df.columns)

    #crear un peuqeño segmento que me ayude a visualizar

    dfs = df.sample(30)
    print(dfs)
    # resSample = dfs.iloc[:, df.columns.get_indexer(["Departamento o Distrito", "Edad"])]
    resSample = df.iloc[:, df.columns.get_indexer(["Departamento o Distrito", "Edad"])]
    # print(resSample)
    print(resSample['Departamento o Distrito'].value_counts())
    # print(resSample['Edad'].mean())

    listaRes = []

    return listaRes

print(casos(r'C:\Users\MakeDream\Desktop\Ruta1\G61-MinTic\DataBase\csv\casos.csv'))

