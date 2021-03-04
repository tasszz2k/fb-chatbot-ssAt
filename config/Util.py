import random
import requests
import json
from flask import Flask, request
from pymessenger.bot import Bot

class Util:
    def send_get_request(url, params={}):
        response = requests.get(
            url,
            params=params)
        return response

    def get_user_by_id(user_id, access_token):
        # ----------------
        url_get_informations = "https://graph.facebook.com/{}".format(user_id)
        params = {
            'fields': 'id,name,first_name,last_name,profile_pic,locale,timezone,gender',
            'access_token': {access_token}
        }
        response = Util.send_get_request(url_get_informations, params)
        print(response.text)
        user = json.loads(response.text)
        # print(user)
        return user
        # ----------------
