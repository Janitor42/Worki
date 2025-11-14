import random
import sqlite3

lessons_data = [
    ('Математика', 'Иванов И.И.'),
    ('Физика', 'Петров П.П.'),
    ('Химия', 'Сидорова С.С.'),
    ('История', 'Козлова К.К.'),
    ('Литература', 'Николаева Н.Н.')
]


def clear_base(name='lessons'):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = f""" DROP TABLE IF EXISTS {name}"""
        cursor.execute(query)
        db.commit()


def create_base(name='lessons'):
    with sqlite3.connect('database.db') as db:
        db.execute('PRAGMA foreign_keys = ON')
        cursor = db.cursor()
        query = f""" CREATE TABLE IF NOT EXISTS '{name}'
        (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, 
        name TEXT,
        name_teacher TEXT,
        price REAL)
        """
        cursor.execute(query)
        db.commit()


def add_teachers(name='lessons'):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        for title, teacher in lessons_data:
            query = f"""INSERT INTO '{name}' (name, name_teacher) VALUES (?, ?)"""
            cursor.execute(query, (title, teacher))
        db.commit()


def set_price(name='lessons'):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = f"""SELECT id FROM '{name}'"""
        cursor.execute(query)
        result = cursor.fetchall()

        for i in result:
            query = f"""UPDATE {name} SET price = ? WHERE id = ?"""
            cursor.execute(query, (random.randint(1000, 3000), i[0]))
            db.commit()



