import telebot
import os

from db import Database
from markups import create_sex_markup

API_TOKEN = os.getenv('TOKEN', 'token')

bot = telebot.TeleBot(API_TOKEN)
db = Database()


@bot.message_handler(commands=['start'])
def start_questions(message):
    return bot.reply_to(message, 'Введіть ваше ім\'я')


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    markup = create_sex_markup()
    bot.reply_to(message, 'Оберіть стать', reply_markup=markup)


bot.infinity_polling()
