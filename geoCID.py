# geoCID.py
from geolocation import obtener_geolocalizacion

def geolocalizar_por_celular(cell_towers):
    datos = {
        "considerIp": "false",
        "cellTowers": cell_towers
    }
    resultado = obtener_geolocalizacion(datos)
    if resultado:
        print(f"Latitud: {resultado['location']['lat']}")
        print(f"Longitud: {resultado['location']['lng']}")
        print(f"Precisión: {resultado['accuracy']} metros")
    else:
        print("No se pudo obtener la ubicación.")
