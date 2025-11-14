import sqlite3

# Выборка уникальных значений. Оператор DISTINCT
# Оператор DISTINCT позволяет выбрать уникальные данные по определенным столбцам.
# К примеру, разные товары могут иметь одних и тех же производителей, и, допустим, у нас следующая таблица товаров:

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
    importer TEXT,
    price REAL)"""
    cursor.execute(query)
    db.commit()

data = [
    ('apple', 'Canada', 3.44),
    ('banana', 'Thailand', 2.45),
    ('plump', 'Canada', 4),
    ('strawberry', 'Canada', 3.44),
    ('watermelon', 'China', 2.95)
]

with sqlite3.connect('db_replace.db') as db:
    cursor = db.cursor()
    query = """INSERT OR IGNORE INTO Product (name, importer, price) VALUES (?, ?, ?)"""
    cursor.executemany(query, data)
    db.commit()

    query = """SELECT * FROM Product"""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

print('-' * 60)

# посмотрим на обычную выборку при помощи SELECT
with sqlite3.connect('db_replace.db') as db:
    cursor = db.cursor()
    query = """SELECT importer FROM Product"""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)  # видим повторяющиеся значения

    # а теперь воспользуемся distinct
    query = """SELECT DISTINCT importer FROM Product"""  # выборка только по importer
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    query = """SELECT DISTINCT importer,price FROM Product"""  # двойная выборка
    #strawberry к нам не попала
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)