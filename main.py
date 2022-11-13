import telebot
from local_settings import BOT_TOKEN, currencies
from extensions import *
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    greet = 'Вас приветствует бот-конвертер валют! Для справки введите команду "/help"'

    bot.send_message(message.chat.id, greet)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Для конвертаци доступны валюты:\n'
    for currency in currencies.keys():
        text = '\n'.join((text, currency)) + ' - ' + currencies[currency]

    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def helper(message: telebot.types.Message):
    help_text = 'Для вывода списка доступных валют введите команду "/values".\n\n Для конвертации введите через пробел:\n\n1. <имя валюты цену которой надо узнать> \
    \n2. <имя валюты в которой надо узнать цену первой валюты>\n3. <количество первой валюты>\n\n Например, чтобы узнать цену 123.5 долларов в рублях введите:\n "USD RUB 123.5"'

    bot.send_message(message.chat.id, help_text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException('Неверное количество параметров!')

        answer = Converter.get_price(*values)
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Неправильно указана валюта или сумма: {e}")
    else:
        bot.reply_to(message, answer)


bot.polling()
