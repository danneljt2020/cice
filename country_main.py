from country_api import *

user = "r"
menu = ['1', '2', '3', '4', 'Q', 'q']
continents = ['europe', 'africa', 'asia', 'americas']


# get one answer random
def print_answer():
    answers = {
        'capital': "Cual es la capital de: ",
        'population': "Cual es la poblacion de: ",
        'lang': "Cual es el idioma de: ",
        'superficie': "Cual es la superficie de: ",
        'region': "A que region pertenece el pais: ",
        'calling_code': "Cual es el codigo telefonico para llamar al pais: ",
        'europe': "Diga un pais perteneciente al continente Europeo: ",
        'asia': "Diga un pais perteneciente al continente Asiatico: ",
        'africa': "Diga un pais perteneciente al continente Africano: ",
    }

    return random.choice(list(answers.items()))


# get the answers to quiz
def make_answers(continent):
    list_answers = []

    answer = {
        'question': "Diga el pais que pertenece",
        'choices': ['cuba', 'espana', 'peru'],
        'resp': '1',
        'user': '',
        'type': 'k_country'
    }

    answers1 = {
        'question': "Pais mas poblado del continente",
        'choices': ['rusia', 'japon', 'china'],
        'resp': '1',
        'user': '',
        'type': 'k_country'
    }

    answers2 = {
        'question': "Pais con menos poblacion del continente",
        'choices': ['rusia', 'japon', 'china'],
        'resp': '1',
        'user': '',
        'type': 'k_country'
    }

    answers3 = {
        'question': "Cual es la poblacion del pais:",
        'choices': ['3222', '58889', '45'],
        'resp': '1',
        'user': '',
        'type': 'k_country'
    }
    list_answers.append(answer)
    list_answers.append(answers1)
    list_answers.append(answers2)
    list_answers.append(answers3)

    return list_answers


# get normalize data from request
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
            find_by_country(flag_pais, True)

        if option_menu == "3":
            print("introduzca en que continente desea jugar!")
            continent = input("Contienente:")
            answers = make_answers(continent)
            random.shuffle(answers)
            for k, a in enumerate(answers):
                print(a['question'])
                for i, choice in enumerate(a['choices']):
                    print(str(i + 1) + "-" + choice)
                resp_user = input("respuesta:")
                print("".center(50, "-"))

        elif option_menu == "q":
            print("Hasta la Proxima!!!".center(40, "-"))
            break
    else:
        print("Ha seleccionado una Opcion no valida! USE ESPEJUELOS")
