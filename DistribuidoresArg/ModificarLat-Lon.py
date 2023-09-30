import pandas as pd

df = pd.read_excel(r"D:\Users\Admin\Desktop\DistribuidoresARG2.xlsx")
caracter = '.'
def agregar_punto(numero):
    if pd.notnull(numero):
        numero = str(numero)
        return '{}{}{}'.format(numero[:3], '.', numero[3:])
    else:
        return numero
df['Latitud'] = df['Latitud'].apply(agregar_punto)
df['Longitud'] = df['Longitud'].apply(agregar_punto)

def eliminar_penultimo_caracter(numero):
    if pd.notnull(numero):
        numero = str(numero)
        return numero[:-2] + numero[-1]
    else:
        return numero

df['Latitud'] = df['Latitud'].apply(eliminar_penultimo_caracter)
df['Longitud'] = df['Longitud'].apply(eliminar_penultimo_caracter)

#df.to_csv(r'D:\Users\Admin\Downloads\bd\FINAL.csv', encoding='latin-1', sep=';')