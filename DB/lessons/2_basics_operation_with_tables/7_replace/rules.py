# Команда REPLACE по сути является сокращением от INSERT OR REPLACE.
# Ее идея состоит в следующем.
# При вставке данных может нарушаются ограничения UNIQUE или PRIMARY KEY, например,
# когда мы пытаемся добавить для столбца, который должен иметь уникальные значения, данные,
# которые уже есть в таблице. Этот конфликт ограничений призвана разрешить команда REPLACE.

# Эта команда сначала удаляет строку, которая вызвала конфликт на уникальность данных,
# и затем вместо нее вставляет новую строку. То есть фактически все выглядит как замена строки.

# Если конфликтов с ограничениями не происходит, то команда REPLACE по сути действует аналогично команде INSERT.

import sqlite3

with sqlite3.connect('db_replace.db') as db:
    cursor = db.cursor()
    cursor.execute("""DROP TABLE IF EXISTS Product""")
    db.commit()

# создадим таблицу
with sqlite3.connect('db_replace.db') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS Product
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    product_count INTEGER,
    price REAL)"""
    cursor.execute(query)
    db.commit()

data = [
    ('apple', 3, 3.44),
    ('banana', 2, 2.45),
    ('plump', 2, 4),
    ('strawberry', 1, 8.25),
    ('watermelon', 5, 2.95)
]

# пробуем добавить новое яблоко обычным INSERT
with sqlite3.connect('db_replace.db') as db:
    cursor = db.cursor()
    query = """INSERT INTO Product (name, product_count, price) VALUES (?, ?, ?)"""
    cursor.executemany(query, data)
    db.commit()

    query = """SELECT * FROM Product"""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    try:
        query = """INSERT INTO Product (name, product_count, price) VALUES (?, ?, ?)"""
        cursor.execute(query, ('apple', 3, 3.44))
    except:
        print('ошибка уникальное имя уже существует')

    query = """SELECT * FROM Product"""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

# а теперь применим REPLACE
#Эта команда удалить ранее добавленную стоку, и вставит текущие данные:
with sqlite3.connect('db_replace.db') as db:
    cursor = db.cursor()
    query = """REPLACE INTO Product (name, product_count, price) VALUES (?, ?, ?)"""
    cursor.execute(query, ('apple', 100, 100.0))
    db.commit()

    query = """SELECT * FROM Product"""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
