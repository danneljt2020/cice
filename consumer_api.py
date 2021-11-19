import requests as req

base_url = 'https://www.metaweather.com/api/location/'


# find weather by city
def find_weather_by_city(city):
    city_url = base_url + "search/?query=" + city
    response = req.get(city_url)
    data = response.json()
    list_woeid = get_woeid(data)
    cities_weather = get_weather(list_woeid)
    return cities_weather


# find weather by city and date
def find_weather_by_date_city(city, date):

    city_url = base_url + "search/?query=" + city
    response = req.get(city_url)

    data = response.json()
    list_woeid = get_woeid(data)
    cities_weather = get_weather(list_woeid)
    return cities_weather


# find weather by coodenadas
def find_weather_by_coodenadas(lat, lon):
    lat_lon_url = 'search/?lattlong=' + lat + ',' + lon
    response = req.get(base_url + lat_lon_url)
    data = response.json()
    list_woeid = get_woeid(data)
    cities_weather = get_weather(list_woeid)
    return cities_weather


# get weather from list_woeid
def get_weather(list_woeid):
    list_weather = []
    for i, woeid in enumerate(list_woeid):
        response = req.get(base_url + str(woeid))
        list_weather.append(response.json())
    return list_weather


# get list of all woeid city find
def get_woeid(data):
    woeid = []
    for i, k in enumerate(data):
        woeid.append(k['woeid'])
    return woeid
