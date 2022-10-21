from typing import List
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def create_sex_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    male_gender = KeyboardButton('Чоловіча')
    female_gender = KeyboardButton('Жіноча')
    markup.add(male_gender, female_gender)
    return markup


def create_main_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    first_btn = KeyboardButton('Про мене')
    second_btn = KeyboardButton('Рецепти')
    markup.add(first_btn, second_btn)
    return markup


def create_recipes_markup(recipes: List[tuple]):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for recipe in recipes:
        recipe_btn = KeyboardButton(recipe[1])
        markup.add(recipe_btn)
    return markup
