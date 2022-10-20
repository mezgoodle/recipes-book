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
        
    def get_user_info(self, tg_id: str) -> tuple:
        self.cur.execute("SELECT * FROM dashboard_telegramuser WHERE telegram_id=?", (tg_id,))
        user = self.cur.fetchall()
        return user[0]

    def create_user(self, user) -> int:
        sql = '''INSERT INTO telegramuser(name, surname, username, questioned_name, sex, telegram_id)
                VALUES(?,?,?,?,?,?)'''
        self.cur.execute(sql, user)
        self.conn.commit()
        return self.cur.lastrowid
