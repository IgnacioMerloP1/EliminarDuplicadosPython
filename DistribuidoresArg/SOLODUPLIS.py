import pandas as pd

df = pd.read_csv(r"D:\Users\Admin\Downloads\bd\BackUp\SOLODUPLICADOS.csv", encoding="latin-1", delimiter=";")

df = df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'])

df = df.sort_values(by='IDuplicados')

df = df.groupby('IDuplicados').apply(lambda x: x.ffill().bfill())

df = df.drop_duplicates(subset='IDuplicados')

print(df)
