from municipios import *

import csv


def pretty_print(municipio):
    print("Nombre municipio:", municipio[1])
    print("Código INE:", municipio[2])
    print("Superficie:", municipio[5] + " km2")
    print("Densidad:", municipio[6] + " km2")
    print("")


with open("municipios.csv", mode="r", encoding="utf8") as file:
    data = list(csv.reader(file, delimiter=";"))
    del data[0]
    user = "r"
    menu = ['1', '2', '3', '4', '5', '6', '7', '8', 'Q', 'q']

    while user.lower() != "q":
        print("Bienvenido Municipios Madrid".center(50, "-"))
        print("1. Obtener municipio por código INE")
        print("2. Obtener el municipio más grande")
        print("3. Obtener superficie total")
        print("4. Obtener densidad total")
        print("5. Obtener la población de Madrid")
        print("6. Obtener la población media de los municipios")
        print("7. LEY BENDFORD")
        print("Presione la letra Q para salir")
        option_menu = input(":")

        if option_menu in menu:
            if option_menu == "1":
                print("Introduzca el INE".center(50, "-"))
                ine = input("ID:")
                pretty_print(getMunicipioByCodeINE(data, ine))

            elif option_menu == "2":
                print("El municipio mas grande es:")
                print("")
                pretty_print(getMunicipioBig(data))

            elif option_menu == "3":
                print("La superficie total de los Municipios es:")
                print("")
                print(getSuperficieTotal(data), "Km cuadrados")

            elif option_menu == "4":
                print("La densidad total de los Municipios es:")
                print("")
                print(getDensidadTotal(data), "km Cuadrados")

            elif option_menu == "5":
                print("La poblacion total de los municipios de madrid es:")
                print("")
                print(getPoblacionMadrid(data), 'personas')

            elif option_menu == "6":
                print("La poblacion media de Madrid es:")
                print("")
                print(getPoblacionMedia(data), 'personas')

            elif option_menu == "7":
                print("LEY:")
                print("")
                density = [mun[-1] for mun in data]
                result = verifyLeyBendford(density)
                for row in result:
                    print(row)

            elif option_menu == "q":
                print("Hasta la Proxima!!!".center(40, "-"))
                break
        else:
            print("Ha seleccionado una Opcion no valida! USE ESPEJUELOS")
