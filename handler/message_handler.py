import random
import json
from datetime import datetime
import urllib.parse

import config.util as util
from unidecode import unidecode

from handler import bot_handler
from handler.bot_handler import bot

# Load text from data folder
from handler.spotify_handler import get_playlist_items


hello_inputs = util.get_list_from_file("data/hello/hello_input.txt")
hello_outputs = util.get_list_from_file("data/hello/hello_output.txt")

food_inputs = util.get_list_from_file("data/food/food_input.txt")
food_outputs = util.get_list_from_file("data/food/food_output.txt")

quote_inputs = util.get_list_from_file("data/quote/quote_input.txt")
quote_outputs = util.get_list_from_file("data/quote/quote_output.txt")

weather_inputs = util.get_list_from_file("data/weather/weather_input.txt")
weather_outputs = util.get_list_from_file("data/weather/weather_output.txt")

number_inputs = util.get_list_from_file("data/number/number_input.txt")
number_outputs = util.get_list_from_file("data/number/number_output.txt")

music_inputs = util.get_list_from_file("data/music/music_input.txt")
music_outputs = util.get_list_from_file("data/music/music_output.txt")


def get_response_text(user, message_text):
    # Get recipient_id
    recipient_id = user["id"]

    # Start typing
    bot_handler.typing(recipient_id, 1)

    # Normalize message_text
    message_text = unidecode(message_text).lower()
    response_text = None

    # Hello
    if check_string_contains_an_element_of_list(message_text, hello_inputs):
        response_text = handle_hello_message(user, message_text)
    # Food
    elif check_string_contains_an_element_of_list(message_text, food_inputs):
        response_text = handle_food_message(user, message_text)
    # Quote
    elif check_string_contains_an_element_of_list(message_text, quote_inputs):
        response_text = handle_quote_message(user, message_text)
    # Weather
    elif check_string_contains_an_element_of_list(message_text, weather_inputs):
        response_text = handle_weather_message(user, message_text)
    # Number
    elif check_string_contains_an_element_of_list(message_text, number_inputs):
        response_text = handle_number_message(user, message_text)
    # Music
    elif check_string_contains_an_element_of_list(message_text, music_inputs):
        response_text = handle_music_message(user, message_text)
    else:
        response_text = handle_not_match_any_message(user)
    print(">> response_text : " + response_text)
    # Stop typing
    bot_handler.typing(recipient_id, 0)
    # return selected item to the user
    return response_text


def handle_hello_message(user, message_text):
    '''
        - Handle Hello Message
        @param user: User sending the message
        @Param message_text: content of the message
    '''
    name = user["first_name"]
    gender = user["gender"]
    now = datetime.now()
    response_text = "hello"
    hello_str = "Chào {} {}, em là ssAt - đệ anh Tuấn Anh ạ!\n^^"

    # check gender
    if gender == 'male':
        # gender is male
        response_text = hello_str.format("anh", name)
    else:
        # gender is female
        response_text = hello_str.format("chị", name)

    return response_text


def handle_food_message(user, message_text):
    '''
        - Handle Food Message
        @param user: User sending the message
        @Param message_text: content of the message
    '''
    name = user["first_name"]
    gender = user["gender"]
    gender_call = "chị" if (gender == "female") else "anh"
    now = datetime.now()
    response_text = "food"
    food_str = "Bữa nay ăn '{}' là hợp lý {} {} ạ!\n🥗🥗🥗\nCông thức nấu ăn: \nhttps://cookpad.com/vn/tim-kiem/{} "

    food = random.choice(food_outputs)

    response_text = food_str.format(food, gender_call, name, urllib.parse.quote(food))

    return response_text


def handle_quote_message(user, message_text):
    quote_url = "https://quotes.rest/qod?language=en"
    response = util.send_get_request(quote_url)
    response_text = "Quote"
    quote_str = "Quote of the day: 💬 \"{}\" 💬"
    # print(response.text)
    data_json = json.loads(response.text)
    quotes = data_json['contents']['quotes']
    quote = quotes[0]['quote']
    response_text = quote_str.format(quote)
    return response_text


def handle_not_match_any_message(user):
    '''
        - Handle Not Match Any Message
        @param user: User sending the message
        @Param message_text: content of the message
    '''
    name = user["first_name"]
    gender = user["gender"]
    now = datetime.now()
    response_text = "None"
    sorry_str = "Xin lỗi {} {}, em học bài chưa kĩ, em sẽ về bảo sư phụ dạy thêm ạ!\n😢"

    # check gender
    if gender == 'male':
        # gender is male
        response_text = sorry_str.format("anh", name)
    else:
        # gender is female
        response_text = sorry_str.format("chị", name)

    return response_text


def handle_weather_message(user, message_text):
    APP_ID_OPENWEATHERMAP = 'eda5d9eb59ecde1880816e988e56c122'
    openweathermap_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': 'hanoi',
        'units': 'metric',
        'appid': {APP_ID_OPENWEATHERMAP}
    }
    response = util.send_get_request(openweathermap_url, params)
    city = "Hanoi"
    response_text = "Weather"
    weather_str = '''Current weather in {} and forecast for today: 
    ❄❄❄
- Main: {},
- Description: {},
- Temperature: {}°C,
- Min Temperature: {}°C 
- Max Temperature: {}°C
'''
    weather_icon_url = "http://openweathermap.org/img/w/{}.png"
    print(response.text)
    data_json = json.loads(response.text)
    weather = data_json["weather"][0]
    main = data_json["main"]
    print(type(main["temp"]))
    response_text = weather_str.format(city, weather["main"], weather["description"],
                                       main["temp"],
                                       main["temp_min"],
                                       main["temp_max"])
    # Send weather source and icon
    bot.send_image_url(user["id"], weather_icon_url.format(weather["icon"]))
    return response_text


def handle_number_message(user, message_text, min=0, max=99):
    num = random.randint(min, max)
    response_text = "Number"
    number_str = "Con số may mắn: 🌀 {} 🌀"

    response_text = number_str.format(num)
    return response_text


def handle_music_message(user, message_text):
    name = user["first_name"]
    gender = user["gender"]
    gender_call = "chị" if (gender == "female") else "anh"
    playlist_items = get_playlist_items()
    num = random.randint(0, len(playlist_items) - 1)
    response_text = "Music"
    music_str = '''
Nay nghe bài này đi {} {} ơi:
️🎶️🎶️🎶
'{}' - {}
️🎶️🎶️🎶
Link spotify nè: {}'''

    response_text = music_str.format(gender_call, name, playlist_items[num]['name'], playlist_items[num]['artists'], playlist_items[num]['spotify'])
    return response_text


def check_string_contains_an_element_of_list(str, list):
    # print(any(element in str for element in list))
    return any(element in str for element in list)


def get_all_data(self):
    print(self.hello_inputs)
    print(self.hello_outputs)
    print(self.food_inputs)
    print(self.food_outputs)
    print(self.weather_inputs)
    print(self.weather_outputs)
    print(self.music_inputs)
    print(self.music_outputs)
