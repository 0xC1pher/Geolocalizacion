# geoIP.py
from geolocation import obtener_geolocalizacion

def geolocalizar_por_ip():
    datos = {"considerIp": "true"}
    resultado = obtener_geolocalizacion(datos)
    if resultado and 'location' in resultado:
        return {
            "latitud": resultado['location']['lat'],
            "longitud": resultado['location']['lng'],
            "precision": resultado.get('accuracy', 'N/A')
        }
    else:
        return {"error": "No se pudo obtener la ubicación."}
