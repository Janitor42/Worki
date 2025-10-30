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
        cursor = db.cursor()
        query = f""" CREATE TABLE IF NOT EXISTS '{name}' (
name TEXT, name_teacher TEXT) """
        cursor.execute(query)
        db.commit()


def add_teachers(name='lessons'):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        for title, teacher in lessons_data:
            query = f"""INSERT INTO '{name}' (name, name_teacher) VALUES (?, ?)"""
            cursor.execute(query, (title, teacher))
        db.commit()
