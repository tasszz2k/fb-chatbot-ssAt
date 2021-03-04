import random
from flask import Flask, request
from pymessenger.bot import Bot
from config.Util import Util

app = Flask(__name__)  # Initializing our Flask application
ACCESS_TOKEN = open("config/access_token.txt", "r").read()
VERIFY_TOKEN = 'TASS_VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)


# Importing standard route and two request types: GET and POST.
# We will receive messages that Facebook sends our bot at this endpoint
@app.route('/', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        # Before allowing people to message your bot Facebook has implemented a verify token
        # that confirms all requests that your bot receives came from Facebook.
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)

    # If the request was not GET, it  must be POST and we can just proceed with sending a message
    # back to user
    else:
        # get whatever message a user sent the bot
        output = request.get_json()
        print(output)
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    # Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    # ----------------

                    user = Util.get_user_by_id(recipient_id, ACCESS_TOKEN)
                    print(user)
                    # ----------------

                    # if user send us any message is text
                    receive_message = message['message'].get('text')
                    if receive_message:
                        # response text here
                        response_sent_text = get_message(user, receive_message)
                        send_message(recipient_id, response_sent_text)

                    # if user send us a GIF, photo, video or any other non-text item
                    elif message['message'].get('attachments'):
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)
    return "Message Processed"


def get_message(user, message_text):
    # sample_responses = ["Hế lô, Tui là ssAt đệ anh #tass!\n ^^", "Hi, Tui là ssAt đệ anh #tass!\n:3"]
    response_message = "Chào {}, Tui là ssAt đệ anh #tass!\n ^^".format(user["first_name"])
    print(response_message + ">>" + response_message)
    # return selected item to the user
    return response_message


def verify_fb_token(token_sent):
    # take token sent by Facebook and verify it matches the verify token you sent
    # if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


# Uses PyMessenger to send response to the user
def send_message(recipient_id, response):
    # sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return {
        'status': 'success',
        'message_response': response
    }


# Add description here about this if statement.
if __name__ == "__main__":
    app.run(port=5001)
