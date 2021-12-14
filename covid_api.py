import requests as req
import json
from datetime import datetime


base_url = 'https://datos.comunidad.madrid/catalogo/dataset/b3d55e40-8263-4c0b-827d-2bb23b5e7bab/resource/907a2df0-2334-4ca7-aed6-0fa199c893ad/download/covid19_tia_zonas_basicas_salud_s.json'
data = req.get(base_url).json()


# read the json file
def get_data(json_file):
    with open(json_file, encoding="utf8") as file:
        return json.load(file)


# write the json file
def write_data(json_file, data_json):
    with open(json_file, mode="w", encoding="utf8") as file:
        json.dump(data_json, file, ensure_ascii=False, indent=4)

# write_data("covid.json",data) update


# get all confirmed by month TODO add by month and day
def get_confirmed_by_month(month):
    data_list = get_data("covid.json")['data']
    all_cases = 0
    for dat in data_list:
        date_time_obj = datetime.strptime(dat['fecha_informe'], '%Y/%m/%d %H:%M:%S')
        if date_time_obj.month == month and date_time_obj.day == 7:
            all_cases += dat['casos_confirmados_totales']

    return all_cases


def get_all_data():
    return get_data("covid.json")['data']


# data array by date dict
def get_data_by_date():
    data_list = get_data("covid.json")['data']
    result = {}
    for dat in data_list:
        date_zone = dat['fecha_informe'].split(" ")[0]
        if result.get(date_zone):
            result[date_zone].append(dat)
        else:
            result[date_zone] = [dat]
    return result

