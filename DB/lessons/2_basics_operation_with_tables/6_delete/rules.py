import sqlite3

# Команда DELETE удаляет данные из БД. :


with sqlite3.connect('db_delete.db') as db:
    cursor = db.cursor()
    cursor.execute("""DROP TABLE IF EXISTS Product""")
    db.commit()

# создадим таблицу
with sqlite3.connect('db_delete.db') as db:
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

with sqlite3.connect('db_delete.db') as db:
    # записать
    cursor = db.cursor()
    query = """INSERT OR IGNORE INTO Product (name, product_count, price) VALUES (?, ?, ?)"""
    cursor.executemany(query, data)
    db.commit()

    # посмотреть
    query = """SELECT * FROM Product"""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

# пример 1
with sqlite3.connect('db_delete.db') as db:
    cursor = db.cursor()
    query = """DELETE FROM Product WHERE name = ?"""  # удалим по имени (имя ниже)
    cursor.execute(query, ('apple',))
    db.commit()

    query = """SELECT * FROM Product"""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

# пример 2
with sqlite3.connect('db_delete.db') as db:
    cursor = db.cursor()
    query = """DELETE FROM Product WHERE price <5"""  # удалим все что меньше 5 по цене
    cursor.execute(query)
    db.commit()

    query = """SELECT * FROM Product"""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
