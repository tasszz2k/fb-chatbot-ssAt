import random
import json
from datetime import datetime
from config.Util import Util
from unidecode import unidecode


class MessageHandler:
    # Load text from data folder
    hello_inputs = Util.get_list_from_file("data/hello/hello_input.txt")
    hello_outputs = Util.get_list_from_file("data/hello/hello_output.txt")

    food_inputs = Util.get_list_from_file("data/food/food_input.txt")
    food_outputs = Util.get_list_from_file("data/food/food_output.txt")

    quote_inputs = Util.get_list_from_file("data/quote/quote_input.txt")
    quote_outputs = Util.get_list_from_file("data/quote/quote_output.txt")

    weather_inputs = Util.get_list_from_file("data/weather/weather_input.txt")
    weather_outputs = Util.get_list_from_file("data/weather/weather_output.txt")

    def get_response_text(user, message_text):
        message_text = unidecode(message_text).lower()
        response_text = None

        # Hello
        if MessageHandler.check_string_contains_an_element_of_list(message_text, MessageHandler.hello_inputs):
            response_text = MessageHandler.handle_hello_message(user, message_text)
        # Food
        elif MessageHandler.check_string_contains_an_element_of_list(message_text, MessageHandler.food_inputs):
            response_text = MessageHandler.handle_food_message(user, message_text)
        # Quote
        elif MessageHandler.check_string_contains_an_element_of_list(message_text, MessageHandler.quote_inputs):
            response_text = MessageHandler.handle_quote_message(user, message_text)
        # Weather
        elif MessageHandler.check_string_contains_an_element_of_list(message_text, MessageHandler.weather_inputs):
            response_text = MessageHandler.handle_weather_message(user, message_text)
        else:
            response_text = MessageHandler.handle_not_match_any_message(user)
        print(">> response_text : " + response_text)
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
        now = datetime.now()
        response_text = "food"
        food_str = "Bữa nay ăn {} là hợp lý {} {} ạ!\n^^"

        food = random.choice(MessageHandler.food_outputs)

        # check gender
        if gender == 'male':
            # gender is male
            response_text = food_str.format(food, "anh", name)
        else:
            # gender is female
            response_text = food_str.format(food, "chị", name)

        return response_text

    def handle_quote_message(user, message_text):
        quote_url = "https://quotes.rest/qod?language=en"
        response = Util.send_get_request(quote_url)
        response_text = "Quote"
        quote_str = "Quote of the day: \"{}\""
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
            'appid': {APP_ID_OPENWEATHERMAP}
        }
        response = Util.send_get_request(openweathermap_url, params)
        city = "Hanoi"
        response_text = "Weather"
        weather_str = '''Current weather in {} and forecast for today: 
- Main: {},
- Description: {},
- Temperature: {},
- MinTemperature: {} - MaxTemperature: {}
source: http://openweathermap.org/img/w/{}.png
'''
        print(response.text)
        data_json = json.loads(response.text)
        weather = data_json["weather"][0]
        main = data_json["main"]
        print(type(main["temp"]))
        response_text = weather_str.format(city, weather["main"], weather["description"],
                                           Util.convertFahrenheitToCelsius(main["temp"]),
                                           Util.convertFahrenheitToCelsius(main["temp_min"]),
                                           Util.convertFahrenheitToCelsius(main["temp_max"]),
                                           weather["icon"])
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