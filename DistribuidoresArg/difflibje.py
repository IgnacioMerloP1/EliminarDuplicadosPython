import difflib

def encontrar_correspondencia(valor, lista_valores):
    mejor_coincidencia = None
    mejor_ratio = 0
    for val in lista_valores:
        ratio = difflib.SequenceMatcher(None, valor, val).ratio()
        if ratio > mejor_ratio:
            mejor_coincidencia = val
            mejor_ratio = ratio
    return mejor_coincidencia

def reemplazar_valores(lista_orig, lista_valores):
    lista_nueva = []
    for valor in lista_orig:
        coincidencia = encontrar_correspondencia(valor, lista_valores)
        if coincidencia:
            lista_nueva.append(coincidencia)
        else:
            lista_nueva.append(valor)  
    return lista_nueva

valores_originales = [
    "formuladora los aromos SA",
    "otra empresa",
    "formuladora de los aromos sociedad anonima",
    "empresa XYZ"
]

valores_unicos = [
    "formuladora de los aromos sociedad anonima",
    "otra empresa",
    "empresa XYZ"
]

valores_actualizados = reemplazar_valores(valores_originales, valores_unicos)
print(valores_actualizados)