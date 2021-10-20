import requests
from bs4 import BeautifulSoup
from telebot import types  # Импортируем типы из модуля, чтобы создавать кнопки
import telebot  # Подключаем модуль для Телеграма
bot = telebot.TeleBot('2052572267:AAESJ1ffIJQmINdV3Snh9LS6rcc005KVE9Y')  # Указываем токен
first = [""]
second = [""]
second_add = [""]
third = [""]


@bot.message_handler(commands=["start"])
def inline(message):
    key = types.InlineKeyboardMarkup()
    """/start"""
    but_1 = types.InlineKeyboardButton(text="курс валюты", callback_data="currency")
    but_2 = types.InlineKeyboardButton(text="страна - валюта", callback_data="Country")
    key.add(but_1, but_2)
    bot.send_message(message.chat.id, "Что бы вы хотели?)", reply_markup=key)
    """/start"""


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'currency':
        """/start-->Посмотреть курс валюты (выдает)"""
        key = types.InlineKeyboardMarkup()
        but_1_1 = types.InlineKeyboardButton(text="Юань", callback_data="currencyY")
        but_1_2 = types.InlineKeyboardButton(text="Доллар", callback_data="currencyD")
        but_1_3 = types.InlineKeyboardButton(text="Евро", callback_data="currencyE")
        but_1_4 = types.InlineKeyboardButton(text="Еще", callback_data="EELSE1")
        key.add(but_1_1, but_1_2, but_1_3, but_1_4)
        bot.send_message(c.message.chat.id, 'Выбирайте валюту)', reply_markup=key)
        """/start-->Посмотреть курс валюты (выдает)"""

    if c.data == 'EELSE1':
        key = types.InlineKeyboardMarkup()
        but_2_1 = types.InlineKeyboardButton(text="Юань", callback_data="currencyY")
        but_2_2 = types.InlineKeyboardButton(text="Доллар", callback_data="currencyD")
        but_2_3 = types.InlineKeyboardButton(text="Евро", callback_data="currencyE")
        but_2_4 = types.InlineKeyboardButton(text="Дирхам", callback_data="dir")
        but_2_5 = types.InlineKeyboardButton(text="Драм", callback_data="dra")
        but_2_6 = types.InlineKeyboardButton(text="Лира", callback_data="lir")
        but_2_7 = types.InlineKeyboardButton(text="Песо", callback_data="pes")
        but_2_8 = types.InlineKeyboardButton(text="Бат", callback_data="bat")
        but_2_9 = types.InlineKeyboardButton(text="Еще", callback_data="EELSE2")
        key.add(but_2_1, but_2_2, but_2_3, but_2_4, but_2_5, but_2_6, but_2_7, but_2_8, but_2_9)
        bot.send_message(c.message.chat.id, 'Выбирайте валюту)', reply_markup=key)

    if c.data == 'EELSE2':
        key = types.InlineKeyboardMarkup()
        but_3_1 = types.InlineKeyboardButton(text="Юань", callback_data="currencyY")
        but_3_2 = types.InlineKeyboardButton(text="Доллар", callback_data="currencyD")
        but_3_3 = types.InlineKeyboardButton(text="Евро", callback_data="currencyE")
        but_3_4 = types.InlineKeyboardButton(text="Дирхам", callback_data="dir")
        but_3_5 = types.InlineKeyboardButton(text="Драм", callback_data="dra")
        but_3_6 = types.InlineKeyboardButton(text="Лира", callback_data="lir")  # a
        but_3_8 = types.InlineKeyboardButton(text="Песо", callback_data="pes")
        but_3_9 = types.InlineKeyboardButton(text="Бат", callback_data="bat")
        but_3_10 = types.InlineKeyboardButton(text="Фунт стер.", callback_data="fst")
        but_3_11 = types.InlineKeyboardButton(text="Швец. франк", callback_data="shf")
        but_3_12 = types.InlineKeyboardButton(text="Иена", callback_data="ien")
        but_3_13 = types.InlineKeyboardButton(text="Авст. доллар", callback_data="avd")
        but_3_14 = types.InlineKeyboardButton(text="Гонк. доллар", callback_data="god")
        but_3_15 = types.InlineKeyboardButton(text="ринггит", callback_data="rin")
        but_3_16 = types.InlineKeyboardButton(text="Гульден", callback_data="gul")
        but_3_18 = types.InlineKeyboardButton(text="Лари", callback_data="lar")
        key.add(but_3_1, but_3_2, but_3_3, but_3_4, but_3_5, but_3_6, but_3_8, but_3_9, but_3_10, but_3_11,
                but_3_12, but_3_13, but_3_14, but_3_15, but_3_16, but_3_18)
        bot.send_message(c.message.chat.id, 'Выбирайте валюту)', reply_markup=key)

    if c.data == 'dir':
        result = main('dir')
        print(f'Курс {c.data} равен: {result}')

    if c.data == 'Country':
        """1 Этап выбора валюты стран"""
        key = types.InlineKeyboardMarkup()

        but_3_1 = types.InlineKeyboardButton(text="Россия", callback_data="Rus_c")
        but_3_2 = types.InlineKeyboardButton(text="Америка", callback_data="USA_c")
        but_3_3 = types.InlineKeyboardButton(text="Испания", callback_data="ISP_c")
        but_3_4 = types.InlineKeyboardButton(text="Ещё", callback_data="ELSE_1")
        key.add(but_3_1, but_3_2, but_3_3, but_3_4)
        bot.send_message(c.message.chat.id, 'Выбирайте страну)', reply_markup=key)

    if c.data == 'ELSE_1':
        """LVL1 ELSE"""
        key = types.InlineKeyboardMarkup()

        but_4_1 = types.InlineKeyboardButton(text="Россия", callback_data="Rus_c")
        but_4_2 = types.InlineKeyboardButton(text="Америка", callback_data="USA_c")
        but_4_3 = types.InlineKeyboardButton(text="Испания", callback_data="ISP_c")
        but_4_4 = types.InlineKeyboardButton(text="Франция", callback_data="Fran_c")
        but_4_5 = types.InlineKeyboardButton(text="Китай", callback_data="China_c")
        but_4_6 = types.InlineKeyboardButton(text="Италия", callback_data="ITAL_c")
        but_4_7 = types.InlineKeyboardButton(text="Ещё", callback_data="ELSE_2")
        key.add(but_4_1, but_4_2, but_4_3, but_4_4, but_4_5, but_4_6, but_4_7)
        bot.send_message(c.message.chat.id, 'Выбирайте страну)', reply_markup=key)

    if c.data == 'ELSE_2':
        """LVL2 ELSE"""
        key = types.InlineKeyboardMarkup()

        but_5_1 = types.InlineKeyboardButton(text="Россия", callback_data="Rus_c")
        but_5_2 = types.InlineKeyboardButton(text="Америка", callback_data="USA_c")
        but_5_3 = types.InlineKeyboardButton(text="Испания", callback_data="ISP_c")
        but_5_4 = types.InlineKeyboardButton(text="Франция", callback_data="Fran_c")
        but_5_5 = types.InlineKeyboardButton(text="Китай", callback_data="China_c")
        but_5_6 = types.InlineKeyboardButton(text="Италия", callback_data="ITAL_c")
        but_5_7 = types.InlineKeyboardButton(text="Турция", callback_data="Tur_c")
        but_5_8 = types.InlineKeyboardButton(text="Мексика", callback_data="Mex_c")
        but_5_9 = types.InlineKeyboardButton(text="Германия", callback_data="Ger_c")
        but_5_10 = types.InlineKeyboardButton(text="Таиланд", callback_data="Tai_c")
        but_5_11 = types.InlineKeyboardButton(text="Великобретания", callback_data="Vel_c")
        but_5_12 = types.InlineKeyboardButton(text="Швейцария", callback_data="Shv_c")
        but_5_13 = types.InlineKeyboardButton(text="Ещё", callback_data="ELSE_3")
        key.add(but_5_1, but_5_2, but_5_3, but_5_4, but_5_5, but_5_6, but_5_7, but_5_8, but_5_9, but_5_10, but_5_11,
                but_5_12, but_5_13)
        bot.send_message(c.message.chat.id, 'Выбирайте страну)', reply_markup=key)
    """/start-->Посмотреть курс валюты (обработчик)"""

    if c.data == 'ELSE_3':
        """LVL2 ELSE"""
        key = types.InlineKeyboardMarkup()

        but_6_1 = types.InlineKeyboardButton(text="Россия", callback_data="Rus_c")
        but_6_2 = types.InlineKeyboardButton(text="Америка", callback_data="USA_c")
        but_6_3 = types.InlineKeyboardButton(text="Испания", callback_data="ISP_c")
        but_6_4 = types.InlineKeyboardButton(text="Франция", callback_data="Fran_c")
        but_6_5 = types.InlineKeyboardButton(text="Китай", callback_data="China_c")
        but_6_6 = types.InlineKeyboardButton(text="Италия", callback_data="ITAL_c")
        but_6_7 = types.InlineKeyboardButton(text="Турция", callback_data="Tur_c")
        but_6_8 = types.InlineKeyboardButton(text="Мексика", callback_data="Mex_c")
        but_6_9 = types.InlineKeyboardButton(text="Германия", callback_data="Ger_c")
        but_6_10 = types.InlineKeyboardButton(text="Таиланд", callback_data="Tai_c")
        but_6_11 = types.InlineKeyboardButton(text="Великобретания", callback_data="Vel_c")
        but_6_12 = types.InlineKeyboardButton(text="Швейцария", callback_data="Shv_c")
        but_6_13 = types.InlineKeyboardButton(text="Япония", callback_data="Gap_c")
        but_6_14 = types.InlineKeyboardButton(text="Австралия", callback_data="Avs_c")
        but_6_15 = types.InlineKeyboardButton(text="Гонконг", callback_data="Gonk_c")
        but_6_16 = types.InlineKeyboardButton(text="Греция", callback_data="Gre_c")
        but_6_17 = types.InlineKeyboardButton(text="Малазия", callback_data="Mal_c")
        but_6_18 = types.InlineKeyboardButton(text="Португалия", callback_data="Port_c")
        but_6_19 = types.InlineKeyboardButton(text="Нидерланды", callback_data="Hid_c")
        but_6_20 = types.InlineKeyboardButton(text="Греция", callback_data="Grek_c")
        but_6_21 = types.InlineKeyboardButton(text="Дубаи", callback_data="Dub_c")
        but_6_22 = types.InlineKeyboardButton(text="Эстония", callback_data="Ist_c")
        but_6_23 = types.InlineKeyboardButton(text="Черногория", callback_data="Cher_c")
        but_6_24 = types.InlineKeyboardButton(text="Армения", callback_data="Arm_c")
        key.add(but_6_1, but_6_2, but_6_3, but_6_4, but_6_5, but_6_6, but_6_7, but_6_8, but_6_9, but_6_10, but_6_11,
                but_6_12, but_6_13, but_6_14, but_6_15, but_6_16, but_6_17, but_6_18, but_6_19, but_6_20, but_6_21,
                but_6_22, but_6_23, but_6_24)
        bot.send_message(c.message.chat.id, 'Выбирайте страну)', reply_markup=key)

    """Обработка стран)"""
    if c.data == 'Rus_c':
        result = main('d')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это рубль. Он бесценен!")
    if c.data == 'USA_c':
        result = main('d')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это доллар. Он равен {result} р.")
    if c.data == 'ISP_c':
        result = main('e')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Евро. Оно равно {result} р.")
    if c.data == 'Fran_c':
        result = main('e')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Евро. Оно равно {result} р.")
    if c.data == 'Dub_c':
        result = main('dir')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Дирхам. Он равен {result} р.")
    if c.data == 'Ist_c':
        result = main('e')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Евро. Он равен {result} р.")
    if c.data == 'Cher_c':
        result = main('e')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Евро. Он равен {result} р.")
    if c.data == 'Arm_c':
        result = main('dra')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это драм. Он равен {result} р.")
    if c.data == 'ITAL_c':
        result = main('e')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Евро. он равен {result} р.")  # 5
    if c.data == 'China_c':
        result = main('y')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Юань. Он равен {result} р.")
    if c.data == 'Tur_c':
        result = main('lir')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Лира. она равна {result} р.")
    if c.data == 'Mex_c':
        result = main('pes')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Песо. Оно равно {result} р.")
    if c.data == 'Ger_c':
        result = main('e')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Евро. Он равен {result} р.")
    if c.data == 'Tai_c':
        result = main('bat')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Бат. Он равен {result} р.")  # 5
    if c.data == 'Vel_c':
        result = main('fst')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Фунт Стерлинов. Он равен {result} р.")
    if c.data == 'Shv_c':
        result = main('shf')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это швецарский Франк. Он равен {result} р.")
    if c.data == 'Gap_c':
        result = main('ien')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Иена. она равна {result} р.")
    if c.data == 'Avs_c':
        result = main('avd')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Австралийский доллар. Он равен {result} р.")
    if c.data == 'Gonk_с':
        result = main('god')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Гонконский доллар. Он равен {result} р.")  # 5
    if c.data == 'Gre_c':
        result = main('e')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Евро. Он равен {result} р.")
    if c.data == 'Mal_c':
        result = main('rin')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это ринггит. Он равен {result} р.")
    if c.data == 'Port_c':
        result = main('e')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Евро. он равен {result} р.")
    if c.data == 'Hid_c':
        result = main('gul')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Гульден. Он равен {result} р.")
    if c.data == 'Grek_c':
        result = main('lar')
        bot.send_message(c.message.chat.id, f"Оснавная валюта, это Лари. Она равна {result} р.")  # 5

    if c.data == 'currencyY':
        result = main('y')
        bot.send_message(c.message.chat.id, f"1 Юань равен {result} р.")
    if c.data == 'currencyD':
        result = main('d')
        bot.send_message(c.message.chat.id, f"1 Доллар равен {result} р.")
    if c.data == 'currencyE':
        result = main('e')
        bot.send_message(c.message.chat.id, f"1 Евро равен {result} р.")
    if c.data == 'dir':
        result = main('dir')
        bot.send_message(c.message.chat.id, f'Курс 1 Дирхам равен: {result} р.')
    if c.data == 'dra':
        result = main('dra')
        bot.send_message(c.message.chat.id, f'Курс 1 Драм равен: {result} р.')
    if c.data == 'lir':
        result = main('lir')
        bot.send_message(c.message.chat.id, f'Курс 1 Лиры равен: {result} р.')
    if c.data == 'pes':
        result = main('pes')
        bot.send_message(c.message.chat.id, f'Курс 1 Песо равен: {result} р.')
    if c.data == 'bat':
        result = main('bat')
        bot.send_message(c.message.chat.id, f'Курс 1 Бата равен: {result} р.')
    if c.data == 'fst':
        result = main('fst')
        bot.send_message(c.message.chat.id, f'Курс 1 Фунта стерлинга равен: {result} р.')
    if c.data == 'shf':
        result = main('shf')
        bot.send_message(c.message.chat.id, f'Курс 1 Швецарского франка равен: {result} р.')
    if c.data == 'ien':
        result = main('ien')
        bot.send_message(c.message.chat.id, f'Курс 1 Иены равен: {result} р.')
    if c.data == 'avd':
        result = main('avd')
        bot.send_message(c.message.chat.id, f'Курс 1 Австралийского доллара равен: {result} р.')
    if c.data == 'god':
        result = main('god')
        bot.send_message(c.message.chat.id, f'Курс 1 Гонконгского доллара равен: {result} р.')
    if c.data == 'rin':
        result = main('rin')
        bot.send_message(c.message.chat.id, f'Курс 1 Ринггита равен: {result} р.')
    if c.data == 'gul':
        result = main('gul')
        bot.send_message(c.message.chat.id, f'Курс 1 Гульдена равен: {result} р.')
    if c.data == 'lar':
        result = main('lar')
        bot.send_message(c.message.chat.id, f'Курс 1 Лари равен: {result} р.')
    """/start-->Посмотреть курс валюты (обработчик)"""


"""//////////////////////////////////Ограничение для удобства читания кода///////////////////////////////////////////"""


class Currency:
    """Класс для работ по курсу"""

    # Доллар
    DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei' \
                 '=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8' \
                 'E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178' \
                 '..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
    # Евро
    EURO_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&sxsrf=AOaemvLc9wYK9' \
               'YrHk5_951xFa52ILPTNkw%3A1633593073190&ei=8aZeYZj_CrHMrgSW9ZOoBA&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0' \
               '%B2%D1%80%D0%BE&gs_lcp=Cgdnd3Mtd2l6EAMYAzIECCMQJzIECCMQJzIECCMQJzIICAAQgAQQsQMyCwgAEIAEELEDEIMBMgsIAB' \
               'CABBCxAxCDATILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDILCAAQgAQQsQMQgwE6BwgjEOoCECc6DgguEIAEELEDEMcBENEDOgU' \
               'ILhCABDoICAAQsQMQgwE6CAguEIAEELEDSgUIPBIBM0oECEEYAFDzQ1jvVmDicGgFcAJ4AIABc4gBtASSAQM1LjKYAQCgAQGwAQrA' \
               'AQE&sclient=gws-wiz'
    # Юань
    CNY_RUB = 'https://www.google.com/search?q=%D1%8E%D0%B0%D0%BD%D1%8C+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&rlz=1C1' \
              'CHBD_ruRU893RU893&oq=%D1%8E%D0%B0%D0%BD%D1%8C&aqs=chrome.1.69i57j0i67i433j0i67i131i433j0i67l3j0i512j46' \
              'i512j0i512l2.2165j0j15&sourceid=chrome&ie=UTF-8'
    # Дирхам
    DIR_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%B8%D1%80%D1%85%D0%B0%D0%BC%D0%B0' \
              '+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0' \
              '%B8%D1%80&aqs=chrome.0.0i512l4j69i57j0i512j0i10i512j0i512j0i10i512j0i512.3583j1j15&sourceid=chrome&ie' \
              '=UTF-8 '
    # Драм
    DRA_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D1%80%D0%B0%D0%BC+%D0%BA+%D1%80%D1%83' \
              '%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvIqGqOHoOjnekOMOdoxahijMfKt1g%3A1633949152235' \
              '&ei=4BVkYbDgDau1qtsPu42i6A4&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D1%80%D0%B0%D0%BC+%D0%BA+%D1%80%D1%83' \
              '%D0%B1%D0%BB%D1%8E&gs_lcp' \
              '=Cgdnd3Mtd2l6EAEYADIECAAQDTIECAAQDTIECAAQDTIECAAQDTIICAAQCBANEB4yCAgAEAgQDRAeMggIABAIEA0QHjIICAAQCBA' \
              'NEB46BwgAEEcQsAM6BwgAELADEEM6EAguEMcBEKMCEMgDELADEEM6EAguEMcBENEDEMgDELADEEM6CAgAEAcQChAeOgYIABAHEB5' \
              'KBQg4EgExSgQIQRgAULXjBFjR7wRgkfsEaAFwAngAgAFSiAHsApIBATWYAQCgAQHIAQvAAQE&sclient=gws-wiz'
    # Лира
    LIR_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%BB%D0%B8%D1%80%D0%B0+%D0%BA+%D1%80%D1%8' \
              '3%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvIbIWGajmtXs7g-cDHyq9Igyf6R-w%3A1633949235285' \
              '&ei=MxZkYbiAEZCdrgTwgZXgDg&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%BB%D0%B8%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%' \
              'D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAEYADIECAAQDTIECAAQDTIECAAQDTIGCAAQDRAeMgYIABANEB4yBggAEA0QHjII' \
              'CAAQDRAFEB4yCAgAEA0QBRAeMggIABAIEA0QHjIICAAQCBANEB46BwgAEEcQsAM6BwgAELADEEM6BggAEAcQHkoECEEYAFCulw1Y' \
              'rp4NYOypDWgBcAJ4AIABY4gB9QOSAQE2mAEAoAEByAEKwAEB&sclient=gws-wiz'
    # Песо
    PES_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%BF%D0%B5%D1%81%D0%BE+%D0%BA+%D1%80%D1%8' \
              '3%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvIbfojRwOKFI-7PQR_SMhMLCWr89w%3A163394945440' \
              '6&ei=DhdkYaqRGOzErgSLgo-oAg&ved=0ahUKEwiq0L2GmMLzAhVsoosKHQvBAyUQ4dUDCA4&uact=5&oq=%D0%BA%D1%83%D1%8' \
              '0%D1%81+%D0%BF%D0%B5%D1%81%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEI' \
              'AEMgUIABCABDIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAgQHjIGCAAQCBAeMgYIABAIEB46Bwg' \
              'AEEcQsAM6BwgAELADEEM6BAgAEA06CAgAEAgQBxAeSgQIQRgAUOvjCljG5wpg6ekKaAFwAngAgAFPiAGYApIBATSYAQCgAQHIAQrAA' \
              'QE&sclient=gws-wiz'
    # Бат
    BAT_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B0%D1%82%D1%82+%D0%BA+%D1%80%D1%83' \
              '%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvIbsD4EeeQ7aSppE4ZwCXKMJoPhWA%3A1633949632520&' \
              'ei=wBdkYe6nH-birgSBjozYCw&ved=0ahUKEwjuh7XbmMLzAhVmsYsKHQEHA7sQ4dUDCA4&uact=5&oq=%D0%BA%D1%83%D1%80%D' \
              '1%81+%D0%B1%D0%B0%D1%82%D1%82+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMyCQgAEAoQRh' \
              'CCAjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjoHCAAQRxCwAzoHCAAQsAMQQzo' \
              'GCAAQBxAeOgQIABANOgUIABCABEoECEEYAFCqwwRY08YEYNfIBGgBcAJ4AIABZ4gBuwKSAQMzLjGYAQCgAQHIAQrAAQE&sclient=' \
              'gws-wiz'
    # Фунт стерлингов
    FST_RUB = 'https://www.google.ru/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%84%D1%83%D0%BD%D1%82+%D1%81%D1%82%D0%B5%D1' \
              '%80%D0%BB%D0%B8%D0%BD%D0%B3%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&newwindow=1&sxsrf=AOaemvJjnoIl' \
              'AnrpQDRDtyQVYPbwisyavg%3A1633955192204&ei=eC1kYb2FDOKErwTHgoOABQ&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%84%D1' \
              '%83%D0%BD%D1%82+%D1%81%D1%82%D0%B5%D1%80%D0%BB%D0%B8%D0%BD%D0%B3%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB' \
              '%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMYADIJCCMQJxBGEIICMgoIABCABBCHAhAUMggIABCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCA' \
              'BDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEOoCECc6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARCjAjoECCMQJzoEC' \
              'AAQQzoHCAAQsQMQQzoHCAAQyQMQQzoNCAAQgAQQhwIQsQMQFEoECEEYAFDBJljbOGDtPWgBcAJ4AIABaYgB9ASSAQM3LjGYAQCgAQG' \
              'wAQrAAQE&sclient=gws-wiz'
    # Швецарский франк
    SHF_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+idtwfhcrbq+ahfyr+%D0%BA+%D1%80%D1%83%D0%B1%D0' \
              '%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvKW8a95ox1av70KeBF14JqaF5KDwg%3A1633949798312&ei=ZhhkYc2' \
              '1EpLargSYobfQBg&ved=0ahUKEwjNgLyqmcLzAhUSrYsKHZjQDWoQ4dUDCA4&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+idtwfh' \
              'crbq+ahfyr+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMyCQgAEA0QRhCCAjIICAAQDRAFEB4yCA' \
              'gAEAgQDRAeOgcIABBHELADOgYIABAHEB46BAgAEA06BQgAEM0CSgQIQRgAUJDCBVi86wVg1-wFaANwAngAgAGWAYgB1AqSAQQxNC4y' \
              'mAEAoAEByAEIwAEB&sclient=gws-wiz'
    # Иена
    IEN_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B8%D0%B5%D0%BD+%D0%BA+%D1%80%D1%83%D0%B1%' \
              'D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvJonlm3PLmMMHDdPj3Ts5Dm1uEZDA%3A1633949895013&ei=xxhkY' \
              'acO7KOuBIqRofAL&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B8%D0%B5%D0%BD+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&g' \
              's_lcp=Cgdnd3Mtd2l6EAMYADIECAAQDTIECAAQDTIGCAAQDRAeMgYIABANEB4yBggAEA0QHjIICAAQDRAFEB4yCAgAEAgQDRAeMgoI' \
              'ABAIEA0QChAeOgcIABBHELADOgYIABAHEB46CAgAEAcQChAeSgQIQRgAUNHIBFjiywRg7NoEaABwAngAgAFpiAHxAZIBAzIuMZgBAK' \
              'ABAcgBCMABAQ&sclient=gws-wiz'
    # Авст доллар
    AVD_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%B2%D1%81%D1%82%D1%80%D0%B0%D0%BB%D0' \
              '%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83' \
              '%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvKmncuGJ2TwrTkhFg8CSKOQ0CPFRA%3A1633949973005&e' \
              'i=FBlkYcvyPOumrgSaxr3wBg&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B0%D0%B2%D1%81%D1%82%D1%80%D0%B0%D0%BB%D0%B8%' \
              'D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%' \
              'B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMYADIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQ' \
              'HjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIICAAQCBAHEB46BwgAEEcQsAM6BwgAELADEEM6BAgAEA1KBAhBGABQgYEFWNOHBWCYjg' \
              'VoBHACeACAAU2IAZYCkgEBNJgBAKABAcgBCsABAQ&sclient=gws-wiz'
    # Гонконский доллар
    GOD_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B3%D0%BE%D0%BD%D0%BA%D0%BE%D0%BD%D0%B3+%D' \
              '0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU89' \
              '3&sxsrf=AOaemvKlYA8VkGzLfraDPzRkUoQw4tTdQw%3A1633950057399&ei=aRlkYeTkF62SrgSfx5u4BQ&oq=%D0%BA%D1%83%D' \
              '1%80%D1%81+%D0%B3%D0%BE%D0%BD%D0%BA%D0%BE%D0%BD%D0%B3+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%B' \
              'A+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMYATIGCAAQDRAeMggIABAIEA0QHjoHCAAQRxCwAzoHCAAQsA' \
              'MQQzoECAAQDToGCAAQBxAeOggIABAHEAoQHjoFCAAQzQJKBAhBGABQ7aIDWKy0A2DPwgNoAXACeACAAZEBiAHBA5IBAzQuMZgBAKAB' \
              'AcgBCsABAQ&sclient=gws-wiz'
    # ринггит
    RIN_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%80%D0%B8%D0%BD%D0%B3%D0%B3%D0%B8%D1%82+%D' \
              '0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvJBwPDYxUk5CDQ7UTJT7XYb0ABXaQ%' \
              '3A1633950115755&ei=oxlkYfLELef1qwGwq6KQBA&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%80%D0%B8%D0%BD%D0%B3%D0%B3%D' \
              '0%B8%D1%82+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMYADIGCAAQDRAeMggIABAIEA0QHjIICA' \
              'AQCBANEB4yCAgAEAgQDRAeOgcIABBHELADOgYIABAHEB46CAgAEAcQChAeOgoIABAIEAcQChAeOggIABAIEAcQHjoECAAQDUoECEEY' \
              'AFD1zQ1YnNsNYIXhDWgDcAJ4AIABkgGIAYgEkgEDNS4xmAEAoAEByAEIwAEB&sclient=gws-wiz'
    # Гульден
    GUL_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B3%D1%83%D0%BB%D1%8C%D0%B4%D0%B5%D0%BD+%D' \
              '0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvJXTra7KDRL1OYzExbHpmkDsZz0_w%' \
              '3A1633950341925&ei=hRpkYczkN_SGwPAPq6mu0AU&ved=0ahUKEwiMu9etm8LzAhV0AxAIHauUC1oQ4dUDCA4&uact=5&oq=%D0%' \
              'BA%D1%83%D1%80%D1%81+%D0%B3%D1%83%D0%BB%D1%8C%D0%B4%D0%B5%D0%BD+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&' \
              'gs_lcp=Cgdnd3Mtd2l6EAMyBggAEAcQHjIICAAQCBAHEB4yBggAEAgQHjoHCAAQRxCwAzoECAAQDUoECEEYAFCJ_QRY8YUFYIOKBWg' \
              'BcAJ4AIABmgGIAboEkgEDNi4xmAEAoAEByAEIwAEB&sclient=gws-wiz'
    # Лари
    LAR_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%BB%D0%B0%D1%80%D0%B8+%D0%BA+%D1%80%D1%83%' \
              'D0%B1%D0%BB%D1%8E&rlz=1C1CHBD_ruRU893RU893&sxsrf=AOaemvKsJMhX6pkT7saOSVUJkOHT5tV9gw%3A1633950425815&ei' \
              '=2RpkYa2bMaeMrwS594rAAw&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%BB%D0%B0%D1%80%D0%B8+%D0%BA+%D1%80%D1%83%D0%B1' \
              '%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAEYADIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDT' \
              'IECAAQDTIECAAQDToHCAAQRxCwAzoGCAAQDRAeOggIABANEAUQHjoICAAQCBANEB5KBAhBGABQl_ADWPjyA2Cn-wNoAXACeACAAU-I' \
              'AaYCkgEBNJgBAKABAcgBBMABAQ&sclient=gws-wiz'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/94.0.4606.71 Safari/537.36'}

    def parse_currency(self, c):
        """парсит страничку со значениями"""
        if c == 'd':
            full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'e':
            full_page = requests.get(self.EURO_RUB, headers=self.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'dir':
            full_page = requests.get(self.DIR_RUB, headers=self.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'dra':
            full_page = requests.get(self.DRA_RUB, headers=self.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'lir':
            full_page = requests.get(self.LIR_RUB, headers=self.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'pes':
            full_page = requests.get(self.PES_RUB, headers=self.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'bat':
            full_page = requests.get(self.BAT_RUB, headers=self.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'fst':
            full_page = requests.get(self.FST_RUB, headers=self.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'shf':
            full_page = requests.get(self.SHF_RUB, headers=self.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'ien':
            full_page = requests.get(self.IEN_RUB, headers=self.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'avd':
            full_page = requests.get(self.AVD_RUB, headers=self.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'god':
            full_page = requests.get(self.GOD_RUB, headers=self.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'rin':
            full_page = requests.get(self.RIN_RUB, headers=self.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'gul':
            full_page = requests.get(self.GUL_RUB, headers=self.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'lar':
            full_page = requests.get(self.LAR_RUB, headers=self.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'y' or 'юань':
            full_page = requests.get(self.CNY_RUB, headers=self.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        else:
            return '404 Error'

    def parse_currency2(self, val):
        """Я просто не знаю, как подругому избавиться от повторения кода"""
        soup = BeautifulSoup(val.content, 'html.parser')  # Разбираем через BeautifulSoup
        convert = soup.findAll("span", {"class": "SwHCTb", "data-precision": 2})  # Получаем нужное для нас значение
        return convert[0].text


def main(info):
    """Основная функция"""
    cur = Currency()
    result = cur.parse_currency(info)
    return result


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=2)  # Запускаем постоянный опрос бота в Телеграме
