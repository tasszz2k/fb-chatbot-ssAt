from handler.MessageHandler import MessageHandler
from unidecode import unidecode

user = {
    'id': '4335647276450366',
    'name': 'Đinh Tuấn Anh',
    'first_name': 'Tuấn Anh',
    'last_name': 'Đinh',
    'profile_pic': 'https://platform-lookaside.fbsbx.com/platform/profilepic/?psid=4335647276450366&width=1024&ext=1617512123&hash=AeQGMdIxEE0f-VfMfrk',
    'locale': 'en_GB',
    'timezone': 7,
    'gender': 'male'
}

message_text = 'ăn gì bây giờ nhỉ'

response_text = MessageHandler.get_response_text(user, message_text)
print(response_text)

MessageHandler.get_all_data(MessageHandler)

# hello_inputs = open("data/hello/hello_input.txt", "r").read().replace(';\n', ';').split(";")
# hello_outputs = open("data/hello/hello_output.txt", "r").read().replace(';\n', ';').split(";")

# print(hello_inputs)
# print(hello_outputs)


#------------------------------------
# str = "Đinh Tuấn Anh"
#
# new_str = unidecode(str)
#
# print(str)
# print(new_str)