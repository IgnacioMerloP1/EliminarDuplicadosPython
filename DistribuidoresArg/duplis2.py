import pandas as pd

df = pd.read_csv(r"D:\Users\Admin\Downloads\bd\BackUp\agrupados.csv", encoding="latin-1", delimiter=";")

df["IDuplicados"] = df["Suc-Loc"].str[:6] + df["Localidad"]
df_duplicados = df[df.duplicated(subset="IDuplicados", keep=False)]

df = df.drop_duplicates(subset="IDuplicados", keep=False)
print(df[:30])

