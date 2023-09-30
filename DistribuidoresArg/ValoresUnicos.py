import pandas as pd

df = pd.read_csv(r'D:\Users\Admin\Downloads\bd\regex.csv', encoding='latin-1')

nuevo_df = pd.DataFrame(columns=df.columns) #Creé un df nuevo con las mismas columnas del df antiguo.
for columna in df.columns: #En este bucle, obtengo los valores unicos de cada columna y los cargo en el nuevo df.
    valores_unicos = df[columna].unique()
    nuevo_df[columna] = pd.Series(valores_unicos)

#df.to_csv(r'D:\Users\Admin\Downloads\bd\FINAL.csv', encoding='latin-1', sep=';')
print("Se ha creado el nuevo archivo CSV con los valores únicos:", nuevo_df)
