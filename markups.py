from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def create_sex_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    male_gender = KeyboardButton('Чоловіча')
    female_gender = KeyboardButton('Жіноча')
    markup.add(male_gender, female_gender)
    return markup

