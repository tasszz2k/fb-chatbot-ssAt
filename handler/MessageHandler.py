from datetime import datetime
import random
from flask import Flask, request
from pymessenger.bot import Bot

from app import ACCESS_TOKEN, app, bot
from config.Util import Util

class MessageHandler:

    def get_response_text(user, message_text):
        name = user["first_name"]
        gender = user["gender"]
        now = datetime.now()
        response_text = ""
        hello_str = "Em chào {} {} ạ, em là ssAt -  đệ anh Tuấn Anh!\n^^"

        # check gender
        if (gender == 'male'):
            # gender is male
            response_text = hello_str.format("anh", name)
        else:
            # gender is female
            response_text = hello_str.format("chị", name)

        # sample_responses = ["Hế lô, Tui là ssAt đệ anh #tass!\n ^^", "Hi, Tui là ssAt đệ anh #tass!\n:3"]
        # response_text = "Chào {}, Tui là ssAt đệ anh #tass!\n ^^".format(user["first_name"])
        print(response_text + ">>" + response_text)
        # return selected item to the user
        return response_text