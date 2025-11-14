import sqlite3

with sqlite3.connect('db_sort_order_by.db') as db:
    cursor = db.cursor()
    cursor.execute("""DROP TABLE IF EXISTS Product""")
    db.commit()

# создадим таблицу
with sqlite3.connect('db_sort_order_by.db') as db:
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

with sqlite3.connect('db_sort_order_by.db') as db:
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

# Оператор ORDER BY сортируют значения по одному или нескольких столбцам.
# Например, упорядочим выборку из таблицы products по столбцу price:

with sqlite3.connect('db_sort_order_by.db') as db:
    cursor = db.cursor()
    query = """SELECT * FROM Product ORDER BY price"""  # сортировка по price
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

print('-' * 60)

# Сортировка по убыванию
# По умолчанию данные сортируются по возрастанию, однако с помощью оператора DESC можно задать сортировку по убыванию.\
# По умолчанию вместо DESC используется оператор ASC, который сортирует по возрастанию:
with sqlite3.connect('db_sort_order_by.db') as db:
    cursor = db.cursor()
    query = """SELECT * FROM Product ORDER BY price DESC"""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

print('-' * 60)

# Сотировка по нескольким столбцам
# При сортировке сразу по нескольким столбцам все эти столбцы указываются через запятую после оператора ORDER BY:

with sqlite3.connect('db_sort_order_by.db') as db:
    cursor = db.cursor()
    query = """SELECT * FROM Product ORDER BY price ASC, name DESC"""  # изначальная сортировка по цене от низа в верх,
    # доп сортировка по словам в обратном порядке алфавита
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

print('-' * 60)

# Сортировка по NULL
# NULL представляет специальное значение, которое не сравнивается с другими значениями.
# По умолчанию NULL оценивается как наименьшее из значений.
# Это значит, что при сортировке по возрастанию значение NULL будет предшествовать всем остальным значениям.
# Однако поведение по умолчанию, когда NULL идет перед остальными значениями при сортировке по возрастанию или
# в конце при сортировке по убыванию может быть нежелательным. В этом случае мы можем использовать дополнительные
# операторы: NULLS FIRST и NULLS LAST. NULLS FIRST указывает, что значение NULL идет перед всеми остальными
# значениями, а NULLS LAST - после.
# Например, выведем значения NULL при сортировке по возрастанию после остальных значений:

#примера нет (создайте сами)
