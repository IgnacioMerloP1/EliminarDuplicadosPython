import pandas as pd

df = pd.read_csv(r'D:\Users\Admin\Downloads\bd\FINAL.csv', encoding='latin-1', delimiter=';')

df_FINAL = pd.read_csv(r'D:\Users\Admin\Downloads\bd\BackUp\SOLODUPLICADOSPRUEBA.csv', encoding='Latin-1', delimiter=';')
df = df._append(df_FINAL, ignore_index=True)
#df.to_csv(r'D:\Users\Admin\Downloads\bd\FINAL.csv', encoding='latin-1', sep=';')