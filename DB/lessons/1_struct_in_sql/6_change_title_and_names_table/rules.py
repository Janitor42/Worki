import sqlite3

with sqlite3.connect('db_change_titles_and_tables.db') as db:
    cursor = db.cursor()
    query = f"""CREATE TABLE IF NOT EXISTS Companies (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL);

CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
company_id INTEGER
)"""
    cursor.executescript(query)
    db.commit()

#после этого есть 2 таблицы *Companies Users


with sqlite3.connect('db_change_titles_and_tables.db') as db:
    cursor = db.cursor()
    query = f"""ALTER TABLE Companies
RENAME TO Groups"""
    cursor.executescript(query)
    db.commit()

#"ALTER TABLE Companies RENAME TO Groups - после этого таблица сменила название


with sqlite3.connect('db_change_titles_and_tables.db') as db:
    cursor = db.cursor()
    query = f"""ALTER TABLE Users ADD COLUMN email TEXT NOT NULL"""
    cursor.executescript(query)
    db.commit()
#Добавим в таблицу Users новый столбец emai
# В данном случае столбец email имеет тип TEXT и для него определено ограничение NOT NULL.


with sqlite3.connect('db_change_titles_and_tables.db') as db:
    cursor = db.cursor()
    query = f"""ALTER TABLE Users RENAME COLUMN email TO login"""
    cursor.executescript(query)
    db.commit()
# Переименуем столбец email в login


with sqlite3.connect('db_change_titles_and_tables.db') as db:
    cursor = db.cursor()
    query = f"""ALTER TABLE Users DROP COLUMN login"""
    cursor.executescript(query)
    db.commit()
#удалить столбец (нужна свежая версия питона)