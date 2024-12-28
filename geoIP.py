#-----------------------------------------------------------------------
#Nombre: geoIP.py
#Descripción: Script de geolocalización basado en la IP del usuario
#Uso: Simplemente ejecutar y te geolocaliza según tu IP pública
#			considerIp: true/false para determinar si usa la IP o no
#Autor:@edusatoe
#------------------------------------------------------------------------
import requests
import os

def obtener_geolocalizacion_ip():
    # Usar una variable de entorno para la API key
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        raise ValueError("API key no encontrada. Configura la variable de entorno 'GOOGLE_API_KEY'.")

    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
    datos = {"considerIp": "true"}

    try:
        response = requests.post(url, json=datos)
        response.raise_for_status()  # Lanza una excepción si la respuesta no es 200 OK
        resultado = response.json()

        if 'location' in resultado:
            latitud = resultado['location']['lat']
            longitud = resultado['location']['lng']
            precision = resultado.get('accuracy', 'N/A')

            print(f"Latitud: {latitud}")
            print(f"Longitud: {longitud}")
            print(f"Precisión: {precision}")
        else:
            print("Error: No se pudo obtener la ubicación.")

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")

if __name__ == "__main__":
    obtener_geolocalizacion_ip()