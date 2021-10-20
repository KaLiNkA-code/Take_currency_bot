import requests
from bs4 import BeautifulSoup

"""This is a part of code for parse currency pages"""


class Currency:
    """Класс для работ по курсу"""

    def parse_currency(self, c):
        import mainDataBase
        """парсит страничку со значениями"""
        if c == 'd':
            full_page = requests.get(mainDataBase.DOLLAR_RUB, headers=mainDataBase.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'e':
            full_page = requests.get(mainDataBase.EURO_RUB, headers=mainDataBase.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'dir':
            full_page = requests.get(mainDataBase.DIR_RUB, headers=mainDataBase.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'dra':
            full_page = requests.get(mainDataBase.DRA_RUB, headers=mainDataBase.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'lir':
            full_page = requests.get(mainDataBase.LIR_RUB, headers=mainDataBase.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'pes':
            full_page = requests.get(mainDataBase.PES_RUB, headers=mainDataBase.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'bat':
            full_page = requests.get(mainDataBase.BAT_RUB, headers=mainDataBase.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'fst':
            full_page = requests.get(mainDataBase.FST_RUB, headers=mainDataBase.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'shf':
            full_page = requests.get(mainDataBase.SHF_RUB, headers=mainDataBase.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'ien':
            full_page = requests.get(mainDataBase.IEN_RUB, headers=mainDataBase.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'avd':
            full_page = requests.get(mainDataBase.AVD_RUB, headers=mainDataBase.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'god':
            full_page = requests.get(mainDataBase.GOD_RUB, headers=mainDataBase.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'rin':
            full_page = requests.get(mainDataBase.RIN_RUB, headers=mainDataBase.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'gul':
            full_page = requests.get(mainDataBase.GUL_RUB, headers=mainDataBase.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'lar':
            full_page = requests.get(mainDataBase.LAR_RUB, headers=mainDataBase.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        elif c == 'y' or 'юань':
            full_page = requests.get(mainDataBase.CNY_RUB, headers=mainDataBase.headers)  # Парсим всю страницу
            return self.parse_currency2(full_page)
        else:
            return '404 Error'  # random error, but lucks like good AHAHHAHAHAHHA

    def parse_currency2(self, val):
        """Я просто не знаю, как подругому избавиться от повторения кода"""
        soup = BeautifulSoup(val.content, 'html.parser')  # Разбираем через BeautifulSoup
        convert = soup.findAll("span", {"class": "SwHCTb", "data-precision": 2})  # Получаем нужное для нас значение
        return convert[0].text
