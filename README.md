# Geolocalizacion
* Esto es un fork del codigo original de [@eduSatoe]https://github.com/eduSatoe/geolocation
* Al cual he agregado unas caracteristicas mas y hay un archivo que registra los cambios que se han logrado y se haran

# Rama dev 
## API REST de Geolocalización - Versión 0.1.0

Esta es la primera versión de la API REST de Geolocalización, que permite obtener la ubicación basada en IP, Wi-Fi y torres de celular, combinando resultados de múltiples servicios para mejorar la precisión.

---

## Características Principales

1. **Geolocalización por IP:**
   - Obtiene la ubicación basada en la dirección IP del usuario.
2. **Geolocalización por Wi-Fi:**
   - Utiliza direcciones MAC de puntos de acceso Wi-Fi para estimar la ubicación.
3. **Geolocalización por Torres de Celular:**
   - Usa información de torres de celular (cellId, LAC, MCC, MNC) para obtener la ubicación.
4. **Integración de Servicios Open Source:**
   - Combina resultados de **Google Geolocation**, **OpenCelliD** y **Mozilla Location Service** para mejorar la precisión.
5. **API RESTful:**
   - Expone endpoints HTTP para consumir los servicios de geolocalización.

---

## Endpoints Disponibles

| **Método** | **Endpoint**                     | **Descripción**                                                                 |
|------------|----------------------------------|---------------------------------------------------------------------------------|
| GET        | `/geolocalizacion/ip`            | Obtiene la ubicación basada en la dirección IP del usuario.                     |
| POST       | `/geolocalizacion/wifi`          | Obtiene la ubicación basada en direcciones MAC de puntos de acceso Wi-Fi.       |
| POST       | `/geolocalizacion/celular`       | Obtiene la ubicación basada en información de torres de celular.                |

---

## Ejemplos de Uso

### 1. Geolocalización por IP
```bash
curl http://localhost:5000/geolocalizacion/ip
```
### 2. Geolocalización por Wi-Fi
```
curl -X POST http://localhost:5000/geolocalizacion/wifi \
-H "Content-Type: application/json" \
-d '{"mac_addresses": ["68:bc:0c:64:e6:3f", "c8:f9:f9:d4:80:df"]}'
```
### 3. Geolocalización por Celular
```
curl -X POST http://localhost:5000/geolocalizacion/celular \
-H "Content-Type: application/json" \
-d '{"cell_towers": [{"cellId": 73628675, "locationAreaCode": 268, "mobileCountryCode": 214, "mobileNetworkCode": 1}]}'
```

##Proximos cambios 
```
### - Autenticación y Seguridad:
Implementar autenticación (por ejemplo, tokens JWT) para proteger los endpoints.
### - Monitoreo y Logs:
Añadir un sistema de monitoreo y logs para rastrear el uso y los errores de la API.
```
