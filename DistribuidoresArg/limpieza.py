import pandas as pd

df = pd.read_csv(r'D:\Users\Admin\Downloads\bd\SinDupla.csv', encoding='latin-1', delimiter=';')

df = df.drop('Unnamed: 0',axis=1)
df = df.drop('Unnamed: 0.1',axis=1)

print(df.head())
#df.to_csv(r'D:\Users\Admin\Downloads\bd\FINAL.csv', encoding='latin-1', sep=';')