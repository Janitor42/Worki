import sqlite3

# cоздадим и заполним таблицу
with sqlite3.connect('db_where.db') as db:
    cursor = db.cursor()
    query = """DROP TABLE IF EXISTS Product"""
    cursor.execute(query)
    db.commit()

with sqlite3.connect('db_where.db') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS Product
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
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

# запишем в нее данные
with sqlite3.connect('db_where.db') as db:
    cursor = db.cursor()
    query = """INSERT INTO Product(name,price,product_count) VALUES(?,?,?)"""
    cursor.executemany(query, data)
    db.commit()

# Нередко при получении данных из БД
# выбираются только те данные, которые соответствуют некоторому определенному условию.
# Для фильтрации данных в команде SELECT применяется оператор WHERE, после которого указывается условие:

# =: сравнение на равенство
# !=: сравнение на неравенство
# <>: сравнение на неравенство
# <: меньше чем
# >: больше чем
# <=: меньше чем или равно
# >=: больше чем или равно


with sqlite3.connect('db_where.db') as db:
    cursor = db.cursor()
    query = """SELECT * FROM Product WHERE name = ?"""  # запрос и сравнение на то что мы ищем
    cursor.execute(query, ('apple',))  # сюда параметр
    result = cursor.fetchall()
    print(result)

    query = """SELECT * FROM Product WHERE price >= ?"""
    cursor.execute(query, ('5',))  # ищем все что больше 5 по стоимости

    result = cursor.fetchall()
    print(result)

print('-' * 60)

with sqlite3.connect('db_where.db') as db:
    cursor = db.cursor()
    query = """SELECT * FROM Product WHERE product_count*price>10"""  # сразу логика и математика в запросе
    cursor.execute(query)  # сюда параметр
    result = cursor.fetchall()
    print(result)




# Логические операторы
# AND: операция логического И. Она объединяет два выражения:
# выражение1 AND выражение2
# OR: операция логического ИЛИ. Она также объединяет два выражения:
# выражение1 OR выражение2
# NOT: операция логического отрицания. Если выражение в этой операции ложно, то общее условие истинно.
# NOT выражение

# более подробно о операторах
# пример(
# SELECT * FROM products
# WHERE company ='Samsung' OR NOT (price > 30000 AND product_count > 2);
# )
# https://metanit.com/sql/sqlite/3.3.php
