import requests as req
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


def download_flag(country, endpoint):
    response = req.get(endpoint)

    file = open("flags/", "wb")
    file.write(response.content)
    file.close()


# get country data
def get_country_data(data):
    data_result = {}
    data_result["capital"] = data[0]['capital']
    data_result["population"] = data[0]['population']
    data_result["superficie"] = data[0]['area']
    data_result["lang"] = data[0]['languages'][0]['nativeName']
    data_result["flag"] = data[0]['flags']['svg']
    return data_result
