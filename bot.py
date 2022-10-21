import telebot
import os

from db import Database
from states import State

API_TOKEN = os.getenv('TOKEN', '5135575762:AAHdGW6cidFikmIKMKPVZjEpS0e8iAsmEwg')

bot = telebot.TeleBot(API_TOKEN)
db = Database()


@bot.message_handler(commands=['start'])
def start_questions(message):
    state = State(bot, message.from_user.id)
    state.first(message.from_user.id)
    return bot.reply_to(message, 'Введіть ваше ім\'я')


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    state = State(bot, message.from_user.id)
    state.set_data(message)


bot.infinity_polling()
