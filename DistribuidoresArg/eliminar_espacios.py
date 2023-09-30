import pandas as pd

df = pd.read_csv(r'D:\Users\Admin\Downloads\bd\nueva bd.csv', encoding='latin-1', delimiter=',')

#Si el valor en cada campo del df es un string, elimina los espacios en blanco al principio y final.
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

columnas_a_limpiar = ['Direccion', 'Provincia', 'Telefono', 'Email', 'Marca']
df[columnas_a_limpiar] = df[columnas_a_limpiar].applymap(lambda x: x.strip() if isinstance(x, str) else x)


