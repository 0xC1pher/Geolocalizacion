# geolocation.py
import requests
from config import GOOGLE_API_KEY, OPENCELLID_API_KEY

def obtener_geolocalizacion(datos):
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_API_KEY}"
    try:
        response = requests.post(url, json=datos)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud a Google: {e}")
        return None

def obtener_ubicacion_opencellid(cell_towers):
    url = "https://opencellid.org/api/cell/get"
    params = {
        "key": OPENCELLID_API_KEY,
        "mcc": cell_towers[0]["mobileCountryCode"],
        "mnc": cell_towers[0]["mobileNetworkCode"],
        "lac": cell_towers[0]["locationAreaCode"],
        "cellid": cell_towers[0]["cellId"],
        "format": "json"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if "lat" in data and "lon" in data:
            return {
                "latitud": data["lat"],
                "longitud": data["lon"],
                "precision": data.get("range", "N/A")
            }
        else:
            return {"error": "No se pudo obtener la ubicación."}
    except requests.exceptions.RequestException as e:
        return {"error": f"Error en la solicitud a OpenCelliD: {e}"}

def obtener_ubicacion_mozilla(cell_towers):
    url = "https://location.services.mozilla.com/v1/geolocate"
    datos = {
        "cellTowers": cell_towers
    }
    try:
        response = requests.post(url, json=datos)
        response.raise_for_status()
        data = response.json()
        if "location" in data:
            return {
                "latitud": data["location"]["lat"],
                "longitud": data["location"]["lng"],
                "precision": data.get("accuracy", "N/A")
            }
        else:
            return {"error": "No se pudo obtener la ubicación."}
    except requests.exceptions.RequestException as e:
        return {"error": f"Error en la solicitud a Mozilla: {e}"}
