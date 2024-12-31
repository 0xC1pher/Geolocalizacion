# geoMAC.py
from geolocation import obtener_geolocalizacion

def geolocalizar_por_wifi(mac_addresses):
    datos = {
        "considerIp": "false",
        "wifiAccessPoints": [{"macAddress": mac} for mac in mac_addresses]
    }
    resultado = obtener_geolocalizacion(datos)
    if resultado:
        print(f"Latitud: {resultado['location']['lat']}")
        print(f"Longitud: {resultado['location']['lng']}")
        print(f"Precisión: {resultado['accuracy']} metros")
    else:
        print("No se pudo obtener la ubicación.")
