import json

from pymessenger.bot import Bot
from flask import Flask, request

import config.util as util
import requests
import time

from config import config

ACCESS_TOKEN = config.FACEBOOK_ACCESS_TOKEN
VERIFY_TOKEN = config.FACEBOOK_VERIFY_TOKEN
bot = Bot(ACCESS_TOKEN)


# Uses PyMessenger to send response to the user
def send_message(recipient_id, response):
    # sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return {
        'status': 'success',
        'message_response': response
    }


def verify_fb_token(token_sent):
    # take token sent by Facebook and verify it matches the verify token you sent
    # if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def get_user_by_id(user_id):
    # ----------------
    url_get_informations = "https://graph.facebook.com/{}".format(user_id)
    params = {
        'fields': 'id,name,first_name,last_name,profile_pic,locale,timezone,gender',
        'access_token': {ACCESS_TOKEN}
    }
    response = util.send_get_request(url_get_informations, params)
    # print(response.text)
    user = json.loads(response.text)
    # print(user)
    return user
    # ----------------


def typing(recipient_id, action=1):
    typing_action = 'typing_on' if action else 'typing_off'
    print(typing_action)
    time.sleep(1)
    url = "https://graph.facebook.com/v2.6/me/messages";
    params = {
        'access_token': ACCESS_TOKEN
    }
    headers = {'content-type': 'application/json'}
    body = {
        'recipient': {
            'id': recipient_id
        },
        'sender_action': typing_action
    }

    response = requests.post(url, params=params, json=body)
    print(response.text)
    return json.loads(response.text)
