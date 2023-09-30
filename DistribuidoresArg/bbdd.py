import pandas as pd
import re 

df = pd.read_csv(r'D:\Users\Admin\Downloads\bd\Distribuidores Arg Consolidado.csv', encoding='latin-1', delimiter=';')

def normalizar_valor(valor):
    if isinstance(valor, float):
        valor = str(valor)  
    valor = re.sub(r'\W+', '', valor)  
    valor = valor.lower()  
    return valor
df = df.reset_index(drop=True)
#df.to_csv(r'D:\Users\Admin\Downloads\bd\FINAL.csv', encoding='latin-1', sep=';')


