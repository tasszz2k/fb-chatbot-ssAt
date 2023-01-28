import handler.message_handler_v2 as message_handler

user_1 = {
    'id': '4335647276450366',
    'name': 'Đinh Tuấn Anh',
    'first_name': 'Tuấn Anh',
    'last_name': 'Đinh',
    'profile_pic': 'https://platform-lookaside.fbsbx.com/platform/profilepic/?psid=4335647276450366&width=1024&ext=1617512123&hash=AeQGMdIxEE0f-VfMfrk',
    'locale': 'en_GB',
    'timezone': 7,
    'gender': 'male'
}
user_2 = {
    'id': '22222222',
    'name': 'Đinh Tuấn Anh',
    'first_name': 'Tuấn Anh',
    'last_name': 'Đinh',
    'profile_pic': 'https://platform-lookaside.fbsbx.com/platform/profilepic/?psid=4335647276450366&width=1024&ext=1617512123&hash=AeQGMdIxEE0f-VfMfrk',
    'locale': 'en_GB',
    'timezone': 7,
    'gender': 'male'
}



message_handler.handle_message(user_1, "trời lạnh nên ăn gì")
message_handler.handle_message(user_1, "có nên ăn kem vào mùa đông không?")
message_handler.handle_message(user_1, "ăn kem vị gì ngon nhất")
message_handler.handle_message(user_1, "ngoài kem ra có món gì ngon không")



