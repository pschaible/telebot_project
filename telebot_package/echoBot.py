import random
import telebot
from telebot import types


dict = {
    "Жидомор"               :   "Скупец, скряга",
    "Иерусалимская слеза"   :   "Водка",
    "Канапе"                :   "Небольшой диван с приподнятым изголовьем",
    "Комиссия"              :   "Поручение; возня, хлопоты, заботы",
    "Косушка"               :   "Полбутылки водки",
    "Баргузин"              :   "Северо-восточный ветер на Байкале",}


words = ["Жидомор", "Иерусалимская слеза","Канапе"]
meanings = ["Скупец, скряга", "Водка", "Небольшой диван с приподнятым изголовьем"]
selectedWord = "Жидомор"


def correctInDict(aDic, aKey, aValue) :
    if aKey in aDic :
        return aDic.get(aKey) == aValue
    else:
        return False

API_TOKEN = '166712353:AAGQxJyriJEIvi2l4oSqMLcv1Wdhhpc8gFk'
bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):


    global selectedWord
    selectedWord= words[random.randint(0,len(words)-1)]

    markup = types.ReplyKeyboardMarkup()
    markup.row(dir(selectedWord))
    markup.row(meanings[random.randint(0,len(meanings)-1)])
    markup.row(meanings[random.randint(0,len(meanings)-1)])

    bot.send_message(message.chat.id, "Здорово, товарищ! Выбери правильное значение для слова: "
                     + selectedWord, reply_markup=markup)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def guess_message(message):

    if correctInDict(dict, selectedWord, message.text):
        bot.send_message(message.chat.id, "УРА .. ты молодец")
    else:
        bot.send_message(message.chat.id, " .. к сожалению неправильно :-(")

bot.polling()