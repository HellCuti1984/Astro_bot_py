import time

import requests
from core import jsons
from core.market import market
from config import ASTRO_TOKEN


def get_astro_url(url):
    return f'https://astroproxy.com/api/v1/{url}&token={ASTRO_TOKEN}'


def post_json(url):
    url = get_astro_url(url)
    data = requests.post(url).json()
    return data


def get_json(url):
    url = get_astro_url(url)
    data = requests.get(url).json()
    data_code = 0
    if data['status'] == 'ok':
        data_code = 200

    if data_code is 200:
        return data['data']
    else:
        return None


def delete_req(url):
    url = get_astro_url(url)
    data = requests.delete(url).json()
    return data


def patch_req(url):
    url = get_astro_url(url)
    data = requests.patch(url).json()
    return data


def get_calculate(city='Moscow', volume=100, count=1):
    if type(volume) is int:
        traffic_volume = volume / 1000
    else:
        traffic_volume = ''
    url = f'calculate?country=Russia&city={city}&network=Residential&operator=&volume={traffic_volume}&is_unlimited='
    port_cost = 15
    traffic_cost = round(get_json(url)['cost'] - port_cost, 2)
    port_and_traffic = round(port_cost + traffic_cost, 2)
    return {'port_cost': port_cost, 'traffic_cost': traffic_cost * count, 'port_and_traffic': port_and_traffic,
            'count': count}


def get_balance():
    url = "balance?"
    data = get_json(url)['balance']
    return f"Ваш баланс: {data} руб."


def get_cities_from_api():
    url_req = "cities?&country=Russia"
    data = get_json(url_req)
    return data


def get_cities_from_file():
    path_to_priority_cities_file = jsons.FILES['path_to_priority_cities_file']
    return jsons.read_from_file(path_to_priority_cities_file)


# region Порты

def get_ports_from_api():
    url_req = 'ports?tab=all'
    data = get_json(url_req)
    return data['ports']


def get_ports_from_file():
    path_to_ports_file = jsons.FILES['path_to_ports_file']
    return jsons.read_from_file(path_to_ports_file)


def get_archived_ports():
    url_req = 'ports?tab=archived'
    data = get_json(url_req)
    return data['ports']


def update_port_file():
    path_to_priority_cities_file = jsons.FILES['path_to_ports_file']
    cities = get_ports_from_api()
    jsons.write_to_file(cities, path_to_priority_cities_file)


def post_create_port(name='',
                     network='Residential',
                     country='Russia',
                     city='',
                     volume='0.1',
                     username='hellcatrb1476',
                     password='616138'):
    url = f'ports?name={name}&network={network}&country={country}&city={city}&rotation_by=time&rotation_time_type=hours' \
          f'&rotation_time=1&is_unlimited=0&volume={volume}&username={username}&password={password}'

    is_ok = False
    for i in range(int(market.COUNT)):
        status = post_json(url)['status']
        if status != 'ok':
            is_ok = False
        else:
            is_ok = True
        time.sleep(1)
    return is_ok



def post_renew_port(id):
    url = f'ports/{id}/renew?volume=0.1'
    return post_json(url)


def delete_port(id):
    url = f'ports/{id}?'
    return delete_req(url)
# endregion
