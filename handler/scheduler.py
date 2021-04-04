import functools
from datetime import datetime

import pytz
import schedule
import time
from threading import Thread
import threading

from handler.bot_handler import send_message
from handler.message_handler import handle_quote_message

users = [{
    'id': '4335647276450366',
    'name': 'Đinh Tuấn Anh',
    'first_name': 'Tuấn Anh',
    'last_name': 'Đinh',
    'profile_pic': 'https://platform-lookaside.fbsbx.com/platform/profilepic/?psid=4335647276450366&width=1024&ext=1617512123&hash=AeQGMdIxEE0f-VfMfrk',
    'locale': 'en_GB',
    'timezone': 7,
    'gender': 'male'
}]


def job(users):
    print("I'm working...")
    for user in users:
        tz_HCM = pytz.timezone('Asia/Ho_Chi_Minh')
        now = datetime.now(tz_HCM)
        current_time = now.strftime("%H:%M:%S")
        recipient_id = user['id']
        response_text = "Bây giờ là: {}"
        response_text = response_text.format(current_time)
        print(response_text)
        send_message(recipient_id, response_text)
    # pass


def schedule_task():
    print("schedule_task()")

    schedule.every().day.at("06:00").do(lambda: wakeup(users))
    schedule.every().day.at("08:00").do(lambda: job(users))
    schedule.every().day.at("12:00").do(lambda: job(users))
    schedule.every().day.at("13:30").do(lambda: job(users))
    #
    schedule.every().day.at("12:31").do(lambda: wakeup(users))
    schedule.every().day.at("12:32").do(lambda: goodnight(users))
    schedule.every().day.at("12:33").do(lambda: wakeup(users))
    schedule.every().day.at("12:34").do(lambda: goodnight(users))
    schedule.every().day.at("12:35").do(lambda: wakeup(users))
    schedule.every().day.at("12:36").do(lambda: goodnight(users))

    schedule.every().day.at("18:30").do(lambda: job(users))
    schedule.every().day.at("21:30").do(lambda: job(users))
    schedule.every().day.at("23:30").do(lambda: goodnight(users))

    while 1:
        schedule.run_pending()
        time.sleep(20)
    pass


def create_schedule_task_multithreading():
    thread_schedule = threading.Thread(target=schedule_task)
    thread_schedule.start()


def wakeup(users):
    for user in users:
        recipient_id = user['id']
        name = user["first_name"]
        gender = user["gender"]
        gender_call = "chị" if (gender == "female") else "anh"

        message_text = '''
Trời sáng rồi,
Dậy thôi {} {} ơiii.
⏰⏰⏰
    '''
        message_text2 = handle_quote_message(user, "message_text")

        message_text = message_text.format(gender_call, name)
        print(user, message_text)
        send_message(recipient_id, message_text)
        send_message(recipient_id, message_text2)


def goodnight(users):
    for user in users:
        recipient_id = user['id']
        name = user["first_name"]
        gender = user["gender"]
        gender_call = "chị" if (gender == "female") else "anh"

        message_text1 = '''
Giờ cũng muộn rồi,
Đi ngủ thôi {0} {1} ơiii.
    '''
        message_text2 = '''
Chúc {0} ngủ ngon, mơ đẹp ạ 
💤💤💤
        '''
        message_text1 = message_text1.format(gender_call, name)
        message_text2 = message_text2.format(gender_call)
        print(user, message_text1)
        print(user, message_text2)
        send_message(recipient_id, message_text1)
        send_message(recipient_id, message_text2)
