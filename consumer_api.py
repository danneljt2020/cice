import requests as req

base_url = 'https://www.metaweather.com/api/location/'


# find weather by city
def find_weather_by_city(city, **kwargs):
    date_user = kwargs.get('date_user')

    city_url = base_url + "search/?query=" + city
    response = req.get(city_url)
    data = response.json()
    list_woeid = get_woeid(data)

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
    data = response.json()
    list_woeid = get_woeid(data)

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
        response = req.get(base_url + str(woeid))
        if date_user:
            response = req.get(base_url + str(woeid) + '/' + date_user + '/')  # if search by date
        list_weather.append(response.json())
    return list_weather


# get list of all woeid city find
def get_woeid(data):
    woeid = []
    for i, k in enumerate(data):
        woeid.append(k['woeid'])
    return woeid
