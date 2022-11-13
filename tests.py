"""
Тесты
"""

# import requests
# from local_settings import API_KEY
# from extensions import Converter
# from extensions import *

# ------------- Подключение -------------------------------------------------------------------------
# base = 'USD'
# quote = 'RUB'
# amount = 100
# data = requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base}').json()
# print(data)
# ------------- / Подключение------------------------------------------------------------------------
# ------------- Получение данных ------------------------------------------------------------------------
# base_rate = data['conversion_rates'][quote]
# amount_price = data['conversion_rates'][quote] * float(amount)
# print(base_rate)
# print(amount_price)
# ------------- / Получение данных ------------------------------------------------------------------------
# ------------- Класс-конвертер --------------------------------------------------------------------------
# values = ['USD', quote, amount]
# print(values)
# data = Converter.get_price(*values)
# print(data)
# ------------- / Класс-конвертер ------------------------------------------------------------------------
# ------------- Exceptions ------------------------------------------------------------------------
# values = ['usd', 'RUB', 100]
# values = ['рубль', 'доллар', 100]
# values = ['USD', 'USD', 100]
# values = ['USD', 'EUR', 12,5]
# answer = Converter.get_price(*values)
# print(answer)
# ------------- / Exceptions ------------------------------------------------------------------------
