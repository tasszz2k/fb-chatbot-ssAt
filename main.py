from unidecode import unidecode
import handler.message_handler as message_handler
import handler.bot_handler as bot_handler
from handler.scheduler import create_schedule_task_multithreading

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


message_text = 'music'

response_text = message_handler.get_response_text(user, message_text)
print(response_text)


# bot_handler.typing(user["id"], 1)
# message_handler.get_all_data(message_handler)

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