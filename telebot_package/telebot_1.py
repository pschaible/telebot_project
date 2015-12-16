from time import sleep
from math import *
from random import *
import time

import telebot


bot = telebot.TeleBot('166712353:AAGQxJyriJEIvi2l4oSqMLcv1Wdhhpc8gFk')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    # Если функция возвращает None -> Человек не в игре
    answer = utils.get_answer_for_user(message.chat.id)
    # Как Вы помните, answer может быть либо текст, либо None
    # Если None:
    if not answer:
        bot.send_message(message.chat.id, 'Чтобы начать игру, выберите команду /game')
    else:
       bot.send_message(message.chat.id, 'Верно!')



if __name__ == '__main__':
    utils.count_rows()
    random.seed()
    bot.polling(none_stop=True)