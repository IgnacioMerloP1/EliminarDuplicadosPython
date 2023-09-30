import pandas as pd

df = pd.read_csv(r'D:\Users\Admin\Downloads\bd\BackUp\agrupados.csv', encoding='latin-1', delimiter=';')

df['IDuplicados'] = df['Suc-Loc'].str[:6] + df['Localidad']
df_duplicados = df[df.duplicated(subset='IDuplicados', keep=False)]

df_sin_duplicados = df.drop_duplicates(subset='IDuplicados', keep=False)

#df.to_csv(r'D:\Users\Admin\Downloads\bd\FINAL.csv', encoding='latin-1', sep=';')
