import pandas as pd

df = pd.read_csv(r'D:\Users\Admin\Downloads\bd\regex.csv', encoding='latin-1')

nuevo_df = pd.DataFrame(columns=df.columns)
for columna in df.columns:
    valores_unicos = df[columna].unique()
    nuevo_df[columna] = pd.Series(valores_unicos)

#df.to_csv(r'D:\Users\Admin\Downloads\bd\FINAL.csv', encoding='latin-1', sep=';')
print("Se ha creado el nuevo archivo CSV con los valores únicos:", nuevo_df)
