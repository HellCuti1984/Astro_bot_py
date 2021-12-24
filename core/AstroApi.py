import requests
from jsons import jsons
from data.config import ASTRO_TOKEN


def req_json(url):
    url = f'https://astroproxy.com/api/v1/{url}&token={ASTRO_TOKEN}'
    data = requests.get(url).json()
    data_code = requests.get(url).status_code

    if data_code is 200:
        return data['data']
    else:
        return None


def get_calculate(city='Moscow', volume=100, count=1):
    if type(volume) is int:
        traffic_volume = volume / 1000
    else:
        traffic_volume = ''
    url = f'calculate?country=Russia&city={city}&network=Residental&operator=&volume={traffic_volume}&is_unlimited='
    data = req_json(url)['cost']
    return {'cost': data * count, 'count': count}


def get_balance():
    url = "balance?"
    data = req_json(url)['balance']
    return f"Ваш баланс: {data} руб."


def get_cities_from_api():
    url_req = "cities?country=Russia"
    data = req_json(url_req)
    return data


def get_cities_from_file():
    path_to_priority_cities_file = jsons.FILES['path_to_priority_cities_file']
    return jsons.read_from_file(path_to_priority_cities_file)


# region Порты

def get_ports_from_api():
    url_req = 'ports?'
    data = req_json(url_req)
    return data['ports']


def get_ports_from_file():
    path_to_ports_file = jsons.FILES['path_to_ports_file']
    return jsons.read_from_file(path_to_ports_file)

# endregion
