import requests as req
import random
import json

base_url = 'https://restcountries.com/v2/'


# read the json file
def get_data(json_file):
    with open(json_file, encoding="utf8") as file:
        return json.load(file)


# write the json file
def write_data(json_file, data_json):
    with open(json_file, mode="w", encoding="utf8") as file:
        json.dump(data_json, file, ensure_ascii=False, indent=4)


# find country or download flag by city
def find_by_country(country, download=None):
    countrys_json = get_data("country.json")
    country_url = base_url + "name/" + country

    if not countrys_json.get(country.lower()):
        try:
            response = req.get(country_url)
            data_response = response.json()
            country_data_result = get_country_data(data_response)
        except req.exceptions.RequestException as e:
            raise SystemExit(e)
    else:
        country_data_result = countrys_json.get(country.lower())
    if download:
        download_flag(country, country_data_result["flag"])

    return country_data_result


# Download flag country
def download_flag(country, endpoint):
    response = req.get(endpoint)

    file = open("flags/flag_" + country + ".svg", "wb")
    file.write(response.content)
    file.close()


# get country data
def get_country_data(data):
    data_result = {}
    data_result["capital"] = data[0]['capital']
    data_result["population"] = data[0]['population']
    data_result["superficie"] = data[0]['area']
    data_result["lang"] = data[0]['languages'][0]['nativeName']
    data_result["flag"] = data[0]['flag']
    data_result["region"] = data[0]['region']
    data_result["calling_code"] = data[0]['callingCodes']  # list of codes
    return data_result


# get random country for ask
def get_random_country():
    all_countrys = get_data("all_country.json")
    list_country = all_countrys['countrys']
    return random.choice(list_country)


def verify_answer(country, key_answer, resp):
    flag = False
    data_country = find_by_country(country)

    if key_answer not in ['europe', 'africa', 'asia']:
        if key_answer == "calling_code":  #list of codes
            if resp in data_country[key_answer]:
                flag = True

        if data_country[key_answer] == resp:
            flag = True

    if key_answer == "europe":
        country_europe = get_country_by_continent("europe")
        if resp.lower() in country_europe:
            flag = True

    if key_answer == "asia":
        country_asia = get_country_by_continent("asia")
        if resp.lower() in country_asia:
            flag = True

    if key_answer == "africa":
        country_africa = get_country_by_continent("africa")
        if resp.lower() in country_africa:
            flag = True

    return flag


# get all country data from contiennt
def get_country_data_continent(data):
    data_result = []
    for country in data:
        data_result.append(country['name'].lower())
    return data_result


# get all countrys  by contiennt json
def get_country_by_continent(continent):
    url_cont = "https://restcountries.com/v2/region/"+continent
    try:
        response = req.get(url_cont)
        data_response = response.json()
        country_data_result = get_country_data_continent(data_response)
    except req.exceptions.RequestException as e:
        raise SystemExit(e)

    return country_data_result



# print(get_country_by_continent("europe"))

# response = req.get("https://restcountries.com/v2/all")
# data_response = response.json()
# list_all_countrys = {'countrys': []}
# list = []
# for d in data_response:
#     list.append(d['name'])
# list_all_countrys['countrys'] = list
# write_data("all_country.json", list_all_countrys)
