import sqlite3

with sqlite3.connect('db_limit.db') as db:
    cursor = db.cursor()
    cursor.execute("""DROP TABLE IF EXISTS Product""")
    db.commit()

# создадим таблицу
with sqlite3.connect('db_limit.db') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS Product
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    importer TEXT DEFAULT 'NULL',
    price REAL DEFAULT NULL)"""
    cursor.execute(query)
    db.commit()

data = [
    ('apple', 'Canada', 3.44),
    ('banana', 'Thailand', 2.45),
    ('plump', 'Canada', 4),
    ('strawberry', 'Canada', 3.44),
    ('watermelon', 'China', 2.95),
]

with sqlite3.connect('db_limit.db') as db:
    cursor = db.cursor()
    query = """INSERT OR IGNORE INTO Product (name, importer, price) VALUES (?, ?, ?)"""
    cursor.executemany(query, data)
    db.commit()

    query = """SELECT * FROM Product"""
    cursor.execute(query)
    result = cursor.fetchall()
    db.commit()

    print(result)

print('-' * 60)

# Получение диапазона строк. Оператор LIMIT
# Оператор LIMIT позволяет задать ограничение на количество строк :

# Если оператору LIMIT передается один параметр, то он указывает на количество извлекаемых строк.
# Если передается два параметра, то первый параметр устанавливает смещение относительно начала,
# то есть сколько строк нужно пропустить, а второй параметр также указывает на количество извлекаемых строк.

with sqlite3.connect('db_limit.db') as db:
    cursor = db.cursor()
    query = """SELECT * FROM Product LIMIT 3"""  # первые 3 строки
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    print('-' * 60)

    query = """SELECT * FROM Product LIMIT 2,4"""  # с 3 по 5
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    query = """SELECT * FROM Product ORDER BY price  LIMIT 2"""  # сортировка по цене потом берем 2 строки
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

