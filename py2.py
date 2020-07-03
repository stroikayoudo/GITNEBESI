#-*-coding: utf-8 -*-
import telebot
from telebot import types
import kz

bot = telebot.TeleBot("1299068461:AAHOnyTq-qh68j2_IUsxbOtB7hyVF4EIk_8")
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
button1 = telebot.types.KeyboardButton('О компании Amway')
button2 = telebot.types.KeyboardButton('Всё о продукции Amway')
button3 = telebot.types.KeyboardButton('Как купить?')
button4 = telebot.types.KeyboardButton('Гарантия качества Amway')
button5 = telebot.types.KeyboardButton('Програма привилегий для VIP+')
button6 = telebot.types.KeyboardButton('Вознаграждения для Независимого предпринимателя Amway')

keyboard1.row(button1)
keyboard1.row(button2)
keyboard1.row(button3)
keyboard1.row(button4)
keyboard1.row(button5)
keyboard1.row(button6)

keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2.row('Amway в мире', 'Amway в Казахстане', 'Миссия Amway')
backboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
backboard.row('Вернуться в меню')

item1 = telebot.types.KeyboardButton('Здоровье')
item2 = telebot.types.KeyboardButton('Красота')
item3 = telebot.types.KeyboardButton('Уход за телом')
item4 = telebot.types.KeyboardButton('Дом')
item5 = telebot.types.KeyboardButton('Вернуться в меню')

itemboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
itemboard.row(item1)
itemboard.row(item2)
itemboard.row(item3)
itemboard.row(item4)
itemboard.row(item5)

privboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
privboard.row('Возможности', 'Заработок')


cityitem1 = telebot.types.KeyboardButton('Алматы')
cityitem2 = telebot.types.KeyboardButton('Нурсултан')
cityitem3 = telebot.types.KeyboardButton('Караганда')
cityitem4 = telebot.types.KeyboardButton('Шымкент')
cityitem5 = telebot.types.KeyboardButton('Актау')

cityboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
cityboard.row(cityitem1)
cityboard.row(cityitem2)
cityboard.row(cityitem3)
cityboard.row(cityitem4)
cityboard.row(cityitem5)

langitem1 = telebot.types.KeyboardButton('Русский')
langitem2 = telebot.types.KeyboardButton('Қазақ')

langboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
langboard.row(langitem1)
langboard.row(langitem2)


@bot.message_handler(commands=['start'])

def language(message):
    bot.send_message(message.chat.id, 'Тілді таңдаңыз\nВыберите язык', reply_markup=langboard)
    bot.register_next_step_handler(message, language_choice)

def language_choice(message):
    if message.text.lower() == 'қазақ':
        kz_city(message)
    elif message.text.lower() == 'русский':
        start_message(message)
    else:
        bot.send_message(message.chat.id, 'Нажмите пожалуйста на кнопку, чтобы продолжить')

@bot.message_handler(content_types=['text'])
def city(message):
    bot.send_message(message.chat.id, 'Привет, я Amway bot, выбери город для новостей', reply_markup=cityboard)
    bot.register_next_step_handler(message, city_choice)

def city_choice(message):
    if message.text.lower() == 'алматы':
        start_message(message)
    elif message.text.lower() == 'нурсултан':
        start_message(message)
    elif message.text.lower() == 'караганда':
        start_message(message)
    elif message.text.lower() == 'шымкент':
        start_message(message)
    elif message.text.lower() == 'актау':
        start_message(message)
    else:
        bot.send_message(message.chat.id, 'Нажмите пожалуйста на кнопку, чтобы продолжить')

def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я Amway bot, я здесь, чтобы помочь тебе', reply_markup=keyboard1)
    bot.register_next_step_handler(message, send_text)

def send_text(message):
    if message.text.lower() == 'о компании amway':
        about(message)
    elif message.text.lower() == 'всё о продукции amway':
        items(message)
    elif message.text.lower() == 'как купить?':
        delivery(message)
    elif message.text.lower() == 'гарантия качества amway':
        guarantee(message)
    elif message.text.lower() == 'програма привилегий для vip+':
        study(message)
    elif message.text.lower() == 'вознаграждения для Независимого предпринимателя amway ':
        first(message)
    else:
        bot.send_message(message.chat.id, 'Нажмите пожалуйста на кнопку, чтобы продолжить')

def about(message):
    bot.send_photo(message.chat.id, photo=open('0.png','rb'))
    bot.send_message(message.chat.id,
                    'Amway — компания №1 прямых продаж в мире* и на сегодняшний день является одним из лидеров среди компаний-производителей товаров массового спроса для поддержания красоты, здоровья и ведения домашнего хозяйства. Бизнес-модель компании предполагает продажу продукта не через розничные магазины, а через сеть индивидуальных дистрибьюторов, которые продвигают продукт и получают вознаграждение за услуги по продвижению продукции. '
'С компанией сотрудничают более 1 миллиона дистрибьюторов во всем мире.'
'Сегодня компания представлена в более чем 80 странах мира, штаб квартира находится в городе Эйда, штат Мичиган, США. '

'Компания Amway представлена в Казахстане с 2013 года и на сегодняшний день  является 2-м самым быстро растущим рынком Amway. За 2018-2019 г компания выплатила 11,3$ млн в качестве выплат независимым предпринимателям Amway, 147 тысячам клиентов и предпринимателям Amway. '
' *по данным Euromonitor International за 2019г', reply_markup =  keyboard2
                     )

    bot.register_next_step_handler(message, about_choice)


def about_choice(message):
    if message.text.lower() == 'amway в мире':
        history(message)
    elif message.text.lower() == 'amway в казахстане':
        now(message)
    elif message.text.lower() == 'миссия amway':
        mis(message)
    else:
        bot.send_message(message.chat.id, 'Нажмите на кнопку')
        bot.register_next_step_handler(message, about_choice)

def history(message):
    bot.send_photo(message.chat.id, photo=open('1.png','rb'))
    url1(message)
    bot.send_message(message.chat.id, "Вернуться на главную?", reply_markup=backboard)
    bot.register_next_step_handler(message, back)

def url1(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/about-amway-new/globally')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Прочитайте здесь", reply_markup = markup)

def now(message):
    bot.send_photo(message.chat.id, photo=open('2.png','rb'))
    url2(message)
    bot.send_message(message.chat.id, "Вернуться на главную?", reply_markup=backboard)
    bot.register_next_step_handler(message, back)

def url2(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/about-amway-new/in-kazakhstan')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Прочитайте здесь", reply_markup = markup)

def mis(message):
    bot.send_photo(message.chat.id, photo=open('0.png','rb'))
    bot.send_message(message.chat.id, 'С самого момента основания Amway верна своей миссии — помогать людям жить лучше и проще. Мы гарантируем сервис высокого уровня как для потребителей, так и для бизнес-партнёров.'
    , reply_markup=backboard)
    bot.register_next_step_handler(message, back)


def back(message):
    if message.text.lower() == 'вернуться в меню':
        start_message(message)
    else:
        bot.send_message(message.chat.id, 'Нажмите пожалуйста на кнопку, чтобы продолжить')
        bot.register_next_step_handler(message, back)

def items(message):
    bot.send_photo(message.chat.id, photo=open('15.png','rb'))
    bot.send_message(message.chat.id, 'Познакомьтесь с брендами компании Amway и ассортиментом товаров для красоты, здоровья и ухода за домом.'
    , reply_markup=itemboard)
    items_choice(message)

def items_choice(message):
    if message.text.lower()=="здоровье":
        health(message)
    elif message.text.lower()=="красота":
        beauty(message)
    elif message.text.lower()=="дом":
        home(message)
    elif message.text.lower()=="уход за телом":
        body(message)
    elif message.text.lower()=="вернуться в меню":
        bot.register_next_step_handler(message, back)
    else:
        bot.register_next_step_handler(message, items_choice)

def health(message):
    healthboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    healthboard.row('Nutrilite', 'TRUVIVITY', 'XS')
    bot.send_message(message.chat.id,"Выбирите интересующий вас товар", reply_markup=healthboard)
    health_choice(message)

def health_choice(message):
    if message.text.lower()=="nutrilite":
        nutrilite(message)
    elif message.text.lower()=="truvivity":
        truvivity(message)
    elif message.text.lower()=="xs":
        xs(message)
    else:
        bot.register_next_step_handler(message, health_choice)

def nutrilite(message):
    bot.send_photo(message.chat.id, photo=open('3.png', 'rb'))
    bot.send_message(message.chat.id, 'Amway — компания №1 прямых продаж в мире* и на сегодняшний день является одним из лидеров среди компаний-производителей товаров массового спроса для поддержания красоты, здоровья и ведения домашнего хозяйства. Бизнес-модель компании предполагает продажу продукта не через розничные магазины, а через сеть индивидуальных дистрибьюторов, которые продвигают продукт и получают вознаграждение за услуги по продвижению продукции. '
'С компанией сотрудничают более 1 миллиона дистрибьюторов во всем мире.'
'Сегодня компания представлена в более чем 80 странах мира, штаб квартира находится в городе Эйда, штат Мичиган, США. '
'Компания Amway представлена в Казахстане с 2013 года и на сегодняшний день  является 2-м самым быстро растущим рынком Amway. За 2018-2019 г компания выплатила 11,3$ млн в качестве выплат независимым предпринимателям Amway, 147 тысячам клиентов и предпринимателям Amway. '
, reply_markup=backboard)
    url3(message)
    bot.register_next_step_handler(message, back)

def truvivity(message):
    bot.send_photo(message.chat.id, photo=open('4.png', 'rb'))
    bot.send_message(message.chat.id, 'РАСКРОЙТЕ СЕКРЕТ ГЛАДКОЙ, ЭЛАСТИЧНОЙ И ПЛЕНИТЕЛЬНО СИЯЮЩЕЙ КОЖИ!'
'Инновационная система увлажнения кожи TRUVIVITY™ от NUTRILITE™ – решение, направленное на глубокое увлажнение Вашей кожи 24 часа в сутки!', reply_markup=backboard)
    url4(message)
    bot.register_next_step_handler(message, back)

def xs(message):
    bot.send_photo(message.chat.id, photo=open('5.png', 'rb'))
    bot.send_message(message.chat.id, 'ЭНЕРГИЯ ТВОЕГО Я! ТЫ МОЖЕШЬ БОЛЬШЕ, ЧЕМ ТЫ ДУМАЕШЬ! Для тех, кто верит, что в жизни помимо работы найдется место для отдыха и приключений! ', reply_markup=backboard)
    url5(message)
    bot.register_next_step_handler(message, back)

def url5(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/our-brands/xs-powerdrink')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)

def url4(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/our-brands/truvivity-by-nutrilite')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)

def url3(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/our-brands/nutrilite')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)

def beauty(message):
    beautyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    beautyboard.row('ARTISTRY', 'Ароматы Amway', 'HYMM for Men')
    bot.send_message(message.chat.id,"Выбирите интересующий вас бренд", reply_markup=beautyboard)
    beauty_choice(message)

def beauty_choice(message):
    if message.text.lower()=="artistry":
        artistry(message)
    elif message.text.lower()=="ароматы amway":
        aroamway(message)
    elif message.text.lower()=="hymm for men":
        hymm(message)
    else:
        bot.register_next_step_handler(message, beauty_choice)

def artistry(message):
    bot.send_photo(message.chat.id, photo=open('6.png', 'rb'))
    bot.send_message(message.chat.id, 'В основе философии бренда ARTISTRY™ сочетание удивительной силы природы, последних научных разработок и внимание к индивидуальным потребностям каждой женщины. С помощью средств по уходу за кожей ARTISTRY™ и линии декоративной косметики, мечты становятся реальностью!'
    , reply_markup=backboard)
    url6(message)
    bot.register_next_step_handler(message, back)

def url6(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/our-brands/artistry')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)
def aroamway(message):
    bot.send_photo(message.chat.id, photo=open('7.png', 'rb'))
    bot.send_message(message.chat.id, 'Ароматы для женщин и мужчин, отражающие Ваше настроение и подчеркивающие индивидуальность Вашего стиля.   ', reply_markup=backboard)
    url7(message)
    bot.register_next_step_handler(message, back)

def url7(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/our-brands/fragrances-by-amway')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)

def hymm(message):
    bot.send_photo(message.chat.id, photo=open('8.png', 'rb'))
    bot.send_message(message.chat.id, 'Серия средств по уходу для мужчин. Эффективные формулы с натуральными ингредиентами.     '
    , reply_markup=backboard)
    url8(message)
    bot.register_next_step_handler(message, back)

def url8(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/our-brands/hymm')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)

def home(message):
    homeboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    homeboard.row('Amway HOME', 'eSPRING', 'iCook')
    bot.send_message(message.chat.id,"Выбирите интересующий вас бренд", reply_markup=homeboard)
    home_choice(message)

def home_choice(message):
    if message.text.lower()=="amway home":
        amway_home(message)
    elif message.text.lower()=="espring":
        espring(message)
    elif message.text.lower()=="icook":
        icook(message)
    else:
        bot.register_next_step_handler(message, home_choice)

def amway_home(message):
    bot.send_photo(message.chat.id, photo=open('9.png', 'rb'))
    bot.send_message(message.chat.id, 'AMWAY HOME™ — средства для стирки белья, очищения поверхностей и мытья посуды — обладают все теми же замечательными качествами, заслужившими Вашу любовь и доверие. '
    , reply_markup=backboard)
    url9(message)
    bot.register_next_step_handler(message, back)

def url9(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/our-brands/amway-home  ')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)

def espring(message):
    bot.send_photo(message.chat.id, photo=open('10.png', 'rb'))
    bot.send_message(message.chat.id, 'Благодаря системе очистке воды eSpring™ Вы и ваша семья смогут насладиться очищенной и полезной водой.', reply_markup=backboard)
    url10(message)
    bot.register_next_step_handler(message, back)

def url10(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/our-brands/espring')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)

def icook(message):
    bot.send_photo(message.chat.id, photo=open('11.png', 'rb'))
    bot.send_message(message.chat.id, 'Кухонная посуда iCook — это не просто наилучший способ приготовления пищи. Ведь она позволяет вам наслаждаться изысканными блюдами в кругу самых дорогих людей — своей семьи и друзей.',
     reply_markup=backboard)
    url11(message)
    bot.register_next_step_handler(message, back)

def url11(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/our-brands/icook')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)

def body(message):
    bodyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    bodyboard.row('G&H', 'Satinique', 'Glister')
    bot.send_message(message.chat.id,"Выбирите интересующий вас бренд", reply_markup=bodyboard)
    body_choice(message)

def body_choice(message):
    if message.text.lower()=="g&h":
        gh(message)
    elif message.text.lower()=="satinique":
        satinique(message)
    elif message.text.lower()=="glister":
        glister(message)
    else:
        bot.register_next_step_handler(message, body_choice)

def gh(message):
    bot.send_photo(message.chat.id, photo=open('12.png', 'rb'))
    bot.send_message(message.chat.id, 'Коллекция средств G&H от Amway для ухода за кожей для всех членов семьи независимо от пола, возраста и типа кожи.', reply_markup=backboard)
    url12(message)
    bot.register_next_step_handler(message, back)

def url12(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/our-brands/bodycare#skin')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)

def satinique(message):
    bot.send_photo(message.chat.id, photo=open('13.png', 'rb'))
    bot.send_message(message.chat.id, 'Satinique™ от Amway это полный набор эффективных средств для ухода, восстановления и укладки волос любого типа.', reply_markup=backboard)
    url13(message)
    bot.register_next_step_handler(message, back)

def url13(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/our-brands/bodycare#hair')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)

def glister(message):
    bot.send_photo(message.chat.id, photo=open('14.png', 'rb'))
    bot.send_message(message.chat.id, 'Glister™ от Amway это уникальный комплексный набор эффективных, универсальных средств по уходу за полостью рта.', reply_markup=backboard)
    url14(message)
    bot.register_next_step_handler(message, back)

def url14(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/our-brands/bodycare#teeth')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)

def delivery(message):
    del1=telebot.types.KeyboardButton('Условия доставки')
    del2=telebot.types.KeyboardButton('Условия оплаты')
    del3=telebot.types.KeyboardButton('Как разместить заказ?')
    delboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    delboard.row(del1)
    delboard.row(del2)
    delboard.row(del3)
    bot.send_photo(message.chat.id, photo=open('16.png', 'rb'))
    bot.send_message(message.chat.id,"Откройте для себя уникальную продукцию Amway — закажите продукцию онлайн или купите в магазинах г.Алматы и г.Нур-Султан.", reply_markup=delboard)
    del_choice(message)
    

def del_choice(message):
    if message.text.lower()=="условия доставки":
        deliv(message)
    elif message.text.lower()=="условия оплаты":
        payment(message)
    elif message.text.lower()=="как разместить заказ?":
        how(message)
    else:
        bot.register_next_step_handler(message, del_choice)

def deliv(message):
    bot.send_photo(message.chat.id, photo=open('17.png', 'rb'))
    bot.send_message(message.chat.id, '\nДоставка на дом\n'
    'Закажите товар онлайн и получите его, не выходя из дома. '                                                                 
          ' \nСамовывоз\n'
    'Мы предлагаем Вам возможность самостоятельно забирать свои заказы от 100 баллов со складов в г.Алматы, г.Нур-Султан и г. Актобе.', reply_markup=backboard)
    url15(message)
    bot.register_next_step_handler(message, back)

def url15(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/how-to-buy/delivery#pickup')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)

def payment(message):
    
    bot.send_photo(message.chat.id, photo=open('18.png', 'rb'))
    bot.send_message(message.chat.id,
    'Все заказы, размещенные через www.amway.kz могут быть оплачены банковской картой в режиме онлайн, а также банковским или почтовым переводами. ', reply_markup=backboard)
    bot.send_document(message.chat.id, data=open('instruction.pdf', 'rb'))
    url16(message)
    bot.register_next_step_handler(message, back)

def url16(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/how-to-buy/payment-terms#online-payment')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)

def how(message):
    bot.send_photo(message.chat.id, photo=open('19.png', 'rb'))
    bot.send_message(message.chat.id,
    'Компания Amway предлагает разные варианты доставки продукции — стоимость будет зависеть от параметров и объема заказа.', reply_markup=backboard)
    url17(message)
    bot.register_next_step_handler(message, back)

def url17(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/how-to-buy/how-to-make')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)

def guarantee(message):
    bot.send_message(message.chat.id,
    'Мы настолько уверены в качестве нашей продукции, что в случае, если она вам не понравилась, готовы её принять в течении 90 дней без лишних вопросов.'                                               
'Мы поддерживаем высокое качество продукции Amway и гарантируем Вам удовлетворение от ее'
'использования. Если Вы или Ваши клиенты не удовлетворены продукцией (товаром), то по Вашему желанию (усмотрению) мы вернем Вам денежные средства или осуществим обмен товара ненадлежащего качества на идентичный/аналогичный товар надлежащего качества (в случае его наличия на момент обращения в ТОО «Эмвэй»).'
, reply_markup=backboard)
    url18(message)
    bot.register_next_step_handler(message, back)

def url18(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/how-to-buy/return-of-a-product')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)


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














kzkeyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
kzbutton1 = telebot.types.KeyboardButton('Компания туралы')
kzbutton2 = telebot.types.KeyboardButton('Өнім туралы')
kzbutton3 = telebot.types.KeyboardButton('Қалай сатып алуға болады?')
kzbutton4 = telebot.types.KeyboardButton('Amway-дің сапа кепілдігі')
kzbutton5 = telebot.types.KeyboardButton('VIP+ арналған артықшылықтар бағдарламасы')
kzbutton6 = telebot.types.KeyboardButton('Amway Тәуелсіз Кәсіпкеріне арналған сыйақылар')

kzkeyboard1.row(kzbutton1)
kzkeyboard1.row(kzbutton2)
kzkeyboard1.row(kzbutton3)
kzkeyboard1.row(kzbutton4)
kzkeyboard1.row(kzbutton5)
kzkeyboard1.row(kzbutton6)

kzkeyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
kzkeyboard2.row('Amway әлемде', 'Amway Қазақстанда', 'Компанияның миссиясы')
kzbackboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
kzbackboard.row('Басты мәзір')

kzitem1 = telebot.types.KeyboardButton('Денсаулық')
kzitem2 = telebot.types.KeyboardButton('Сұлулық')
kzitem3 = telebot.types.KeyboardButton('Дене күтімі')
kzitem4 = telebot.types.KeyboardButton('Үй')
kzitem5 = telebot.types.KeyboardButton('Басты мәзір')

kzitemboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
kzitemboard.row(kzitem1)
kzitemboard.row(kzitem2)
kzitemboard.row(kzitem3)
kzitemboard.row(kzitem4)
kzitemboard.row(kzitem5)

kzprivboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
kzprivboard.row('Возможности', 'Заработок')


cityitem1 = telebot.types.KeyboardButton('Алматы')
cityitem2 = telebot.types.KeyboardButton('Нурсултан')
cityitem3 = telebot.types.KeyboardButton('Караганда')
cityitem4 = telebot.types.KeyboardButton('Шымкент')
cityitem5 = telebot.types.KeyboardButton('Актау')



def kz_city(message):
    bot.send_message(message.chat.id, 'Сәлем, мен Amway бот, сіздің қалаңызды таңдаңыз', reply_markup=cityboard)
    bot.register_next_step_handler(message, kzcity_choice)

def kzcity_choice(message):
    if message.text.lower() == 'алматы':
        kzstart_message(message)
    elif message.text.lower() == 'нурсултан':
        kzstart_message(message)
    elif message.text.lower() == 'караганда':
        kzstart_message(message)
    elif message.text.lower() == 'шымкент':
        kzstart_message(message)
    elif message.text.lower() == 'актау':
        kzstart_message(message)
    else:
        bot.send_message(message.chat.id, 'Жалғастыру үшін түймесін басыңыз')

def kzstart_message(message):
    bot.send_message(message.chat.id, 'Басты мәзір', reply_markup=kzkeyboard1)
    bot.register_next_step_handler(message, kzsend_text)

def kzsend_text(message):
    if message.text.lower() == 'компания туралы':
        kzabout(message)
    elif message.text.lower() == 'өнім туралы':
        kzitems(message)
    elif message.text.lower() == 'қалай сатып алуға болады?':
        kzdelivery(message)
    elif message.text.lower() == 'amway-дің сапа кепілдігі':
        kzguarantee(message)
    elif message.text.lower() == 'vip+ арналған артықшылықтар бағдарламасы':
        kzstudy(message)
    elif message.text.lower() == 'amway Тәуелсіз Кәсіпкеріне арналған сыйақылар':
        kzfirst(message)
    else:
        bot.send_message(message.chat.id, 'Жалғастыру үшін түймесін басыңыз')

def kzabout(message):
    bot.send_photo(message.chat.id, photo=open('kz/0.png','rb'))
    bot.send_message(message.chat.id,
                    'Amway — әлемдегі тікелей сатылымдардың №1 компаниясы* және қазіргі таңда сұлулыққа, денсаулыққа және үй шаруашылығын жүргізуге арналған жаппай сұранысқа ие тауарларды өндіруші-компаниялардың арасында көшбасшылардың бірі болып табылады. Компанияның бизнес-үлгісі өнімдерді бөлшек сауда дүкендері арқылы емес, дербес модель дистрибьюторлар желісі арқылы сатуды көздейді, олар өнімді ілгері жылжытады және өнімді ілгері жылжыту қызметі үшін сыйақы алып отырады. '
                    'Компаниямен бүкіл әлем бойынша 1 миллионнан астам дистрибьютор жұмыс істейді.'
                    'Бүгінде компанияның әлемнің 80 астам елінде өкілдіктері бар, штаб пәтері АҚШ-тың Мичиган штатындағы Эйда қаласында орналасқан. '
                    'Amway компаниясы Қазақстанда 2013 жылдан бері жұмыс істеп келеді және қазіргі уақытта  Amway-дің ең жылдам дамып келе жатқан 2-шы нарығы болып табылады. 2018-2019 жж. компания Amway тәуелсіз кәсіпкерлеріне, Amway-дің 147 мың клиенттері мен кәсіпкерлеріне төлем ретінде 11,3$ млн. төледі. '                                                                                                             
                    '*Euromonitor International  2019 ж. деректері бойынша'
, reply_markup =  kzkeyboard2
                     )

    bot.register_next_step_handler(message, kzabout_choice)


def kzabout_choice(message):
    if message.text.lower() == 'amway әлемде':
        kzhistory(message)
    elif message.text.lower() == 'amway қазақстанда':
        kznow(message)
    elif message.text.lower() == 'компанияның миссиясы':
        kzmis(message)
    else:
        bot.send_message(message.chat.id, 'Батырманы басыңыз')
        bot.register_next_step_handler(message, kzabout_choice)

def kzhistory(message):
    bot.send_photo(message.chat.id, photo=open('kz/1.png','rb'))
    kzurl1(message)
    bot.send_message(message.chat.id, "Басты мәзір?", reply_markup=kzbackboard)
    bot.register_next_step_handler(message, kzback)

def kzurl1(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/about-amway-new/globally')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Мұнда оқыңыз", reply_markup = markup)

def kznow(message):
    bot.send_photo(message.chat.id, photo=open('kz/2.png','rb'))
    kzurl2(message)
    bot.send_message(message.chat.id, "Басты мәзір", reply_markup=kzbackboard)
    bot.register_next_step_handler(message, kzback)

def kzurl2(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/about-amway-new/in-kazakhstan')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Мұнда оқыңыз", reply_markup = markup)

def kzmis(message):
    bot.send_photo(message.chat.id, photo=open('kz/0.png','rb'))
    bot.send_message(message.chat.id, 'Amway компаниясы өзінің құрылған сәтінен-ақ өз миссиясына - адамдардың бұрынғысынан жақсы және жеңіл өмір сүруіне көмектесу миссиясына адал болып отырды. Біз тұтынушылар үшін, сондай-ақ бизнес-серіктестер үшін жоғары деңгейдегі сервиске кепілдік береміз.'
    , reply_markup=kzbackboard)
    bot.register_next_step_handler(message, kzback)


def kzback(message):
    if message.text.lower() == 'басты мәзір':
        kzstart_message(message)
    else:
        bot.send_message(message.chat.id, 'Жалғастыру үшін түймесін басыңыз')
        bot.register_next_step_handler(message, kzback)

def kzitems(message):
    bot.send_photo(message.chat.id, photo=open('kz/15.png','rb'))
    bot.send_message(message.chat.id, 'Amway компаниясының бренділерімен және сұлулыққа, денсаулыққа және дене күтіміне арналған тауарлардың ассортиментімен танысыңыз.'
    , reply_markup=kzitemboard)
    kzitems_choice(message)

def kzitems_choice(message):
    if message.text.lower()=="денсаулық":
        kzhealth(message)
    elif message.text.lower()=="сұлулық":
        kzbeauty(message)
    elif message.text.lower()=="үй":
        kzhome(message)
    elif message.text.lower()=="дене күтімі":
        kzbody(message)
    elif message.text.lower()=="басты мәзір":
        bot.register_next_step_handler(message, kzback)
    else:
        bot.register_next_step_handler(message, kzitems_choice)

def kzhealth(message):
    healthboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    healthboard.row('Nutrilite', 'TRUVIVITY', 'XS')
    bot.send_message(message.chat.id,"Сізді қызықтыратын өнімді таңдаңыз", reply_markup=healthboard)
    kzhealth_choice(message)

def kzhealth_choice(message):
    if message.text.lower()=="nutrilite":
        kznutrilite(message)
    elif message.text.lower()=="truvivity":
        kztruvivity(message)
    elif message.text.lower()=="xs":
        kzxs(message)
    else:
        bot.register_next_step_handler(message, kzhealth_choice)

def kznutrilite(message):
    bot.send_photo(message.chat.id, photo=open('kz/3.png', 'rb'))
    bot.send_message(message.chat.id, 'NUTRILITE – бұл әлемдегі дәрумендер мен минералды кешендердің сатылымы бойынша №1 бренд*. Брендінің тарихы 85 жылды құрайды, бұл осы жылдар бойы тағам саласындағы ғылыми зерттеулер мен әзірлемелер, сондай-ақ экспертизалар жүзеге асырылып отырды. Бүгінде АҚШ-тың Калифорния штатының Буэна Парк қаласында орналасқан NUTRILITE™ денсаулық институтында 100 астам ғалымдар мен зерттеушілер жұмыс істеуде.  NUTRILITE™ — бұл меншікті сертификатталған органикалық фермаларда өсіріліп, жиналып және өңдеуден өткізіліп отыратын өсімдіктерге негізделген дәрумендер мен диеталық қоспалардың әлемдегі жалғыз маркасы **'
'*Euromonitor International Limited 2018 жылғы деректері бойынша'
'**Дереккөз: Euromonitor International Limited. 2016 ж. барлық өндірістік қуаттылықтарға ие болып отырған дәруменді және биологиялық белсенді қоспалардың әлемдік өндірушілеріне жүргізілген шолу деректері бойынша.', reply_markup=kzbackboard)
    kzurl3(message)
    bot.register_next_step_handler(message, kzback)

def kztruvivity(message):
    bot.send_photo(message.chat.id, photo=open('kz/4.png', 'rb'))
    bot.send_message(message.chat.id, 'ТЕГІС, СОЗЫЛҒЫШ ЖӘНЕ КЕРЕМЕТ ЖАРҚЫРАҒАН ТЕРІНІҢ ҚҰПИЯСЫН АШЫҢЫЗ!'
'NUTRILITE™ ұсынған TRUVIVITY™ теріні ылғалдандырудың инновациялық жүйесі – Сіздің теріңізді тәулігіне 24 сағат бойы терең ылғалдауға бағытталған шешім!', reply_markup=kzbackboard)
    kzurl4(message)
    bot.register_next_step_handler(message, kzback)

def kzxs(message):
    bot.send_photo(message.chat.id, photo=open('kz/5.png', 'rb'))
    bot.send_message(message.chat.id, 'СЕНІҢ МЕНДІК ЭНЕРГИЯҢ! СЕН ӨЗІҢ ОЙЛАҒАННАН ДА АРТЫҚ ЖАСАЙ АЛАСЫҢ! Өмірде жұмыстан басқа демалыс пен қызықты оқиғаларға да орын бар екеніне сенетіндер үшін!', reply_markup=kzbackboard)
    kzurl5(message)
    bot.register_next_step_handler(message, kzback)

def kzurl5(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/our-brands/xs-powerdrink')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Толығырақ ақпаратпен компанияның сайтынан танысуыңызға болады: ", reply_markup = markup)

def kzurl4(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/our-brands/truvivity-by-nutrilite')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Толығырақ ақпаратпен компанияның сайтынан танысуыңызға болады: ", reply_markup = markup)

def kzurl3(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/our-brands/nutrilite')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Толығырақ ақпаратпен компанияның сайтынан танысуыңызға болады: ", reply_markup = markup)

def kzbeauty(message):
    beautyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    beautyboard.row('ARTISTRY', 'Amway хош иістері', 'HYMM for Men')
    bot.send_message(message.chat.id,"Сізді қызықтыратын өнімді таңдаңыз", reply_markup=beautyboard)
    kzbeauty_choice(message)

def kzbeauty_choice(message):
    if message.text.lower()=="artistry":
        kzartistry(message)
    elif message.text.lower()=="amway хош иістері":
        kzaroamway(message)
    elif message.text.lower()=="hymm for men":
        kzhymm(message)
    else:
        bot.register_next_step_handler(message, kzbeauty_choice)

def kzartistry(message):
    bot.send_photo(message.chat.id, photo=open('kz/6.png', 'rb'))
    bot.send_message(message.chat.id, 'ARTISTRY™ брендінің философиясын табиғаттың керемет күшін, соңғы ғылыми әзірлемелер және әр әйелдің жеке қажетсінулеріне деген көңіл бөлу құрайды. ARTISTRY™ тері күтіміне арналған құралдары мен декоративті косметика желісінің көмегімен армандар ақиқатқа айналады!  '
    , reply_markup=kzbackboard)
    kzurl6(message)
    bot.register_next_step_handler(message, kzback)

def kzurl6(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/our-brands/artistry')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Толығырақ ақпаратпен компанияның сайтынан танысуыңызға болады: ", reply_markup = markup)
def kzaroamway(message):
    bot.send_photo(message.chat.id, photo=open('kz/7.png', 'rb'))
    bot.send_message(message.chat.id, 'Әйелдер мен еркектерге арналған, Сіздің көңіл-күйіңізді білдіретін және Сіздің стиліңіздің дербестігін көрсететін хош иістер.  ', reply_markup=kzbackboard)
    kzurl7(message)
    bot.register_next_step_handler(message, kzback)

def kzurl7(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/our-brands/fragrances-by-amway')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Толығырақ ақпаратпен компанияның сайтынан танысуыңызға болады: ", reply_markup = markup)

def kzhymm(message):
    bot.send_photo(message.chat.id, photo=open('kz/8.png', 'rb'))
    bot.send_message(message.chat.id, 'ЕРКЕКТІҢ ТАҢДАУЫ Еркектерге арналған күтім жасау құралдарының топтамасы. Табиғи ингредиенттері бар тиімді формулалар'
    , reply_markup=kzbackboard)
    kzurl8(message)
    bot.register_next_step_handler(message, kzback)

def kzurl8(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/our-brands/hymm')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Толығырақ ақпаратпен компанияның сайтынан танысуыңызға болады: ", reply_markup = markup)

def kzhome(message):
    homeboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    homeboard.row('Amway HOME', 'eSPRING', 'iCook')
    bot.send_message(message.chat.id,"Сізді қызықтыратын өнімді таңдаңыз", reply_markup=homeboard)
    kzhome_choice(message)

def kzhome_choice(message):
    if message.text.lower()=="amway home":
        kzamway_home(message)
    elif message.text.lower()=="espring":
        kzespring(message)
    elif message.text.lower()=="icook":
        kzicook(message)
    else:
        bot.register_next_step_handler(message, kzhome_choice)

def kzamway_home(message):
    bot.send_photo(message.chat.id, photo=open('kz/9.png', 'rb'))
    bot.send_message(message.chat.id, 'AMWAY HOME™ — кір жууға, беттерді тазартуға және ыдыс жууға арналған құралдар Сіздің сүйіспеншілігіңіз бен сеніміңізге лайық тура сол керемет қасиеттерге ие'
    , reply_markup=kzbackboard)
    kzurl9(message)
    bot.register_next_step_handler(message, kzback)

def kzurl9(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/our-brands/amway-home  ')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Толығырақ ақпаратпен компанияның сайтынан танысуыңызға болады: ", reply_markup = markup)

def kzespring(message):
    bot.send_photo(message.chat.id, photo=open('kz/10.png', 'rb'))
    bot.send_message(message.chat.id, 'eSpring™ су тазарту жүйесінің арқасында Сіз бен Сіздің отбасыңыз тазартылған және пайдалы судан дәм татып рахаттана алады.', reply_markup=kzbackboard)
    kzurl10(message)
    bot.register_next_step_handler(message, kzback)

def kzurl10(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/our-brands/espring')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Толығырақ ақпаратпен компанияның сайтынан танысуыңызға болады: ", reply_markup = markup)

def kzicook(message):
    bot.send_photo(message.chat.id, photo=open('kz/11.png', 'rb'))
    bot.send_message(message.chat.id, 'iCook ас үй ыдыстары — бұл ас әзірлеудің ең жақсы әдісі ғана емес. Сонымен қатар ол бізге ең қымбат адамдарымыздың – отбасымыз бен достарымыздың ортасында таңдаулы астан дәм татып рахаттануға мүмкіндік береді.',
     reply_markup=kzbackboard)
    kzurl11(message)
    bot.register_next_step_handler(message, kzback)

def kzurl11(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/our-brands/icook')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Толығырақ ақпаратпен компанияның сайтынан танысуыңызға болады: ", reply_markup = markup)

def kzbody(message):
    bodyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    bodyboard.row('G&H', 'Satinique', 'Glister')
    bot.send_message(message.chat.id,"Сізді қызықтыратын өнімді таңдаңыз", reply_markup=bodyboard)
    kzbody_choice(message)

def kzbody_choice(message):
    if message.text.lower()=="g&h":
        kzgh(message)
    elif message.text.lower()=="satinique":
        kzsatinique(message)
    elif message.text.lower()=="glister":
        kzglister(message)
    else:
        bot.register_next_step_handler(message, kzbody_choice)

def kzgh(message):
    bot.send_photo(message.chat.id, photo=open('kz/12.png', 'rb'))
    bot.send_message(message.chat.id, 'Жынысына, жасы мен тері типіне байланыссыз барлық отбасы мүшелерінің тері күтіміне арналған Amway ұсынған G&H құралдарының топтамасы.', reply_markup=kzbackboard)
    kzurl12(message)
    bot.register_next_step_handler(message, kzback)

def kzurl12(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/our-brands/bodycare#skin')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Толығырақ ақпаратпен компанияның сайтынан танысуыңызға болады: ", reply_markup = markup)

def kzsatinique(message):
    bot.send_photo(message.chat.id, photo=open('kz/13.png', 'rb'))
    bot.send_message(message.chat.id, 'Кез келген типтегі шашты күтуге, қалпына келтіруге және сәндеуге арналған Amway ұсынған Satinique™ тиімді құралдардың толық жиыны.', reply_markup=kzbackboard)
    kzurl13(message)
    bot.register_next_step_handler(message, kzback)

def kzurl13(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/our-brands/bodycare#hair')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Толығырақ ақпаратпен компанияның сайтынан танысуыңызға болады: ", reply_markup = markup)

def kzglister(message):
    bot.send_photo(message.chat.id, photo=open('kz/14.png', 'rb'))
    bot.send_message(message.chat.id, 'Amway ұсынған Glister™ - бұл ауыз қуысының күтіміне арналған тиімді, әмбебап құралдарының ерекше кешенді жиыны.', reply_markup=kzbackboard)
    kzurl14(message)
    bot.register_next_step_handler(message, kzback)

def kzurl14(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/our-brands/bodycare#teeth')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Толығырақ ақпаратпен компанияның сайтынан танысуыңызға болады:", reply_markup = markup)

def kzdelivery(message):
    del1=telebot.types.KeyboardButton('Жеткізу шарттары')
    del2=telebot.types.KeyboardButton('Төлем шарттары')
    del3=telebot.types.KeyboardButton('Қалай тапсырыс беруге болады?')
    delboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    delboard.row(del1)
    delboard.row(del2)
    delboard.row(del3)
    bot.send_photo(message.chat.id, photo=open('kz/16.png', 'rb'))
    bot.send_message(message.chat.id,"Өзіңіз үшін Amway ерекше өнімдерін ашыңыз — өнімдерге онлайн тапсырыс беріңіз немесе Алматы және Нұр-Сұлтан қалаларындағы дүкендерден сатып алыңыз", reply_markup=delboard)
    kzdel_choice(message)
    

def kzdel_choice(message):
    if message.text.lower()=="жеткізу шарттары":
        kzdeliv(message)
    elif message.text.lower()=="төлем шарттары":
        kzpayment(message)
    elif message.text.lower()=="қалай тапсырыс беруге болады?":
        kzhow(message)
    else:
        bot.register_next_step_handler(message, kzdel_choice)

def kzdeliv(message):
    bot.send_photo(message.chat.id, photo=open('kz/17.png', 'rb'))
    bot.send_message(message.chat.id, '\nҮйге жеткізу\n'
    'Тауарға онлайн тапсырыс беріп, оны үйден шықпай-ақ алыңыз.  '                                                                 
          ' \nКеліп алып кету\n'
    'Біз 100 ұпайдан басталатын тапсырыстарыңызды Алматы, Нұр-Сұлтан және Ақтөбе қалаларындағы қоймалардан келіп алып кету мүмкіндігін ұсынамыз.', reply_markup=kzbackboard)
    kzurl15(message)
    bot.register_next_step_handler(message, kzback)

def kzurl15(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/how-to-buy/delivery#pickup')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Толығырақ ақпаратпен компанияның сайтынан танысуыңызға болады:", reply_markup = markup)

def kzpayment(message):
    
    bot.send_photo(message.chat.id, photo=open('kz/18.png', 'rb'))
    bot.send_message(message.chat.id,
    'www.amway.kz сайты арқылы берілген тапсырыстардың барлығының ақысын онлайн режимінде банкілік карта арқылы, сондай-ақ банкілік немесе пошталық аударымдар арқылы төлеуге болады.', reply_markup=kzbackboard)
    bot.send_document(message.chat.id, data=open('kz/instruction.pdf', 'rb'))
    kzurl16(message)
    bot.register_next_step_handler(message, kzback)

def kzurl16(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/how-to-buy/payment-terms#online-payment')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Толығырақ ақпаратпен компанияның сайтынан танысуыңызға болады:", reply_markup = markup)

def kzhow(message):
    bot.send_photo(message.chat.id, photo=open('kz/19.png', 'rb'))
    bot.send_message(message.chat.id,
    'Amway компаниясы өнімдерді жеткізудің түрлі жолдарын ұсынады — бағасы тапсырыстың параметрлері мен көлеміне байланысты болады', reply_markup=kzbackboard)
    kzurl17(message)
    bot.register_next_step_handler(message, kzback)

def kzurl17(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Сілтемеге басыңыз:)',
                                            url='https://www.amway.kz/how-to-buy/how-to-make')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Толығырақ ақпаратпен компанияның сайтынан танысуыңызға болады:", reply_markup = markup)

def kzguarantee(message):
    bot.send_message(message.chat.id,
    'Мы настолько уверены в качестве нашей продукции, что в случае, если она вам не понравилась, готовы её принять в течении 90 дней без лишних вопросов.'                                               
'Мы поддерживаем высокое качество продукции Amway и гарантируем Вам удовлетворение от ее'
'использования. Если Вы или Ваши клиенты не удовлетворены продукцией (товаром), то по Вашему желанию (усмотрению) мы вернем Вам денежные средства или осуществим обмен товара ненадлежащего качества на идентичный/аналогичный товар надлежащего качества (в случае его наличия на момент обращения в ТОО «Эмвэй»).'
, reply_markup=backboard)
    kzurl18(message)
    bot.register_next_step_handler(message, kzback)

def kzurl18(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Кликните на ссылку:)',
                                            url='https://www.amway.kz/how-to-buy/return-of-a-product')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Более подробно можете ознакомиться по на сайте компании", reply_markup = markup)


def kzpriv(message):
    bot.send_message(message.chat.id, 'Выбирете вашу привелегию', reply_markup=privboard)
    bot.register_next_step_handler(message, kzpriv_choice)

def kzpriv_choice(message):
    if message.text.lower()=="возможности":
        bot.send_message(message.chat.id, 'Вся информация о возможностях', reply_markup=kzbackboard)
        bot.register_next_step_handler(message, kzback)
    elif message.text.lower()=="заработок":
        bot.send_message(message.chat.id, 'Вся информация о заработке', reply_markup=kzbackboard)
        bot.register_next_step_handler(message, kzback)
    else:
        bot.register_next_step_handler(message, kzpriv_choice)

def kzstudy(message):
    bot.send_message(message.chat.id, 'Здесь вся инфа про обучение', reply_markup=backboard)
    bot.register_next_step_handler(message, kzback)

def kzfirst(message):
    bot.send_message(message.chat.id, 'Здесь вся инфа про первые шаги', reply_markup=backboard)
    bot.register_next_step_handler(message, kzback)
bot.polling()