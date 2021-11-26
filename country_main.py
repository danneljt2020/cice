from country_api import *
user = "r"
menu = ['1', '2', '3', '4', 'Q', 'q']


def print_data(data_country):
    print("Datos del Pais".center(50, "-"))
    print("Capital:", data_country['capital'])
    print("Poblacion:", data_country['population'])
    print("Superficie:", data_country['superficie'])
    print("Idioma:", data_country['lang'])
    print("**********************".center(50, "-"))


while user.lower() != "q":
    print("Bienvenido a Paises".center(50, "-"))
    print("1. Buscar por Pais")
    print("2. Descargar Bandera de paises")
    print("3. Jugar")
    print("Presione la letra Q para salir")
    option_menu = input(":")

    if option_menu in menu:
        if option_menu == "1":
            print("Introduzca el pais".center(50, "-"))
            pais = input("Pais:")
            print_data(find_by_country(pais))

        if option_menu == "2":
            print("Introduzca el pais".center(50, "-"))
            flag_pais = input("Pais:")
            download_flag()

        if option_menu == "3":
            print("Indica el Continente".center(50, "-"))
            continent = input("Continente:")

        elif option_menu == "q":
            print("Hasta la Proxima!!!".center(40, "-"))
            break
    else:
        print("Ha seleccionado una Opcion no valida! USE ESPEJUELOS")