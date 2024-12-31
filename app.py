# app.py
from flask import Flask, request, jsonify
from geoIP import geolocalizar_por_ip
from geoMAC import geolocalizar_por_wifi
from geoCID import geolocalizar_por_celular

app = Flask(__name__)

@app.route('/geolocalizacion/ip', methods=['GET'])
def geolocalizacion_ip():
    resultado = geolocalizar_por_ip()
    return jsonify(resultado)

@app.route('/geolocalizacion/wifi', methods=['POST'])
def geolocalizacion_wifi():
    datos = request.json
    if not datos or 'mac_addresses' not in datos:
        return jsonify({"error": "Se requiere una lista de direcciones MAC"}), 400
    resultado = geolocalizar_por_wifi(datos['mac_addresses'])
    return jsonify(resultado)

@app.route('/geolocalizacion/celular', methods=['POST'])
def geolocalizacion_celular():
    datos = request.json
    if not datos or 'cell_towers' not in datos:
        return jsonify({"error": "Se requiere una lista de torres de celular"}), 400
    resultado = geolocalizar_por_celular(datos['cell_towers'])
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
