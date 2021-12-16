import json
import requests
from telebot import types
from settings import ASTRO_API_TOKEN


def req_json(url=None):
    return requests.get(url).json()


def get_calculate(url):
    return str(req_json(url))


def get_balance():
    url_req = f"https://astroproxy.com/api/v1/balance?&token={ASTRO_API_TOKEN}"
    return f"Ваш баланс: {req_json(url_req)['data']['balance']}"


def get_cities():
    url_req = f"https://astroproxy.com/api/v1/cities?country=Russia&token={ASTRO_API_TOKEN}"
    return req_json(url_req)['data']
