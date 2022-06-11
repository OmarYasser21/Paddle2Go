import json
import os

from wit import Wit
from pprint import pprint

at = "TIN7JLLB6C7XBF7LQMGHUNOHYKBI2SN2"
client = Wit(access_token=at)


def get_wit_response(message_text):
    wit_response = client.message(message_text)
    pprint(wit_response)
    entity=None
    intent=None
    value=None
    try:
        entities=list(wit_response['entities'].keys())
        intent = wit_response['intents'][0]['name']
        for key in entities:
                entity=list(wit_response['entities'])[0]
                value=wit_response['entities'][key][0]['value']
    except:
        pass
    return intent, entity, value


def generate_user_response(messaging_text):
    intent,entity,value=get_wit_response(messaging_text)
    response=None

    if intent=="send_greetings":
        response="Hello, how can we serve you\n 1-Book a court\n 2-Cancel Booking\n 3-Ask for Price\n\nIf you want to end the conversation at any time press exit"

    elif intent=="Book":
        response="Pick the date of booking"

    elif intent=="pick_date":
        response="Court1:                   Court2:                 Court3:\n5pm to 7pm           6pm to 7pm        5pm to 9pm\n8pm to 9pm           9pm to 10pm\n "

    elif intent=="pick_time":
        response="The price for booking is 300\n 1-Confirm \n 2-Cancel"

    elif intent=="confirm":
        response="Your reservation ID is: A2X69B0\nThe location of your court is Hadayek El Ahram, Gate2, 20th st, 202 T"

    elif intent=="cancel_":
        response="Your booking is canceled successfully. Thank you for contacting us."

    elif intent=="cancel_booking":
        response="Please send your reservation ID"

    elif intent=="ask_price":
       response="The hourly rate is 300"

    elif intent=="exit":
        response="Thank you for contacting us"

    else:
        response="Sorry, I didn't understand your message"

    return response


