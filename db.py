import sqlite3
from sqlite3 import Error
from typing import List


class Database:
    def __init__(self, db_file: str = 'recipes\db.sqlite3'):
        conn = None
        try:
            conn = sqlite3.connect(db_file, check_same_thread=False)
        except Error as e:
            raise Exception(e)
        self.conn = conn
        self.cur = self.conn.cursor()
    
    def select_all_recipes(self) -> List[tuple]:
        self.cur.execute("SELECT * FROM dashboard_recipe")
        rows = self.cur.fetchall()
        result = []
        for row in rows:
            result.append(row)
        return result

    def get_recipe_info(self, recipe_name: str) -> tuple:
        self.cur.execute("SELECT * FROM dashboard_recipe WHERE name=?", (recipe_name,))
        recipe = self.cur.fetchall()
        return recipe[0]
        
    def get_user_info(self, telegram_id: str) -> tuple:
        self.cur.execute("SELECT * FROM dashboard_telegramuser WHERE telegram_id=?", (telegram_id,))
        user = self.cur.fetchall()
        return user[0]

    def create_user(self, user) -> int:
        sql = '''INSERT INTO dashboard_telegramuser(name, surname, username, questioned_name, sex, telegram_id)
                VALUES(?,?,?,?,?,?)'''
        self.cur.execute(sql, user)
        self.conn.commit()
        return self.cur.lastrowid

    def get_user_state(self, telegram_id) -> int:
        self.cur.execute("SELECT * FROM dashboard_state WHERE telegram_id=?", (telegram_id,))
        user = self.cur.fetchall()
        if user:
            return user[0]
        return []

    def create_user_state(self, telegram_id, state_name) -> int:
        self.cur.execute('INSERT INTO dashboard_state(telegram_id, state) VALUES(?,?)', (telegram_id, state_name))
        self.conn.commit()
        return self.cur.lastrowid

    def change_user_state(self, telegram_id, state_name) -> int:
        self.cur.execute('UPDATE dashboard_state SET state = ? WHERE telegram_id = ?', (state_name, telegram_id))
        self.conn.commit()
