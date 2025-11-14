import sqlite3
import faker

# table People
with sqlite3.connect('db_insert.db') as db:
    cursor = db.cursor()
    query = """DROP TABLE IF EXISTS People"""
    cursor.execute(query)
    db.commit()

with sqlite3.connect('db_insert.db') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS People
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    email TEXT)"""
    cursor.execute(query)
    db.commit()

with sqlite3.connect('db_insert.db') as db:
    cursor = db.cursor()
    query = """INSERT INTO People(name,surname, email) VALUES('Василий','Васильев','15')"""
    cursor.execute(query)
    db.commit()

# """INSERT INTO People(name, email) VALUES('Василий','15')"""
# После названия таблицы указываны два стобца, в которые мы хотим выполнить добавление данные - (name, email).
# После оператора VALUES указаны значения для этих столбцов.
# Значения будут передаваться столбцам по позиции.
# То есть стобцу name передается строка "Василий', столбцу email - число Vas@mail.com.
# И после успешного выполнения данной команды в таблице появится новая строка:

# !!!! используйте всегда так:
with sqlite3.connect('db_insert.db') as db:
    cursor = db.cursor()
    query = """INSERT INTO People(name,surname, email) VALUES(?,?,?)"""
    cursor.execute(query, ('Иван', 'Иванов', 'Iva@mail.com'))
    db.commit()

# Добавление NULL
# Также мы можем опускать при добавлении такие столбцы, которые поддерживают значение NULL
# (которые не имеют ограничения NOT NULL):
# инекция добавила Петра но в email мы добавили NULL автоматом
with sqlite3.connect('db_insert.db') as db:
    cursor = db.cursor()
    query = """INSERT INTO People(name,surname) VALUES(?,?)"""
    cursor.execute(query, ('Петр', 'Петров'))
    db.commit()

# Значения по умолчанию
# Если для столбца задано ограничение DEFAULT,
# то есть значение по умолчанию, то для него тоже можно не передавать значение.
# Например, возьмем следующую таблицу:

# table People2
with sqlite3.connect('db_insert.db') as db:
    cursor = db.cursor()
    query = """DROP TABLE IF EXISTS People2"""
    cursor.execute(query)
    db.commit()

with sqlite3.connect('db_insert.db') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS People2
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT ,
    surname TEXT  DEFAULT 'Undefined',
    email TEXT DEFAULT 'DONT HAVE COMPUTER')"""
    cursor.execute(query)
    db.commit()

# Теперь столбцы surname и email имеют значения по умолчанию. При добавлении данных из можно опустить:
with sqlite3.connect('db_insert.db') as db:
    cursor = db.cursor()
    query = """INSERT INTO People2(name,email) VALUES(?,?)"""
    cursor.execute(query, ('Иван', 'Ivan@mail.com'))

    query = """INSERT INTO People2(name,surname) VALUES(?,?)"""
    cursor.execute(query, ('Петр', 'Петренко'))
    db.commit()

# Множественное добавление
# можем создать свои данные для множественного добавления но я буду использовать faker (лень)

fake_people = faker.Faker()
data = [
    (fake_people.first_name(), fake_people.last_name(), fake_people.email()),
    (fake_people.first_name(), fake_people.last_name(), fake_people.email()),
    (fake_people.first_name(), fake_people.last_name(), fake_people.email())
]

with sqlite3.connect('db_insert.db') as db:
    cursor = db.cursor()
    query = """INSERT INTO People2(name,surname,email) VALUES(?,?,?)"""
    cursor.executemany(query, data)  # метод который берет список и идет по нему открывая его и делая множественное add


# Динамическая типизация
# Стоит отметить, что в SQLite (в отличие от многих других популярных систем баз данных)
# действует динамическая типизиация. Например, возьмем выше использованную таблицу:
with sqlite3.connect('db_insert.db') as db:
    cursor = db.cursor()
    query = """INSERT INTO People2(name,email) VALUES(?,?)"""
    cursor.execute(query, (34.12, 109))
    db.commit()



