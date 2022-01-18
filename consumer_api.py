import requests as req
import json


base_url = 'https://www.metaweather.com/api/location/'


# read the json file
def get_data(json_file):
    with open(json_file, encoding="utf8") as file:
        return json.load(file)


# write the json file
def write_data(json_file, data_json):
    with open(json_file, mode="w", encoding="utf8") as file:
        json.dump(data_json, file, ensure_ascii=False, indent=4)


# find weather by city
def find_weather_by_city(city, **kwargs):
    woeids = get_data("woeids.json")
    date_user = kwargs.get('date_user')
    city_url = base_url + "search/?query=" + city

    if not woeids.get(city.lower()):
        try:
            response = req.get(city_url)
            data = response.json()
        except req.exceptions.RequestException as e:
            raise SystemExit(e)
        list_woeid = get_woeid(data)
        woeids[city] = list_woeid

        # validate if find woeid to write in json file
        if len(list_woeid) > 0:
            write_data("woeids.json", woeids)
    else:
        list_woeid = woeids.get(city.lower())

    if date_user:
        cities_weather = get_weather(list_woeid, date_user=date_user)
    else:
        cities_weather = get_weather(list_woeid)

    return cities_weather


# find weather by coodenadas
def find_weather_by_coodenadas(lat, lon, **kwargs):
    date_user = kwargs.get('date_user')
    lat_lon_url = 'search/?lattlong=' + lat + ',' + lon
    response = req.get(base_url + lat_lon_url)
    cities_weather = []
    if response.status_code == 200:
        data = response.json()

        list_woeid = get_woeid(data)
        save_woeid_from_search_lattlong(data)

        if date_user:
            cities_weather = get_weather(list_woeid, date_user=date_user)
        else:
            cities_weather = get_weather(list_woeid)

    return cities_weather


# get weather from list_woeid
def get_weather(list_woeid, **kwargs):
    list_weather = []
    date_user = kwargs.get('date_user')
    for i, woeid in enumerate(list_woeid):
        try:
            response = req.get(base_url + str(woeid))
        except req.exceptions.RequestException as e:
            raise SystemExit(e)
        if date_user:
            try:
                response = req.get(base_url + str(woeid) + '/' + date_user + '/')  # if search by date
            except req.exceptions.RequestException as e:
                raise SystemExit(e)
        list_weather.append(response.json())
    return list_weather


# get list of all woeid city find
def get_woeid(data):
    woeid = []
    for i, k in enumerate(data):
        woeid.append(k['woeid'])
    return woeid


# verify if exist city and save it if exist
def verify_exist_city(city):
    woeids = get_data("woeids.json")
    city_url = base_url + "search/?query=" + city
    flag = True

    if not woeids.get(city.lower()):
        try:
            response = req.get(city_url)
            data = response.json()
        except req.exceptions.RequestException as e:
            print('City Not Found')
            return False

        list_woeid = get_woeid(data)
        woeids[city] = list_woeid

        # validate if find woeid to write in json file
        if len(list_woeid) > 0:
            write_data("woeids.json", woeids)
        else:
            flag = False

    return flag


# save woeids in json file from coords search
def save_woeid_from_search_lattlong(data):
    woeids = get_data("woeids.json")
    for i, k in enumerate(data):
        woeids[k['title'].lower()] = [k['woeid']]
    write_data("woeids.json", woeids)


# aux get coords from data city
def get_coords_woeid(data):
    location_woeid = {"latt_long": "not_found", "woied": "not_found" }
    try:
        location_woeid = {"latt_long": data[0]['latt_long'], "woied": data[0]['woeid']}
    except IndexError:
        print("ops algo ha salido mal")

    return location_woeid


# get data (latt_long and woied) from city
def get_data_from_city(city):
    woeids = get_data("woeids.json")
    city_base_url = base_url + "search/?query="

    try:
        response = req.get(city_base_url + city)
        data = response.json()
    except req.exceptions.RequestException as e:
        raise SystemExit(e)

    # validate if find woeid to write in json file
    if not woeids.get(city.lower()):
        list_woeid = get_woeid(data)
        woeids[city] = list_woeid
        if len(list_woeid) > 0:
            write_data("woeids.json", woeids)

    return get_coords_woeid(data)


# get the cities distance return a number in km
def distance_between_city(city_origin, city_destiny):
    origin_location_coords = get_data_from_city(city_origin)["latt_long"]

    distance = get_distance_from_origin(city_destiny, origin_location_coords)

    return distance/1000


# get t distance from origin coords
def get_distance_from_origin(city_destiny, location_coords):
    lat_lon_url = 'search/?lattlong=' + location_coords
    try:
        response = req.get(base_url + lat_lon_url)
        data = response.json()
    except req.exceptions.RequestException as e:
        raise SystemExit(e)
    distance = -1
    for i, k in enumerate(data):
        if k['title'].lower() == city_destiny:
            distance = k['distance']
    return distance


# estimate data depends to weather in the  origin and destiny TODO poner try catch
def estimate_data_trip(distance, destiny_woeid, origin_woeid):
    weather_destiny = get_weather([destiny_woeid])[0]['consolidated_weather'][0]
    weather_origin = get_weather([origin_woeid])[0]['consolidated_weather'][0]

    weather_state_destiny = weather_destiny['weather_state_abbr']
    weather_state_origin = weather_origin['weather_state_abbr']

    wind_speed_destiny = weather_destiny['wind_speed']
    wind_speed_origin = weather_origin['wind_speed']

    duration_trip = distance/100

    is_bad_weather = False
    if weather_state_destiny in ["sn", "sl", "h", "t", "hr"] or weather_state_origin in ["sn", "sl", "h", "t", "hr"]:
        is_bad_weather = True

    if wind_speed_destiny > 10 or wind_speed_origin:
        duration_trip = distance / 90

    result = {
        "distance": str(distance) + "km",
        "is_bad_weather": "Mal Tiempo" if is_bad_weather else "Buen Tiempo",
        "duration": str(duration_trip) + " hrs",
    }

    return result


# Estimate Trip
def estimate_trip(city_origin, city_destiny):
    estimate = {}
    if verify_exist_city(city_origin) and verify_exist_city(city_destiny):
        distance = distance_between_city(city_origin, city_destiny)

        woeid_origin = get_data_from_city(city_origin)['woied']
        woeid_destiny = get_data_from_city(city_destiny)['woied']
        estimate = estimate_data_trip(distance, woeid_destiny, woeid_origin)

    return estimate


