import sqlite3
from faker import Faker


def create_base(name='students'):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = f""" CREATE TABLE IF NOT EXISTS {name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        second_name TEXT,
        surname TEXT)"""
        cursor.execute(query)


def clear_base(name='students'):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = f""" DROP TABLE IF EXISTS {name}"""
        cursor.execute(query)
        db.commit()


def add_students_in_base(value=20, name='students'):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()

        person = Faker('ru_RU')
        for i in range(value):
            query = f"""INSERT INTO {name} (name, second_name, surname) VALUES (?,?,?)"""
            cursor.execute(query,
                           (person.first_name(), person.middle_name(), person.last_name()))

        db.commit()
