import os

from core import jsons

path_to_priority_cities_file = os.getcwd() + "\\data\\priority_cities.json"
path_to_all_cities_list = os.getcwd() + "\\data\\all_priority_cities.json"

IS_CHECKING_BY_TIMER = False


def check_city_in_priority_list(city):
    pr_cities_list = jsons.read_from_file(path_to_priority_cities_file)

    if pr_cities_list is None:
        return False
    else:
        for pr_city in pr_cities_list:
            if pr_city['name'] == city:
                return True

    return False


def add_remove_pr_cities(city):
    cities_list = jsons.read_from_file(path_to_priority_cities_file)

    if check_city_in_priority_list(city):
        cities_list.remove({'name': city})
    else:
        cities_list.append({'name': city})

    jsons.write_to_file(cities_list, path_to_priority_cities_file)
