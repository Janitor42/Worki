import sqlite3

with sqlite3.connect('db_function_scal.db') as db:
    cursor = db.cursor()
    cursor.execute("""DROP TABLE IF EXISTS Product""")
    db.commit()

# создадим таблицу
with sqlite3.connect('db_function_scal.db') as db:
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

with sqlite3.connect('db_function_scal.db') as db:
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

# Агрегатные функции вычисляют некоторые скалярные значения на основе набора строк.
# В SQLite определены следующие агрегатные функции:

# AVG: вычисляет среднее значение
# Функция Avg возвращает среднее значение на диапазоне значений столбца таблицы.
# При этом строки со значением NULL игнорируются.

# SUM: вычисляет сумму значений
# Функция Sum вычисляет сумму значений столбца. Если столбец имеет значение NULL, то оно игнорируется.
# Например, подсчитаем общее количество товаров:

# MIN: вычисляет наименьшее значение
# MAX: вычисляет наибольшее значение
# Функции Min и Max вычисляют минимальное и максимальное значение по столбцу соответственно. Например,
# найдем минимальную цену среди товаров:

# COUNT: вычисляет количество строк в запросе
# Функция Count вычисляет количество строк в выборке. Есть две формы этой функции. Первая форма COUNT(*)
# подсчитывает число строк в выборке

# Все агрегатные функции в качестве параметра принимают выражение, которое представляет критерий для определения
# значений. Обычно это название столбца, над значениями которого надо проводить вычисления.
# Для рассмотрения агрегатных функций возьмем следующую таблицу products, которая хранит набор товаров:

#https://metanit.com/sql/sqlite/4.5.php


#ниже только один пример (лень)
with sqlite3.connect('db_function_scal.db') as db:

    query = """SELECT SUM(price) FROM Product"""
    cursor.execute(query)
    result = cursor.fetchall()
    db.commit()

    print(result)

