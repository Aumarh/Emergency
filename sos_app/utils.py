import string
from random import randint
import random
from twilio.rest import Client
from emergency_project import settings


def generate_user_id():
    # Random string with a combination of lower, uppercase and numbers
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(12))
    num = randint(10, 99)
    user_id = result_str + str(num)
    return user_id


def send_message(nickname, name, number2, map):
    # Send message to emergency contacts
    nickname = nickname
    name = name
    phone1 = number2
    map = map
    sid = settings.TWILIO_ACCOUNT_SID
    token = settings.TWILIO_AUTH_TOKEN
    number = "Emergency"
    client = Client(sid, token)
    message_to_send1 = f'Hello {name} your friend, {nickname} is in trouble and urgently needs your help at {map}'
    client.messages.create(to=str(phone1), from_=number, body=message_to_send1)
    return True


