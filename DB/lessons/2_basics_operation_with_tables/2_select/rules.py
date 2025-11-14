# Для получения данных в SQLite применяется команда SELECT.
import sqlite3
import faker

# table People
with sqlite3.connect('db_select.db') as db:
    cursor = db.cursor()
    query = """DROP TABLE IF EXISTS People"""
    cursor.execute(query)
    db.commit()

# создаем таблицу
with sqlite3.connect('db_select.db') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS People
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    email TEXT)"""
    cursor.execute(query)
    db.commit()

# создаем данные для работы
fake_people = faker.Faker('RU_ru')
data = [
    (fake_people.first_name(), fake_people.last_name(), fake_people.email()),
    (fake_people.first_name(), fake_people.last_name(), fake_people.email()),
    (fake_people.first_name(), fake_people.last_name(), fake_people.email())
]
with sqlite3.connect('db_select.db') as db:
    cursor = db.cursor()
    query = """INSERT INTO People(name,surname,email) VALUES(?,?,?)"""
    cursor.executemany(query, data)
    db.commit()

with sqlite3.connect('db_select.db') as db:
    cursor = db.cursor()
    query = """SELECT * FROM People"""  # звездочка указывает что берем все
    cursor.execute(query)

    result = cursor.fetchall()  # получить и положить в result все что делал cursor
    ###!!! альтернативные способы взять из cursor

    # cursor.fetchone() - взять 1 запись
    # cursor.fetchmany(2) - взять несколько (2) записи
    # cursor.fetchall() - взять оставшиеся записи
    for row in result:  # показываем как это выглядит
        print(row)
    db.commit()

print('-' * 60)

with sqlite3.connect('db_select.db') as db:
    cursor = db.cursor()
    query = """SELECT surname,email FROM People"""  # а вот здесь берем что то конкретное (по полям)
    cursor.execute(query)

    result = cursor.fetchall()
    for row in result:  # показываем как это выглядит
        print(row)

    db.commit()

# создадим другую таблицу  #
with sqlite3.connect('db_select.db') as db:
    cursor = db.cursor()
    query = """DROP TABLE IF EXISTS Product"""
    cursor.execute(query)
    db.commit()

with sqlite3.connect('db_select.db') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS Product
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    product_count INTEGER)"""
    cursor.execute(query)
    db.commit()

data = [
    ('iPhone 13', 3, 76000),
    ('iPhone 12', 2, 51000),
    ('Galaxy S21', 2, 56000),
    ('Galaxy S20', 1, 41000),
    ('P40 Pro', 5, 36000)
]

with sqlite3.connect('db_select.db') as db:
    cursor = db.cursor()
    query = """INSERT INTO Product(name,price,product_count) VALUES(?,?,?)"""
    cursor.executemany(query, data)
    db.commit()

with sqlite3.connect('db_select.db') as db:
    cursor = db.cursor()
    query = """SELECT name, product_count*price FROM Product"""  # выбираем и сразу же умножаем (математика внутри запроса)
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)
    db.commit()
