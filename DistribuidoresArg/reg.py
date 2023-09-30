import pandas as pd 

df = pd.read_csv(r'D:\Users\Admin\Downloads\bd\nueva bd.csv', encoding='latin-1')

new_df = df[['Sucursal','Localidad','suc - loc']]

#df.to_csv(r'D:\Users\Admin\Downloads\bd\FINAL.csv', encoding='latin-1', sep=';')