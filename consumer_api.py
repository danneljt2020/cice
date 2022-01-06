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
    try:
        response = req.get(base_url + lat_lon_url)
        data = response.json()
    except req.exceptions.RequestException as e:
        raise SystemExit(e)

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


# save woeids in json file from coords search
def save_woeid_from_search_lattlong(data):
    woeids = get_data("woeids.json")
    for i, k in enumerate(data):
        woeids[k['title'].lower()] = [k['woeid']]
    write_data("woeids.json", woeids)


# get the cities distance return a number in km
def distance_between_city(city_origin, city_destiny):
    woeids = get_data("woeids.json")
    city_base_url = base_url + "search/?query="

    try:
        response = req.get(city_base_url + city_origin)
        data = response.json()
    except req.exceptions.RequestException as e:
        raise SystemExit(e)
    origin_location_coords = get_coords_woeid(data)["latt_long"]

    # validate if find woeid to write in json file
    if not woeids.get(city_origin.lower()):
        list_woeid = get_woeid(data)
        woeids[city_origin] = list_woeid
        if len(list_woeid) > 0:
            write_data("woeids.json", woeids)

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


# aux get coords from data city
def get_coords_woeid(data):
    location_woeid = {"latt_long": data[0]['latt_long'], "woied": data[0]['woeid']}
    return location_woeid


# estimate time depends to weather TODO pasale le woeid del origen y destino y distancia y listo
def estimate_data_trip(distance, destiny_woeid):
    weather = get_weather([destiny_woeid])[0]['consolidated_weather'][0]
    weather_state = weather['weather_state_abbr']
    wind_speed = weather['wind_speed']
    duration_trip = distance/100

    is_bad_weather = False
    if weather_state in ["sn", "sl", "h", "t", "hr"]:
        is_bad_weather = True

    if wind_speed > 10:
        duration_trip = distance / 90

    result = {
        "distance": str(distance) + "km",
        "is_bad_weather": "Mal Tiempo" if is_bad_weather else "Buen Tiempo",
        "duration": str(duration_trip) + " hrs",
    }

    print(result)

    return wind_speed



estimate_data_trip(550,753692)