import random
import telebot
from telebot import types


def rundomIntList(begin, end, number):
    intList = []
    while number > 0:
        newNumber = random.randint(begin, end)
        if newNumber in intList:
            continue
        else:
            intList.append(newNumber)
            number = number - 1
    return intList

dict = {
    "Жидомор": "Скупец, скряга",
    "Иерусалимская слеза": "Водка",
    "Канапе": "Небольшой диван с приподнятым изголовьем",
    "Комиссия": "Поручение; возня, хлопоты, заботы",
    "Косушка": "Полбутылки водки",
    "Баргузин": "Северо-восточный ветер на Байкале",}

words = ["Жидомор", "Иерусалимская слеза", "Канапе"]
meanings = ["Скупец, скряга", "Водка", "Небольшой диван с приподнятым изголовьем"]
selectedWord = "Жидомор"


def correctInDict(aDic, aKey, aValue):
    if aKey in aDic:
        return aDic.get(aKey) == aValue
    else:
        return False


API_TOKEN = '166712353:AAGQxJyriJEIvi2l4oSqMLcv1Wdhhpc8gFk'
bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):

    global selectedWord, wrongWord1, wrongWord2
    global selectedMeaning, wrongMeaning1, wrongMeaning2

    selectedWordIndexes = rundomIntList(0, len(words)-1, 3)

    selectedWord = words[selectedWordIndexes[0]]
    wrongWord1 =  words[selectedWordIndexes[1]]
    wrongWord2 = words[selectedWordIndexes[2]]

    selectedMeaning = meanings[selectedWordIndexes[0]]
    wrongMeaning1 =  meanings[selectedWordIndexes[1]]
    wrongMeaning2 = meanings[selectedWordIndexes[2]]

    markup = types.ReplyKeyboardMarkup()

    markup.row(selectedMeaning)
    markup.row(wrongMeaning1)
    markup.row(wrongMeaning2)

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
