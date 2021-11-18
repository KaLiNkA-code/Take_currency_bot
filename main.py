from telebot import types  # Импортируем типы из модуля, чтобы создавать кнопки
import telebot  # Подключаем модуль для Телеграма
from k import k
import parse

bot = telebot.TeleBot(k)  # Указываем токен


@bot.message_handler(commands=["start"])
def inline(message):
    key = types.InlineKeyboardMarkup()
    """/start"""
    but_1 = types.InlineKeyboardButton(text="курс валюты", callback_data="currency")
    but_2 = types.InlineKeyboardButton(text="страна - валюта", callback_data="Country")
    key.add(but_1, but_2)
    bot.send_message(message.chat.id, "Что бы вы хотели?)", reply_markup=key)
    """/start  """


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


def main(info):
    """Основная функция"""
    cur = parse.Currency()
    result = cur.parse_currency(info)
    return result


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=2)  # Запускаем постоянный опрос бота в Телеграме
