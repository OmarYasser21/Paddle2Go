import os, sys
from flask import Flask, request
import json
from pymessenger import Bot
from pprint import pprint
from Utils import generate_user_response


PAGE_ACCESS_TOKEN = "EAAQkU3rFmEgBAJUEqfRzwL2T6hnVSFGZAD9B4SCkZCuFjDQH2ok6ltZAX4G5TRy8fcjoj0jXb90zgDV9MNTqG6jVJfkQlqWByGWwKbbzXqIJZCbv72QVYRqJxOxnkiibDm62b74tZAKGyt9sF8BNpjxUzAlhsAEHCVadcyw7xDucwoUL61y9A"
bot = Bot(PAGE_ACCESS_TOKEN)


app = Flask(__name__)
VERIFICATION_TOKEN = "hello"


@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back# the 'hub.challenge' value it receives in the query arguments

    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get(
                "hub.verify_token") == VERIFICATION_TOKEN:  # you can replace VERIFICATION_TOKEN with os.environ["VERIFY_TOKEN"]
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello-world", 200



@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    printmsg(data)
    process_data(data)
    return "okk", 200



def process_data(data):
# Check if value corresponding to object key is "page"
    if data["object"] == "page":
 # loop on the list corresponding to entry key
     for entry in data["entry"]:
 # loop on the list corresponding to the messaging key
       for messaging_event in entry["messaging"]:
 # access the message event:
    # (1) get sender and recipient IDs
            sender_id = messaging_event["sender"]["id"]
            recipient_id = messaging_event["recipient"]["id"]
    # (2) check message type is simple message type
            if messaging_event.get("message"):
                if "text" in messaging_event["message"]:
                    messaging_text = messaging_event["message"]["text"]
                # there is text key
                else:
                    messaging_text = "no text"
                printmsg(messaging_text)
                response=generate_user_response(messaging_text)
                bot.send_text_message(sender_id, response)



def printmsg(msg):
    print(msg)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(debug=True, port=80)



