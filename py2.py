import telebot
from telebot import types

bot = telebot.TeleBot("1299068461:AAHOnyTq-qh68j2_IUsxbOtB7hyVF4EIk_8")
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
button1 = telebot.types.KeyboardButton('О компании Amway')
button2 = telebot.types.KeyboardButton('Всё о продукции Amway')
button3 = telebot.types.KeyboardButton('Программа привелегий')
button4 = telebot.types.KeyboardButton('Обучение с компанией')
button5 = telebot.types.KeyboardButton('Первые шаги')

keyboard1.row(button1)
keyboard1.row(button2)
keyboard1.row(button3)
keyboard1.row(button4)
keyboard1.row(button5)

keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2.row('Amway в мире', 'Amway в Казахстане')
backboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
backboard.row('Вернуться в меню')
itemboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
itemboard.row('Бренды на выбор', 'Вернуться в меню')
privboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
privboard.row('Возможности', 'Заработок')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я Amway bot, я здесь, чтобы помочь тебе', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'о компании amway':
        about(message)
    elif message.text.lower() == 'всё о продукции amway':
        items(message)
    elif message.text.lower() == 'о доставке':
        delivery(message)
    elif message.text.lower() == 'программа привелегий':
        priv(message)
    elif message.text.lower() == 'обучение с компанией':
        study(message)
    elif message.text.lower() == 'первые шаги':
        first(message)
    else:
        bot.send_message(message.chat.id, 'Нажмите пожалуйста на кнопку, чтобы продолжить')

def about(message):
    bot.send_photo(message.chat.id, photo())
    bot.send_message(message.chat.id,
                     'Amway — компания №1 прямых продаж в мире* и на сегодняшний день является одним из лидеров среди компаний-производителей товаров массового спроса для поддержания красоты, '
                     'здоровья и ведения домашнего хозяйства. Бизнес модель компании предполагает продажу продукта не через розничные магазины а через сеть индивидуальных дистрибьюторов которые продвигают продукт и получают вознаграждение за услуги по продвижению продукции. C компанией сотрудничают более 1 миллиона дистрибьюторов во всем мире.'
                     'Сегодня компания представлена в более 80 стран мира, штаб квартира находиться в '
                     'городе Эйда, штат Мичиган, США. '
                     'Компания Amway представлена в Казахстане с 2013 года и на сегоднешний день и является 2 самым быстро растущим рынком Amway. За 2018-2019 г компания выплатила 11,3$ млн в качестве выплат независимым предпринимателям Amway. 147 тысяч клиентов и предпринимателей Amway. '
                     '*по данным Euromonitor International за 2019г',
                     reply_markup=  keyboard2
                     )
    bot.register_next_step_handler(message, about_choice)
def about_choice(message):
    if message.text.lower() == 'amway в мире':
        history(message)
    elif message.text.lower() == 'amway в казахстане':
        now(message)
    else:
        bot.send_message(message.chat.id, 'Нажмите на кнопку')
        bot.register_next_step_handler(message, about_choice)

def history(message):
    bot.send_message(message.chat.id, 'Здесь будет история или картинка', reply_markup=backboard)

    bot.register_next_step_handler(message, back)

def now(message):
    bot.send_message(message.chat.id, 'Здесь будет о компании или картинка', reply_markup=backboard)
    bot.register_next_step_handler(message, back)

def back(message):
    if message.text.lower() == 'вернуться в меню':
        start_message(message)
    else:
        bot.send_message(message.chat.id, 'Нажмите пожалуйста на кнопку, чтобы продолжить')
        bot.register_next_step_handler(message, back)

def items(message):
    bot.send_message(message.chat.id, 'Здесь текст о продукции или картинки', reply_markup=itemboard)
    items_choice(message)

def items_choice(message):
    if message.text.lower()=="бренды на выбор":
        bot.send_message(message.chat.id, 'Здесь будут ваши бренды в виде фотографий или текста',
                         reply_markup=backboard)
        bot.register_next_step_handler(message, back)
    elif message.text.lower()=="вернуться в меню":
        bot.register_next_step_handler(message, back)
    else:
        bot.register_next_step_handler(message, items_choice)
def delivery(message):
    bot.send_message(message.chat.id, 'Здесь вся информация о доставке')
    bot.register_next_step_handler(message, back)

def priv(message):
    bot.send_message(message.chat.id, 'Выбирете вашу привелегию', reply_markup=privboard)
    bot.register_next_step_handler(message, priv_choice)

def priv_choice(message):
    if message.text.lower()=="возможности":
        bot.send_message(message.chat.id, 'Вся информация о возможностях', reply_markup=backboard)
        bot.register_next_step_handler(message, back)
    elif message.text.lower()=="заработок":
        bot.send_message(message.chat.id, 'Вся информация о заработке', reply_markup=backboard)
        bot.register_next_step_handler(message, back)
    else:
        bot.register_next_step_handler(message, priv_choice)

def study(message):
    bot.send_message(message.chat.id, 'Здесь вся инфа про обучение', reply_markup=backboard)
    bot.register_next_step_handler(message, back)

def first(message):
    bot.send_message(message.chat.id, 'Здесь вся инфа про первые шаги', reply_markup=backboard)
    bot.register_next_step_handler(message, back)


bot.polling()