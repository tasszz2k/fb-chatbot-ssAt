import requests
from unidecode import unidecode


def send_get_request(url, params={}):
    response = requests.get(
        url,
        params=params)
    return response

def get_list_from_file(src):
    element_list = open(src, "r").read().split('\n')
    return list(filter(None, element_list))


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return int(celsius)

def find_elements_by_keyword(list, keyword):
    new_list = []
    for element in list:
        # if keyword in unidecode(element).lower():
        if contains_word(unidecode(element).lower(), keyword):
            new_list.append(element)
    return new_list

def contains_word(s, w):
    return f' {w} ' in f' {s} '