import pandas as pd

df = pd.read_excel(r"D:\Users\Admin\Desktop\DistribuidoresARG2.xlsx")
caracter = '.'
#Agrego puntos para separar los numeros de la latitud y longitud
def agregar_punto(numero): 
    if pd.notnull(numero):
        numero = str(numero)
        return '{}{}{}'.format(numero[:3], '.', numero[3:])
    else:
        return numero
df['Latitud'] = df['Latitud'].apply(agregar_punto)
df['Longitud'] = df['Longitud'].apply(agregar_punto)

#Elimino el anteultimo caracter, que en el csv aparecía automaticamente.
def eliminar_penultimo_caracter(numero):
    if pd.notnull(numero):
        numero = str(numero)
        return numero[:-2] + numero[-1]
    else:
        return numero

df['Latitud'] = df['Latitud'].apply(eliminar_penultimo_caracter)
df['Longitud'] = df['Longitud'].apply(eliminar_penultimo_caracter)
