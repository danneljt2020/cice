import requests as req
import threading

base_url = 'https://restcountries.com/v3.1/all'


# get all flags
def get_all_flags():
    list_flag = []
    response = req.get(base_url)
    data_response = response.json()
    for f in data_response:
        list_flag.append(f['flags']['png'])
    return list_flag


# Download flag country
def save_flag(endpoint):
    name = endpoint[-6:-4]
    response = req.get(endpoint)
    file = open("flags/flag_" + name + ".png", "wb")
    file.write(response.content)
    file.close()


def download_flag():
    flags = get_all_flags()
    for endpoint in flags:
        t1 = threading.Thread(target=save_flag, args=(endpoint,))
        t1.start()


download_flag()



