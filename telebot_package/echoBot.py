import random
import telebot
from telebot import types


API_TOKEN = '166712353:AAGQxJyriJEIvi2l4oSqMLcv1Wdhhpc8gFk'

bot = telebot.TeleBot(API_TOKEN)

selectedWord = "";

dic = {
    "test"                  : "Скупец, скряга",
    "Иерусалимская слеза"   : "Водка",
    "Канапе"                : "Небольшой диван с приподнятым изголовьем"}

ans =

possible_answers = ['выдающаяся хрящевая часть гортани', 'Полдень, время завтрака или раннего обеда', 'В средние века - часть обряда посвящения в рыцари',
'Термин средневековой схоластики', 'Бесцеремонное, фамильярное обращение', 'Сад, модный в XVIII в. в Англии', 'Взятка', 'Металлическая сетка, прикрепляемая к шлему, для прикрытия лица, плеч, груди',
'Бесприданница', 'Поцелуй', 'Ассигнация достоинством в 25 рублей','Женщина, живущая в монастыре, но не постриженная в монашество',
'В скандинавской мифологии - воин, обладавший сверхчеловеческой силой', 'Голень','Маленький китайский наклонный бильярд', 'Буддийский жрец в Японии и Китае',
'Пустой, дрянной человек','Извилины, кривы или ломаные линии, вычурный узор','Свободное от занятий время, каникулы',
'Беглый или отбывший наказание каторжник', 'Девы, умершие невестами, женские духи', 'Спинная струна (хорда) красной рыбы, употребляемая в пищу',
'Плетеный шнурок или тесьма', 'Французское кушанье из холодной фаршированной рыбы','Гвельфы - политические сторонники римских пап, боровшихся с императорами Священной Римской империи за власть в Италии',
'Жертвоприношение из ста быков древних греков','Гитара', 'Экипаж', 'Человеческое существо, которое, по представлениям средневековых алхимиков, можно получить искусственно',
'Сшитый из лоскутков меха, который брался из-под горла бобра, соболя или куницы',
'Молодая женщина не очень строгих правил','Монета в полкопейки','24 листа писчей бумаги','Турецкая длиннополая одежда с пуговицами на груди и узкими рукавами',
'Гусарский мундир', 'Доска, на которой сидит пряха, втыкая в нее кудель', 'Египетские девы',
'Цыганки', 'Низкорослый кустарник, малорослый, уродливый лес',
'Водка, настоянная на пахучих травах', 'Подполье, погреб', 'Популярный в начале XX в. сорт простого мыла', 'Сторублевый кредитный билет с изображением Екатерины II',
'Сандалии с толстой подошвой, которые надевали древнегреческие и древнеримские актеры для увеличения роста',
'Простенькая, наивная девушка, институтка']



dictionary = ['Жидомор', 'Иерусалимская слеза', 'Канапе','Комиссия','Косушка','Баргузин','Желтый билет',
'Жид', 'Полба', 'Сыть', 'Матица','Мир','Тарап','Требище','Тымьям','Зареть','Зой','Зень','Экипажество', 'Янычары', 'Майорат','Мечтап','Мортира','Навтика', 'Дидивин',
'Дикирий', 'Доля', 'Думные люди','Дьяк','Жеребий', 'Журфикс', 'Зазирать', 'Золотник', 'Изветник','Ифика','Канон','Войт']

rightMeaning = ['Скупец, скряга', 'Водка', 'Небольшой диван с приподнятым изголовьем',
'Поручение; возня, хлопоты, заботы','Полбутылки водки','Северо-восточный ветер на Байкале','В старой России - особый, желтого цвета, паспорт проституток',
'Клякса', 'особый сорт пшеницы', 'еда, пища', 'средняя потолочная балка','крестьянская община',
'порывистый ветер','площадка доля волхования','чебрец','гореть ярким пламенем','вопль','земля',
'оснащение кораблей', 'армейское сословие в Турции', 'порядок наследования земли старшим в семье или в роду',
'топографическая карта','пушка для навесной стрельбы','навигация', 'ученик',
'двусвещие, двойной подсвечник', 'мера веса, 44,43 мг', 'члены боярской думы',
'служитель приказа','пай, земельный надел', 'званый прием', 'осуждать',
'мера веса, около 4,3 г', 'осведомитель; соглядатай','этика','вид церковного песнопения',
'городской голова или сельский староста в Польше']







# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):



    selectedWord = ...
    markup = types.ReplyKeyboardMarkup()

    markup.row(rightMeaning[random.randint(1,20)])
    markup.row(answers[random.randint(1, 20)])
    markup.row(answers[random.randint(21, 40)])

    bot.send_message(message.chat.id, "Здорово, товарищ! Выбери правильное значение для слова: " + dictionary[random.randint(1,25)], reply_markup=markup)



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def guess_message(message):




    if message.text == dictionary()
        bot.send_message(message.chat.id, "УРА ты молодец")
    else
        bot.send_message(message.chat.id, "к сожалению неправильно :-(")

bot.polling()