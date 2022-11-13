import requests
from local_settings import currencies, API_KEY

"""
Классы исключений
"""


class APIException(Exception):
    def __str__(self):
        return 'Ошибка получения данных. Воспользуйтесь командами "/values" и "/help"'


class WrongCodeException(Exception):
    def __str__(self):
        return 'Ошибка получения данных. Неверно уканан код валюты. Воспользуйтесь командой "/values"'


class SameCodeException(Exception):
    def __str__(self):
        return 'Ошибка получения данных. Указан одинаковый код валюты. Для конвертации укажите разные валюты.'


class AmountException(Exception):
    def __str__(self):
        return 'Ошибка получения данных. Воспользуйтесь командами "/values" и "/help"'


"""
Класс-конвертер валют. 
Имеет статический метод get_price, принимает три аргумента: имя валюты, цену на которую надо узнать, — base, имя валюты, цену в которой надо узнать, — quote, \
количество переводимой валюты — amount и возвращает нужную сумму в валюте.
"""


class Converter:

    @staticmethod
    def get_price(base, quote, amount):
        # -------------------------------------
        try:
            base not in currencies.values()
        except ValueError:
            raise WrongCodeException(f'Неверно указана валюта {base}')

        try:
            quote not in currencies.values()
        except ValueError:
            raise WrongCodeException(f'Неверно указана валюта {quote}')

        if base == quote:
            raise SameCodeException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise AmountException(f'Не удалось обработать количество {amount}!')

        data = requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base}').json()
        base_rate = data['conversion_rates'][quote]
        amount_price = data['conversion_rates'][quote] * float(amount)
        message = f"Цена 1 {base} : {round(base_rate, 3)} {quote}\n {amount} {base} в {quote} стоит {round(amount_price, 3)}"
        return message
