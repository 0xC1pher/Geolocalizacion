# main.py
from geoIP import geolocalizar_por_ip
from geoMAC import geolocalizar_por_wifi
from geoCID import geolocalizar_por_celular

def mostrar_menu():
    print("----------------------------------------")
    print("Menú de Geolocalización")
    print("1. Geolocalización por IP")
    print("2. Geolocalización por Wi-Fi")
    print("3. Geolocalización por Torres de Celular")
    print("4. Salir")
    print("----------------------------------------")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\nObteniendo ubicación por IP...")
            geolocalizar_por_ip()
        elif opcion == "2":
            print("\nObteniendo ubicación por Wi-Fi...")
            mac_addresses = ["68:bc:0c:64:e6:3f", "c8:f9:f9:d4:80:df"]  # Ejemplo de direcciones MAC
            geolocalizar_por_wifi(mac_addresses)
        elif opcion == "3":
            print("\nObteniendo ubicación por Torres de Celular...")
            cell_towers = [
                {"cellId": 73628675, "locationAreaCode": 268, "mobileCountryCode": 214, "mobileNetworkCode": 1}
            ]  # Ejemplo de torres de celular
            geolocalizar_por_celular(cell_towers)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
