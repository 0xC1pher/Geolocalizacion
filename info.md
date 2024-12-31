```markdown
# Manual de Usuario: API de Geolocalización

Este manual proporciona una guía completa para configurar, usar y entender la API de Geolocalización, que permite obtener la ubicación basada en IP, Wi-Fi y torres de celular.

---

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Configuración](#configuración)
3. [Endpoints](#endpoints)
4. [Ejemplos de Uso](#ejemplos-de-uso)
5. [Casos de Uso](#casos-de-uso)
6. [Ejemplos de Salida](#ejemplos-de-salida)
---

## Introducción

La API de Geolocalización permite obtener la ubicación de un dispositivo utilizando tres métodos:
1. **Geolocalización por IP:** Basada en la dirección IP pública del usuario.
2. **Geolocalización por Wi-Fi:** Basada en las direcciones MAC de los puntos de acceso Wi-Fi cercanos.
3. **Geolocalización por Celular:** Basada en la información de las torres de celular cercanas.

---

## Configuración

### Requisitos
- Python 3.7 o superior.
- Librerías necesarias: `flask`, `requests`.

### Instalación
1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias:
   ```bash
   pip install flask requests
   ```
3. Configura la API key de Google en `config.py`:
   ```python
   # config.py
   import os
   GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', 'YOUR_API_KEY')
   ```

### Ejecución
1. Inicia el servidor API:
   ```bash
   python app.py
   ```
2. El servidor estará disponible en `http://localhost:5000`.

---

## Endpoints

### 1. Geolocalización por IP
- **Método:** GET
- **URL:** `http://localhost:5000/geolocalizacion/ip`
- **Respuesta:**
  ```json
  {
    "latitud": 40.7128,
    "longitud": -74.0060,
    "precision": 100
  }
  ```

### 2. Geolocalización por Wi-Fi
- **Método:** POST
- **URL:** `http://localhost:5000/geolocalizacion/wifi`
- **Body (JSON):**
  ```json
  {
    "mac_addresses": ["68:bc:0c:64:e6:3f", "c8:f9:f9:d4:80:df"]
  }
  ```
- **Respuesta:**
  ```json
  {
    "latitud": 40.7128,
    "longitud": -74.0060,
    "precision": 50
  }
  ```

### 3. Geolocalización por Celular
- **Método:** POST
- **URL:** `http://localhost:5000/geolocalizacion/celular`
- **Body (JSON):**
  ```json
  {
    "cell_towers": [
      {
        "cellId": 73628675,
        "locationAreaCode": 268,
        "mobileCountryCode": 214,
        "mobileNetworkCode": 1
      }
    ]
  }
  ```
- **Respuesta:**
  ```json
  {
    "latitud": 40.7128,
    "longitud": -74.0060,
    "precision": 200
  }
  ```

---

## Ejemplos de Uso

### 1. Geolocalización por IP
```bash
curl http://localhost:5000/geolocalizacion/ip
```

### 2. Geolocalización por Wi-Fi
```bash
curl -X POST http://localhost:5000/geolocalizacion/wifi \
-H "Content-Type: application/json" \
-d '{"mac_addresses": ["68:bc:0c:64:e6:3f", "c8:f9:f9:d4:80:df"]}'
```

### 3. Geolocalización por Celular
```bash
curl -X POST http://localhost:5000/geolocalizacion/celular \
-H "Content-Type: application/json" \
-d '{"cell_towers": [{"cellId": 73628675, "locationAreaCode": 268, "mobileCountryCode": 214, "mobileNetworkCode": 1}]}'
```

---

## Casos de Uso

1. **Aplicaciones de Rastreo:**
   - Obtener la ubicación de un dispositivo en tiempo real.
2. **Servicios de Entrega:**
   - Determinar la ubicación de un repartidor o cliente.
3. **Seguridad:**
   - Verificar la ubicación de un usuario para autenticación.
4. **Análisis de Datos:**
   - Recopilar datos de ubicación para análisis estadísticos.

---

## Ejemplos de Salida

### 1. Geolocalización por IP
```json
{
  "latitud": 40.7128,
  "longitud": -74.0060,
  "precision": 100
}
```

### 2. Geolocalización por Wi-Fi
```json
{
  "latitud": 34.0522,
  "longitud": -118.2437,
  "precision": 50
}
```

### 3. Geolocalización por Celular
```json
{
  "latitud": 51.5074,
  "longitud": -0.1278,
  "precision": 200
}
```

---

## Manual de Usuario

### 1. Configuración
- Asegúrate de tener Python instalado.
- Instala las dependencias con `pip install flask requests`.
- Configura la API key de Google en `config.py`.

### 2. Ejecución
- Inicia el servidor con `python app.py`.
- Usa los endpoints desde tu aplicación o con herramientas como `curl`.

### 3. Uso desde un Frontend
- Crea un archivo HTML con JavaScript para consumir la API.
- Usa `fetch` para hacer solicitudes HTTP a los endpoints.

---

¡Con este manual, estarás listo para configurar, usar y aprovechar al máximo la API de Geolocalización! 😊
```
---
