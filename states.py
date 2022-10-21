from db import Database
from markups import create_sex_markup, create_main_markup, create_recipes_markup

database = Database()


def answer_name(bot, message):
    markup = create_sex_markup()
    state = State(bot, message.from_user.id)
    state.next(message.from_user.id)
    bot.send_message(message.chat.id, 'Оберіть стать', reply_markup=markup)


def answer_sex(bot, message):
    markup = create_main_markup()
    state = State(bot, message.from_user.id)
    data = state.get_data()
    database.create_user((
        message.from_user.first_name,
        message.from_user.last_name,
        message.from_user.username,
        data['set_name'],
        message.text,
        message.from_user.id
    ))
    state.next(message.from_user.id)
    bot.send_message(message.chat.id, 'Головне меню', reply_markup=markup)


def answer_mid_state(bot, message):
    if message.text == 'Про мене':
        user_info = database.get_user_info(message.chat.id)
        text = f"""
        Ім\'я: <b>{user_info[1]}</b>
Прізвище: <b>{user_info[2]}</b>
Юзернейм: <b>{user_info[3]}</b>
Ім\'я, вказане у анкеті: <b>{user_info[5]}</b>
Стать: <b>{user_info[6]}</b>
        """
        return bot.send_message(message.chat.id, text, parse_mode='HTML')
    else:
        recipes = database.select_all_recipes()
        markup = create_recipes_markup(recipes)
        state = State(bot, message.from_user.id)
        state.next(message.from_user.id)
        return bot.send_message(message.chat.id, 'Оберіть рецепт', reply_markup=markup)


def answer_recipe(bot, message):
    recipe = database.get_recipe_info(message.text)
    photo = open('./recipes/media/' + recipe[3], 'rb')
    return bot.send_photo(message.chat.id, photo, recipe[2])


class State:
    states = {
        'set_name': {
            'method': answer_name,
            'data': None
        },
        'set_sex': {
            'method': answer_sex,
            'data': None
        },
        'mid_state': {
            'method': answer_mid_state,
            'data': None
        },
        'set_recipe': {
            'method': answer_recipe,
            'data': None
        },
    }

    def __init__(self, bot, user_id) -> None:
        self.bot = bot
        state_from_db = database.get_user_state(user_id)
        if state_from_db:
            self.active_state = state_from_db[2]
        else:
            first_state = list(self.states.keys())[0]
            database.create_user_state(user_id, first_state)
            self.active_state = first_state

    def set_state(self, state_name: str, user_id: int):
        if state_name in self.states.keys():
            self.active_state = state_name
            database.change_user_state(user_id, state_name)
            return
        raise Exception('Invalid state name')

    def set_data(self, message):
        active_state = self.states[self.active_state]
        active_state['data'] = message
        active_state['method'](self.bot, active_state['data'])

    def get_data(self):
        data = {}
        for key, value in self.states.items():
            if value['data']:
                data[key] = value['data'].text
        return data

    def add_state(self, state_name: str, method):
        self.states[state_name] = {'method': method, 'data': None}

    def first(self, user_id):
        database.change_user_state(user_id, list(self.states.keys())[0])
        self.active_state = list(self.states.keys())[0]

    def next(self, user_id):
        keys_list = list(self.states.keys()) 
        index = keys_list.index(self.active_state)
        if index + 1 == len(keys_list):
            self.set_state(keys_list[0], user_id)
        self.set_state(keys_list[index + 1], user_id)   

    def finish(self):
        for key in self.states.keys():
            self.states[key]['data'] = None
