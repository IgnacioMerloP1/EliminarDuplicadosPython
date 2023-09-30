import pandas as pd

df = pd.read_csv(r'D:\Users\Admin\Downloads\bd\BackUp\agrupados.csv', encoding='latin-1', delimiter=';')

#Creo una nueva columna para poder identificar los registros duplicados, ya que en la columna "Suc-Loc" 
#hay muchos registros que sin estar escritos de la misma forma, son duplicados, por eso tomo los primeros 
# 6 caracteres y lo unifico con el valor en la columna localidad. Asi identifico a los duplicados. 
df['IDuplicados'] = df['Suc-Loc'].str[:6] + df['Localidad']

df = df.sort_values(by='IDuplicados').groupby('IDuplicados').apply(lambda x: x.ffill().bfill())

