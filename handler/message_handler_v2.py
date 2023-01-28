import os

import openai
from unidecode import unidecode

from config import config
from handler import bot_handler
from expiringdict import ExpiringDict

MAX_LENGTH_OF_CHAT_HISTORY = 4

openai.api_key = config.OPENAI_API_KEY
OPEN_AI_MODEL = config.OPEN_AI_MODEL

# create the map(user_id, chat_history_as_list) with a timeout of 1h
chat_history_map = ExpiringDict(max_len=50, max_age_seconds=60 * 60)


def get_response_text(user, message_text):
    # Get recipient_id
    recipient_id = user["id"]

    # Start typing
    bot_handler.typing(recipient_id, 1)

    # Normalize message_text
    message_text = message_text.lower()

    # Use Chat GPT to generate response text
    response_text = handle_message(user, message_text)
    # replace all words "tôi" with "em", "bạn" with "anh" if gender is 'male', otherwise replace with "chị"
    you = "anh" if user['gender'] == 'male' else "chị"

    response_text = response_text.replace("tôi", "em").replace("Tôi", "Em").replace("bạn", you).replace("Bạn", you)

    print(">> response_text : " + response_text)
    # Stop typing
    bot_handler.typing(recipient_id, 0)
    # return selected item to the user
    return response_text


def handle_message(user, message_text):
    """
            chat_history = '''
            Q: trời lạnh nên ăn gì
            A: Trời lạnh thì bạn nên ăn các món ăn nóng như canh, phở, bún, cơm chiên, v.v. Để giúp bạn luôn ấm áp và có sức khỏe tốt hơn.
            Q: hôm nay nên ăn gì
            A:
    '''
    :param user:
    :param message_text:
    :return:
    """

    user_id = user["id"]
    chat_history_as_list = chat_history_map.get(user_id, [])

    # if the length of chat_history_as_list is greater than 4, remove from 1st to 2nd elements
    if len(chat_history_as_list) > MAX_LENGTH_OF_CHAT_HISTORY:
        chat_history_as_list = chat_history_as_list[2:]

    chat_history_as_list.append("Q: " + message_text)

    # convert chat_history_as_list to string with seperated by \n
    chat_history = "\n".join(chat_history_as_list)
    chat_history += "\nA: "
    # print(chat_history)

    response = openai.Completion.create(
        model=OPEN_AI_MODEL,
        temperature=0.5,
        prompt=chat_history,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["Q:"]
    )
    answer = response.choices[0].text.strip()
    # print(answer)
    # update chat_history and  reset the expiration time for the key
    chat_history_as_list.append("A: " + answer)
    # reset the expiration time for the key
    chat_history_map[user_id] = chat_history_as_list
    # print(chat_history_map)
    return answer
