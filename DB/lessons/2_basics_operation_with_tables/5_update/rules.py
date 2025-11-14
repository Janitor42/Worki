import sqlite3

# Для обновления данных в SQLite применяется команда UPDATE:


with sqlite3.connect('db_update.db') as db:
    cursor = db.cursor()
    cursor.execute("""DROP TABLE IF EXISTS Product""")
    db.commit()

# создадим таблицу
with sqlite3.connect('db_update.db') as db:
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

# запишем в нее данные (пример изменение данных во всех таблице сразу)
with sqlite3.connect('db_update.db') as db:
    cursor = db.cursor()
    query = """INSERT OR IGNORE INTO Product(name,product_count,price) VALUES(?,?,?) """
    cursor.executemany(query, data)
    db.commit()

# Смотри сюда
with sqlite3.connect('db_update.db') as db:
    cursor = db.cursor()
    query = """SELECT * FROM Product"""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    db.commit()

    query = """UPDATE Product SET product_count = product_count + 100 """  # -----
    # Увеличим в этой таблице кол-во всех товаров цену на 100:
    cursor.execute(query)
    db.commit()

    query = """SELECT * FROM Product"""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    db.commit()

print('-' * 60)
# пример изменения данных только с определенными ячейками таблицы

with sqlite3.connect('db_update.db') as db:
    cursor = db.cursor()
    query = """UPDATE Product SET name = 'crazy_banana',price=1000,product_count=777 WHERE name = 'banana'"""  # ---
    # изменение данных только по имени и тут же присвоение новых данных
    cursor.execute(query)
    db.commit()

    query = """SELECT * FROM Product"""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
