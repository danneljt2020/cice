import requests as req
import json


def menu():
    print("Real weather".center(50, "-"))
    print("1. Buscar por ciudad".center(50, "-"))
    print("2. Buscar por coordenadas".center(50, "-"))
    print("3. Buscar por ciudad/coordenadas y fecha".center(50, "-"))
    print("4. Calcular viaje".center(50, "-"))
    print("Q. Para salir".center(50, "-"))


# 40.234, -3.554
'''
    La descripción del clima (soleado, nuboso y lluvioso)
    La máxima
    La mínima
    Sensación térmica
    Humedad
    Velocidad del viento y dirección
'''


def get_data(json_file):
    with open(json_file, encoding="utf8") as file:
        return json.load(file)


def write_data(data, json_file):
    with open(json_file, mode="w", encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


woeids = get_data("woeids.json")


def pretty_print(forecast):
    for k, v in forecast.items():
        print(f"{k.upper()}: {v}")


# date=2014/10/10

def get_woeid(location, **kwargs):  # coords bool, date str, limit int
    term = "query"
    woeid = woeids.get(location.lower())
    limit = kwargs.get("limit")
    if not woeid:
        if kwargs.get("coords"):
            term = "lattlong"

        url = f"https://www.metaweather.com/api/location/search/?{term}={location}"
        woeid = req.get(url).json()  # lista
        if len(woeid) >= 1:
            for loc in woeid:
                woeids[loc["title"].lower()] = loc["woeid"]
            write_data(woeids, "woeids.json")
            if limit:
                return [dic["woeid"] for dic in woeid[0:limit]]
            else:
                return [woeid[0]["woeid"]]
        else:
            return None

    return [woeid]


def get_forecast(location, **kwargs):
    woeid = get_woeid(location, **kwargs)[0]
    url = f"https://www.metaweather.com/api/location/{woeid}/"
    date = kwargs.get("date")
    if date:
        url += date
    forecast = req.get(url).json()
    if type(forecast) == list:
        if len(forecast) >= 1:
            forecast = forecast[0]
        if not len(forecast):
            return None
    # forecast = forecast["consolidated_weather"][0]
    return forecast


def calculate_trip(A, B):
    A_woeid = get_woeid(A)
    B_woeid, B_distance = None, None
    if A_woeid:
        A_woeid = A_woeid[0]
        A_coords = req.get(f"https://www.metaweather.com/api/location/{A_woeid}/").json()["latt_long"]
        des_list = req.get(f"https://www.metaweather.com/api/location/search/?lattlong={A_coords}").json()
        for des in des_list[1:]:
            if des["title"].lower() == B.lower():
                B_woeid, B_distance = des["woeid"], des["distance"]
        if B_woeid:
            A_forecast, B_forecast = get_forecast(A)["consolidated_weather"][0], \
                                     get_forecast(B)["consolidated_weather"][0]
            if A_forecast["weather_state_abbr"] in ("sn", "sl", "h", "t", "hr") or B_forecast["weather_state_abbr"] in (
            "sn", "sl", "h", "t", "hr"):
                is_bad_weather = True
            else:
                is_bad_weather = False

            wind_limit = 10
            result = {
                "A_forecast": A_forecast,
                "B_forecast": B_forecast,
                "distance": B_distance / 1000,
                "A_wind_speed": A_forecast["wind_speed"],
                "B_wind_speed": B_forecast["wind_speed"],
                "is_bad_weather": is_bad_weather
            }
            if result["A_wind_speed"] >= wind_limit or result["B_wind_speed"] >= wind_limit:
                result["time"] = result["distance"] / 90
            else:
                result["time"] = result["distance"] / 100
            return result
    else:
        return None


def forecast_v_2(location, **kwargs):  # ciudad/coords - date on - date off

    term = "query"
    woeid = woeids.get(location.lower())
    if not woeid:
        if kwargs.get("coords"):
            term = "lattlong"

        url = f"https://www.metaweather.com/api/location/search/?{term}={location}"
        woeid = req.get(url).json()
        if len(woeid) >= 1:
            for loc in woeid:
                woeids[loc["title"].lower()] = loc["woeid"]
            woeid = woeid[0]["woeid"]
            write_data(woeids, "woeids.json")
        else:
            return None

    # A partir de aquí podemos buscar por woeid:
    '''
    generar la url de llamada en base al woeid obtenido en el código anterior --> url = "weather..."
    '''
    url = f"https://www.metaweather.com/api/location/{woeid}/"
    date = kwargs.get("date")
    if date:
        url += date
    forecast = req.get(url).json()
    if type(forecast) == list:
        forecast = forecast[0]
        if not len(forecast):
            return None
    forecast = forecast["consolidated_weather"][0]

    forecast = {
        "desc": forecast["weather_state_name"],
        "max_temp": forecast["max_temp"],
        "min_temp": forecast["min_temp"],
        "st": forecast["the_temp"],
        "humidity": forecast["humidity"],
        "wind_speed_direction": f"{forecast['wind_speed']} | {forecast['wind_direction_compass']}"
    }

    return forecast


user = ""
while user != "q":
    menu()
    user = input("Opción: ")
    if user == "1":
        city = input("Ciudad: ")
        forecast_search = forecast_v_2(city)
        if forecast_search:
            print(f"La sensación térmica para {city}:")
            pretty_print(forecast_search)
        else:
            print(f"No hay pronóstico disponible para la localización: {city}")
        input("...")
    elif user == "2":
        lattlong = input("Coordenadas (latt, long): ")
        forecast_search = forecast_v_2(lattlong, coords=True)
        print(f"La sensación térmica:")
        pretty_print(forecast_search)
        input("...")
    elif user == "4":
        A = input("Desde: ")
        B = input("Hasta: ")
        trip_prediction = calculate_trip(A, B)
        if trip_prediction:
            if trip_prediction["is_bad_weather"]:
                print("¡Alerta de mal clima!")
            print(f"Temperatura en {A}: {round(trip_prediction['A_forecast']['the_temp'], 2)}")
            print(f"Temperatura en {B}: {round(trip_prediction['B_forecast']['the_temp'], 2)}")

            print(f"Distancia: {trip_prediction['distance']}")
            print(f"Tiempo estimado: {trip_prediction['time']}")

