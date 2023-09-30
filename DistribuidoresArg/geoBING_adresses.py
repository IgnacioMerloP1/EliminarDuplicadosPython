import pandas as pd
from geopy.geocoders import Bing
import time

df = pd.read_csv(r"D:\Users\Admin\Downloads\bd\BackUp\TrabajoMauri2.csv", encoding="latin-1", sep=";")

geolocator = Bing(api_key='AkJPc2UmdOsJtN__Qzz2v62Jr0JCM3qpx7iYVq4htjp4qvP7NSYyFxHCvl8eJtyu')

#Obtengo la latidud y longitud mediante los datos que existan en la bbdd, en caso de un campo estar vacío,
#se tendra en cuenta el otro campo unicamente.
def obtener_latitud_longitud(direccion, localidad, provincia):
    if pd.isnull(localidad) and pd.isnull(provincia):
        ubicacion = direccion
    elif pd.isnull(localidad):
        ubicacion = f"{direccion}, {provincia}"
    elif pd.isnull(provincia):
        ubicacion = f"{direccion}, {localidad}"
    else:
        ubicacion = f"{direccion}, {localidad}, {provincia}"

    print("Ubicación:", ubicacion)  # Mensaje de depuración para verificar la formación de la ubicación

    try:
        location = geolocator.geocode(ubicacion)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except Exception as e:
        print("Error de geocodificación:", str(e))  
        return None, None

#Agrego las coordenadas al df.
for index, row in df.iterrows():
    latitud, longitud = obtener_latitud_longitud(row['Direccion'], row['Localidad'], row['Provincia'])
    df.at[index, 'Latitud'] = latitud
    df.at[index, 'Longitud'] = longitud

    time.sleep(2)

