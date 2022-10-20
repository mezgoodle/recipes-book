import telebot
import os

from db import Database
from markups import create_sex_markup, create_recipes_markup

API_TOKEN = os.getenv('TOKEN', 'token')

bot = telebot.TeleBot(API_TOKEN)
db = Database()


@bot.message_handler(commands=['start'])
def start_questions(message):
    return bot.reply_to(message, 'Введіть ваше ім\'я')


@bot.message_handler(commands=['recipes'])
def show_recipies(message):
    recipes = db.select_all_recipes()
    markup = create_recipes_markup(recipes)
    return bot.reply_to(message, 'Оберіть рецепт', reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    recipe = db.get_recipe_info(message.text)
    photo = open('./recipes/media/' + recipe[3], 'rb')
    return bot.send_photo(message.chat.id, photo, recipe[2])
    # markup = create_sex_markup()
    # bot.reply_to(message, 'Оберіть стать', reply_markup=markup)


bot.infinity_polling()
