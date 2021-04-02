import functools
from datetime import datetime

import pytz
import schedule
import time
from threading import Thread
import threading

from handler.bot_handler import send_message

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
    # print("I'm working...")
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
    # schedule.every(60).seconds.do(lambda: job(users))

    # schedule.every(30).seconds.do(job(users))
    # schedule.every(10).minutes.do(job)
    # schedule.every().hour.do(job)
    schedule.every().day.at("08:00").do(job)
    schedule.every().day.at("12:00").do(job)
    schedule.every().day.at("13:30").do(job)
    schedule.every().day.at("21:30").do(job)
    schedule.every().day.at("23:30").do(job)

    while 1:
        schedule.run_pending()
        time.sleep(30)
    pass


def create_schedule_task_multithreading():
    thread_schedule = threading.Thread(target=schedule_task)
    thread_schedule.start()
