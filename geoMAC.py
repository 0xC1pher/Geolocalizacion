# geoMAC.py
from geolocation import obtener_geolocalizacion

def geolocalizar_por_wifi(mac_addresses):
    datos = {
        "considerIp": "false",
        "wifiAccessPoints": [{"macAddress": mac} for mac in mac_addresses]
    }
    resultado = obtener_geolocalizacion(datos)
    if resultado and 'location' in resultado:
        return {
            "latitud": resultado['location']['lat'],
            "longitud": resultado['location']['lng'],
            "precision": resultado.get('accuracy', 'N/A')
        }
    else:
        return {"error": "No se pudo obtener la ubicación."}
