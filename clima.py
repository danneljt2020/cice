from consumer_api import *
from datetime import date
import datetime

today = date.today()


def print_weather(city_weathers, **kwargs):
    msg_str = "Clima para el dia "
    date_user = kwargs.get('date_user')
    if date_user:
        msg_str = msg_str + " " + date_user
    print(msg_str.center(50, "-"))
    print("Estado:", city_weathers['weather_state_name'])
    print("Máxima:", city_weathers['max_temp'])
    print("Sensación térmica:", city_weathers['the_temp'])
    print("Humedad:", city_weathers['humidity'])
    print("Velocidad del viento y dirección:", city_weathers['wind_direction'])
    print("**********************".center(50, "-"))


user = "r"
menu = ['1', '2', '3', '4', 'Q', 'q']

while user.lower() != "q":
    print("Bienvenido Clima MAX".center(50, "-"))
    print("1. Buscar por ciudad")
    print("2. Buscar por coordenadas (latitud y longitud)")
    print("3. Buscar por ciudad/coordenadas en una determinada fecha")
    print("4. Planificar Viaje")
    print("Presione la letra Q para salir")
    option_menu = input(":")

    if option_menu == "":
        tomorrow = today + datetime.timedelta(days=1)
        tomorrow_2 = tomorrow + datetime.timedelta(days=1)

        print("Pronostico para los proximos 3 dias en Madrid")
        latt = "40.420300"
        long = "-3.705770"
        f1 = find_weather_by_coodenadas(latt, long, date_user=today.strftime("%Y/%m/%d"))[0].pop()
        f2 = find_weather_by_coodenadas(latt, long, date_user=tomorrow.strftime("%Y/%m/%d"))[0].pop()
        f3 = find_weather_by_coodenadas(latt, long, date_user=tomorrow_2.strftime("%Y/%m/%d"))[0].pop()
        print_weather(f1, date_user=today.strftime("%Y/%m/%d"))
        print_weather(f2, date_user=tomorrow.strftime("%Y/%m/%d"))
        print_weather(f3, date_user=tomorrow_2.strftime("%Y/%m/%d"))

    if option_menu in menu:
        if option_menu == "1":
            print("Introduzca la ciudad".center(50, "-"))
            ciudad = input("Ciudad:")
            city_weathers = find_weather_by_city(ciudad)

            try:
                cities = city_weathers[0]['consolidated_weather'].pop()
            except IndexError:
                cities = None
                print("No se ha encntrado la ciudad introducida")
            if cities:
                print_weather(cities)

        if option_menu == "2":
            print("Introduzca las coordenadas (latitud y longitud)".center(50, "-"))
            latt = input("latitud:")
            long = input("longitud:")
            city_weathers = find_weather_by_coodenadas(latt, long)

            if len(city_weathers)>0:
                cities_coords = city_weathers[0]['consolidated_weather'].pop()
                if cities_coords:
                    print_weather(cities_coords)
            else:
                print("No se ha encontrado localizacion valida para las coordenadas introducidas")

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

                if len(city_weathers) > 0:
                    cities_coords_o = city_weathers[0].pop()
                    if cities_coords_o:
                        print_weather(cities_coords_o)
                else:
                    print("No se ha encontrado localizacion valida para las coordenadas introducidas")

            elif opt_menu == "2":
                print("Introduzca la ciudad".center(50, "-"))
                city_d = input("Ciudad:")
                city_weathers_d = find_weather_by_city(city_d, date_user=date_user)

                try:
                    cities_date = city_weathers_d[0].pop()
                except IndexError:
                    cities_date = None
                    print("Ups Algo ha salido mal")
                if cities_date:
                    print_weather(cities_date, date_user=date_user)
            else:
                print("Opcion no valida!")

        if option_menu == "4":
            print("Introduzca las ciudades".center(50, "-"))
            city_origin = input("Ciudad Origen:")
            city_destiny = input("Ciudad Destino:")
            estimate_data_trip = estimate_trip(city_origin, city_destiny)

            if len(estimate_data_trip) > 0:
                print("Datos de su viaje")
                print("Distancia:", estimate_data_trip.get('distance'))
                print("Clima:", estimate_data_trip.get('is_bad_weather'))
                print("Duracion:", estimate_data_trip.get('duration'))

                input("")
            else:
                print("Una de las ciudades no existe")

        elif option_menu == "q":
            print("Hasta la Proxima!!!".center(40, "-"))
            break
    else:
        print("Ha seleccionado una Opcion no valida! USE ESPEJUELOS")
