# geoCID.py
from geolocation import obtener_geolocalizacion, obtener_ubicacion_opencellid, obtener_ubicacion_mozilla

def geolocalizar_por_celular(cell_towers):
    # Obtener ubicación de Google
    datos_google = {
        "considerIp": "false",
        "cellTowers": cell_towers
    }
    resultado_google = obtener_geolocalizacion(datos_google)
    
    # Obtener ubicación de OpenCelliD
    resultado_opencellid = obtener_ubicacion_opencellid(cell_towers)
    
    # Obtener ubicación de Mozilla
    resultado_mozilla = obtener_ubicacion_mozilla(cell_towers)
    
    # Combinar resultados
    resultados = [resultado_google, resultado_opencellid, resultado_mozilla]
    resultados_validos = [r for r in resultados if r and "error" not in r]
    
    if resultados_validos:
        # Elegir el resultado con la mejor precisión
        mejor_resultado = min(resultados_validos, key=lambda x: x.get("precision", float('inf')))
        return mejor_resultado
    else:
        return {"error": "No se pudo obtener la ubicación."}
