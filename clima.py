from consumer_api import *
from datetime import date

today = date.today()


def print_weather(city_weathers, **kwargs):
    date_user = kwargs.get('date_user')
    if date_user:
        date_str = date_user
    print("Clima para el dia".center(50, "-"))
    print("Estado:", city_weathers['weather_state_name'])
    print("Máxima:", city_weathers['max_temp'])
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
            try:
                cities = city_weathers[0]['consolidated_weather'].pop()
            except IndexError:
                cities = None
                print("Ups Algo ha salido mal")
            if cities:
                print_weather(cities)

        if option_menu == "2":
            print("Introduzca las coordenadas (latitud y longitud)".center(50, "-"))
            latt = input("latitud:")
            long = input("longitud:")
            city_weathers = find_weather_by_coodenadas(latt, long)
            print_weather(city_weathers[0]['consolidated_weather'].pop())

        if option_menu == "3":
            print("Introsuzca la fecha en formato 2021/11/22: ".center(50, "-"))
            date_user = input("Fecha:")
            print("Por que desea buscar: ".center(50, "-"))
            print("1. Buscar por coordenadas (latitud y longitud)")
            print("2. Buscar por ciudad")
            opt_menu = input(":")
            if opt_menu == "1":
                print("Introduzca las coordenadas (latitud y longitud)".center(50, "-"))
                latt_d = input("latitud:")
                long_d = input("longitud:")
                city_weathers = find_weather_by_coodenadas(latt_d, long_d, date_user=date_user)

            elif opt_menu == "2":
                print("Introduzca la ciudad".center(50, "-"))
                city_d = input("Ciudad:")
                city_weathers_d = find_weather_by_city(city_d, date_user=date_user)
                print_weather(city_weathers_d[0].pop(), date_user=date_user)
            else:
                print("Opcion no valida!")

        elif option_menu == "q":
            print("Hasta la Proxima!!!".center(40, "-"))
            break
    else:
        print("Ha seleccionado una Opcion no valida! USE ESPEJUELOS")
