import requests as req
import json

url = 'https://www.metaweather.com/api/location/search/?query=mad'
response = req.get(url)
data = response.json()

user = "r"
menu = ['1', '2', '3', 'Q', 'q']

while user.lower() != "q":
    print("Bienvenido Clima MAX".center(50, "-"))
    print("1. Buscar por ciudad")
    print("2. Buscar por coordenadas (latitud y longitud)")
    print("3. Buscar por ciudad/coordenadas en una determinada fecha")
    print("Presione la letra Q para salir")
    option_menu = input(":")

    if option_menu in menu:
        if option_menu == "1":
            print("Introduzca la ciudad".center(50, "-"))
            ciudad = input("Ciudad:")
            print(ciudad)

        if option_menu == "2":
            print("Introduzca las coordenadas (latitud y longitud)".center(50, "-"))
            lat = input("latitud:")
            long = input("longitud:")

        if option_menu == "2":
            print("Por que desea buscar".center(50, "-"))
            print("2. Buscar por coordenadas (latitud y longitud)")
            print("3. Buscar por ciudad en una determinada fecha")
            city_coordenada = input("latitud:")


        elif option_menu == "q":
            print("Hasta la Proxima!!!".center(40, "-"))
            break
    else:
        print("Ha seleccionado una Opcion no valida! USE ESPEJUELOS")
