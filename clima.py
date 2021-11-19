from consumer_api import *
from datetime import date

today = date.today()


def print_weather(city_weathers):
    print("Clima para el dia" + str(today).center(50, "-"))
    print("Estado:", city_weathers['weather_state_name'])
    print("máxima:", city_weathers['max_temp'])
    print("Sensación térmica:", city_weathers['the_temp'])
    print("Humedad:", city_weathers['humidity'])
    print("Velocidad del viento y dirección:", city_weathers['wind_direction'])
    print("**********************".center(50, "-"))


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
            city_weathers = find_weather_by_city(ciudad)
            print_weather(city_weathers[0]['consolidated_weather'].pop())

        if option_menu == "2":
            print("Introduzca las coordenadas (latitud y longitud)".center(50, "-"))
            latt = input("latitud:")
            long = input("longitud:")
            city_weathers = find_weather_by_coodenadas(latt, long)
            print_weather(city_weathers[0]['consolidated_weather'].pop())

        if option_menu == "2":
            print("Por que desea buscar: ".center(50, "-"))
            print("1. Buscar por coordenadas (latitud y longitud)")
            print("2. Buscar por ciudad")
            opt_menu = input(":")
            if opt_menu == "1":
                pass
            elif opt_menu == "2":
                pass
            else:
                print("Opcion no valida")

        elif option_menu == "q":
            print("Hasta la Proxima!!!".center(40, "-"))
            break
    else:
        print("Ha seleccionado una Opcion no valida! USE ESPEJUELOS")
