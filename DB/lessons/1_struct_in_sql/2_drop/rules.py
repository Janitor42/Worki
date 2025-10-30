import time

import sqlite3

with sqlite3.connect('db_drop.db') as db:
    cursor = db.cursor()
    query = f"""CREATE TABLE IF NOT EXISTS Test (
field1 TEXT, field2 TEXT, field102 TEXT)"""
    cursor.execute(query)
    db.commit()

with sqlite3.connect('db_drop.db') as db:
    cursor = db.cursor()
    query = f'DROP TABLE IF EXISTS Test' #простой запрос на удаление таблицы (опять же с доп проверкой на то что она есть)
    db.commit()

#файл есть но в нем отсутвует таблица Test
