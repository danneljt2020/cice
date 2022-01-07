import datetime as dt
import json
from flight import Flight
import random
import string

DB_aereolina = "./aereolina.json"
DB_flight = "./flight.json"


def get_json_data(json_file):
    with open(json_file, encoding="utf8") as file:
        return json.load(file)


def save_flight(data):
    with open(DB_flight, "w", encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def get_flight_by_origin(destiny):
    origin_data = get_json_data(DB_aereolina)
    flights = []
    for flight in origin_data[destiny].items():
        flights.append(flight)
    return flights[2:]


def get_all_origin():
    origin_data = get_json_data(DB_aereolina)
    destiny = []
    for d in origin_data:
        destiny.append(d)
    return destiny


utc_aux = {'ARG': -3, 'PER': -5, 'SPA': 1, 'BRA': -3}
user = ""
while user != "q":
    print("1. Comprar Vuelo")
    print("2. Modificar Vuelo")
    print("3. Cancelar Vuelo")

    user = input("Seleccione: ")
    if user == "1":
        print("Seleccione el Origen")
        for i, o in enumerate(get_all_origin()):
            print(str(i + 1) + " --> " + o)

        origin_opt = input("Seleccione: ")
        origin_selected = get_all_origin()[int(origin_opt) - 1]

        print("Paises disponibles desde el origen " + origin_selected)

        dat_destiny = get_flight_by_origin(origin_selected)
        destinys = dat_destiny[1:]
        utc = dat_destiny[0]

        for i, d in enumerate(destinys):
            print(str(i + 1) + " --> " + d[0])
        destiny_opt = input("Seleccione: ")

        flights_d = destinys[int(destiny_opt) - 1]
        departures = flights_d[1].get('departures')
        destitation = flights_d[0]
        flight_time = flights_d[1].get('flight_time')

        print("Horarios de salida " + origin_selected + " hacia " + destitation)
        for h, horary in enumerate(departures):
            print(str(h + 1) + " --> " + horary)

        horary_opt = input("Seleccione: ")

        flight_obj = Flight(destitation, origin_selected, departures[int(horary_opt) - 1], flight_time, utc)
        utc_origin = utc_aux.get(origin_selected)

        string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        letter = random.choice(string.ascii_letters)

        id_f = letter + str(random.randint(1, 50000))

        now = dt.datetime.now()
        current_time = now.strftime("%H:%M:%S %P")

        info_flight = {
            "id": id_f,
            "origin": flight_obj.origin,
            "destination": flight_obj.destination,
            "departure_hour": flight_obj.departure_hour,
            "time_flight": flight_obj.time_flight,
            "estimate_arrival": flight_obj.estimate_flight(utc_origin),
            "time_buy": current_time
        }

        flights = get_json_data("flight.json")
        flights['flights'].append(info_flight)

        save_flight(flights)

        print("Su reserva se ha registrado satisfactoriamente con identificador:", id_f)

    elif user == "2":
        print("Seleccione el identificador del boleto a modificar")

    elif user == "3":
        pass
