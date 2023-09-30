import pandas as pd

df = pd.read_excel(r"D:\Users\Admin\Desktop\DistribuidoresARG.xlsx")

df['Latitud'] = df['Latitud'].apply(lambda x: '{:.9f}'.format(float(x)).replace('.', '').replace('-', '') if pd.notnull(x) else x)
df['Longitud'] = df['Longitud'].apply(lambda x: '{:.9f}'.format(float(x)).replace('.', '').replace('-', '') if pd.notnull(x) else x)

df['Latitud'] = df['Latitud'].apply(lambda x: '{}.{}.{}'.format(x[:-9], x[-9:-6], x[-6:]) if pd.notnull(x) else x)
df['Longitud'] = df['Longitud'].apply(lambda x: '{}.{}.{}'.format(x[:-9], x[-9:-6], x[-6:]) if pd.notnull(x) else x)

#df.to_csv(r'D:\Users\Admin\Downloads\bd\FINAL.csv', encoding='latin-1', sep=';')