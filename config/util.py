import json
import requests

def send_get_request(url, params={}):
    response = requests.get(
        url,
        params=params)
    return response

def get_list_from_file(src):
    element_list = open(src, "r").read().replace(';\n', ';').split(";")
    return list(filter(None, element_list))


def convertFahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return int(celsius)
