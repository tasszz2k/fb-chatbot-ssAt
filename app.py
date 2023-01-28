from flask import Flask, request

import handler.bot_handler as bot_handler
import handler.message_handler_v2 as message_handler
from handler.scheduler import create_schedule_task_multithreading

# Create new schedule task to send message
create_schedule_task_multithreading()

app = Flask(__name__)  # Initializing our Flask application


# Importing standard route and two request types: GET and POST.
# We will receive messages that Facebook sends our bot at this endpoint
@app.route('/webhook', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        # Before allowing people to message your bot Facebook has implemented a verify token
        # that confirms all requests that your bot receives came from Facebook.
        token_sent = request.args.get("hub.verify_token")
        return bot_handler.verify_fb_token(token_sent)

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
                    user = bot_handler.get_user_by_id(recipient_id)
                    # print(user)
                    # ----------------
                    # if user send us any message is text
                    receive_message = message['message'].get('text')
                    if receive_message:
                        # response text here
                        response_text = message_handler.get_response_text(user, receive_message)
                        bot_handler.send_message(recipient_id, response_text)

                    # if user send us a GIF, photo, video or any other non-text item
                    elif message['message'].get('attachments'):
                        # response text here
                        print(message['message'].get('attachments'))
                        # response_text = MessageHandler.get_response_text(user, receive_message)
                        # send_message(recipient_id, response_text)
    return "Message Processed"


@app.route('/logs', methods=['GET'])
def log_chat_histories():
    logs = ">> Chat Histories: \n"
    for key, value in message_handler.chat_history_map.items():
        logs += ">>> " + key + ": " + value + "\n"
    return logs


@app.route('/', methods=['GET'])
def test():
    return "Hi, I'm ssAt!"


# Add description here about this if statement.
if __name__ == "__main__":
    app.run(port=5001)
