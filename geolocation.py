# geolocation.py
import requests
from config import GOOGLE_API_KEY

def obtener_geolocalizacion(datos):
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_API_KEY}"
    try:
        response = requests.post(url, json=datos)
        response.raise_for_status()  # Lanza una excepción si la respuesta no es 200 OK
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None
