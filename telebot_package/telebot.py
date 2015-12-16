import telebot

from time import sleep
from math import *
from random import *

var = TeleBot("TEST")

bot = telebot.TeleBot('166712353:AAGQxJyriJEIvi2l4oSqMLcv1Wdhhpc8gFk')

max_ids = {}

while True:
    updates = bot.getUpdates()

    for u in updates:
        message = u.message
        text = message['text']
        message_id = message['message_id']
        chat_id = message['chat']['id']
        if chat_id not in max_ids or message_id > max_ids[chat_id]:
            max_ids[chat_id] = message_id
            try:
                bot.sendMessage(chat_id=chat_id, text=str(eval(text)))
            except:
                pass
    sleep(2)
