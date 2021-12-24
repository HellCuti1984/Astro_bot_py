import os
import json

FILES = {
    'path_to_pagination_file': os.getcwd() + "\\data\\pagination.json",
    'path_to_priority_cities_file': os.getcwd() + "\\data\\priority_cities.json",
    'path_to_ports_file': os.getcwd() + "\\data\\ports.json"
}


def read_from_file(path):
    with open(path, 'r') as json_file:
        return json.load(json_file)


def write_to_file(content, path):
    with open(path, 'w') as json_file:
        json.dump(content, json_file, indent=2)


def get_by_index(self, path, index):
    json_content = self.read_from_file(path)
    return json_content[index]


def get_by_attribute_value(self, path, attr, val):
    for json_content in self.read_from_file(path):
        if json_content[attr] == val:
            return json_content


def get_like_pages(content, get_after_index=0, limit=5):
    data = []
    content_count = len(content)
    iterator = 0

    if get_after_index is not 0:
        for i in range(get_after_index, content_count):
            data.append(content[i])
            if iterator is limit:
                return data
            else:
                iterator += 1
    else:
        for i in range(0, content_count):
            data.append(content[i])
            if iterator is limit:
                return data
            else:
                iterator += 1
