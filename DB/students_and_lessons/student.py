import random
import sqlite3
from faker import Faker


def create_base(name='students'):
    with sqlite3.connect('database.db') as db:
        db.execute('PRAGMA foreign_keys = ON')
        cursor = db.cursor()
        query = f""" CREATE TABLE IF NOT EXISTS {name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT,
        second_name TEXT,
        surname TEXT,
        favorite_teacher INTEGER,
        FOREIGN KEY (favorite_teacher) REFERENCES lessons (id) )"""
        cursor.execute(query)


def clear_base(name='students'):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = f""" DROP TABLE IF EXISTS {name}"""
        cursor.execute(query)
        db.commit()


def add_students_in_base(count_of_students=20, name='students'):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()

        person = Faker('ru_RU')
        for i in range(count_of_students):
            query = f"""INSERT INTO {name} (name, second_name, surname) VALUES (?,?,?)"""
            cursor.execute(query,
                           (person.first_name(), person.middle_name(), person.last_name()))

        db.commit()


def records_students(name='students'):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = f"""SELECT id FROM {name}"""
        cursor.execute(query)
        result = cursor.fetchall()

        for i in result:
            query = f"""UPDATE {name} SET favorite_teacher = {random.randint(1, 5)} WHERE id = {i[0]}"""
            cursor.execute(query)
        db.commit()


def group_students(number=1):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = f"""SELECT * FROM students WHERE favorite_teacher = {number}"""
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
