import sqlite3

with sqlite3.connect('db_operators_filtration.db') as db:
    cursor = db.cursor()
    cursor.execute("""DROP TABLE IF EXISTS Product""")
    db.commit()

# создадим таблицу
with sqlite3.connect('db_operators_filtration.db') as db:
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

with sqlite3.connect('db_operators_filtration.db') as db:
    cursor = db.cursor()
    query = """INSERT OR IGNORE INTO Product (name, importer, price) VALUES (?, ?, ?)"""
    cursor.executemany(query, data)
    db.commit()

    query = """SELECT * FROM Product"""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

print('-' * 60)

# IN - определяет набор значений, которые должен иметь столбец:

# Выражение в скобках после IN определяет набор значений. Этот набор может вычисляться динамически на основании,
# например, еще одного запроса, либо это могут быть константные значения.
with sqlite3.connect('db_operators_filtration.db') as db:
    cursor = db.cursor()
    query = """SELECT * FROM Product WHERE importer IN (?,?)"""
    cursor.execute(query, ('Canada', 'China'))
    result = cursor.fetchall()
    print(f"{result} это был IN")

print('-' * 60)

# NOT IN - наоборот, позволяет выбрать все строки, не соответствуют критерию:
with sqlite3.connect('db_operators_filtration.db') as db:
    cursor = db.cursor()
    query = """SELECT * FROM Product WHERE importer NOT IN (?,?)"""
    cursor.execute(query, ('Canada', 'China'))
    result = cursor.fetchall()
    print(f"{result} это был NOT IN")

print('-' * 60)

# Оператор BETWEEN
# Оператор BETWEEN определяет диапазон значений с помощью начального и конечного значения,
# которому должно соответствовать выражение:
with sqlite3.connect('db_operators_filtration.db') as db:
    cursor = db.cursor()
    query = """SELECT * FROM Product WHERE price BETWEEN ? AND ?"""
    cursor.execute(query, (2, 3))
    result = cursor.fetchall()
    print(f"{result} это был BETWEEN")

print('-' * 60)

# NOT BETWEEN
with sqlite3.connect('db_operators_filtration.db') as db:
    cursor = db.cursor()
    query = """SELECT * FROM Product WHERE price NOT BETWEEN ? AND ?"""
    cursor.execute(query, (2, 3))
    result = cursor.fetchall()
    print(f"{result} это был NOT BETWEEN")

print('-' * 60)

# Оператор LIKE
# Оператор LIKE принимает шаблон строки, которому должно соответствовать выражение.
# %: соответствует любой подстроке, которая может иметь любое количество символов,
# при этом подстрока может и не содержать ни одного символа

with sqlite3.connect('db_operators_filtration.db') as db:
    cursor = db.cursor()
    query = """SELECT * FROM Product WHERE importer LIKE (?)"""
    cursor.execute(query, ('C%',))
    result = cursor.fetchall()
    print(f"{result} это был LIKE")

print('-' * 60)

#GLOB и NULL  примеров не будет (GLOB - нужна большая бд, NULL слишком очевидно)
# GLOB
# Оператор GLOB также позволяет проверить, соответствует ли строка некоторому выражению.
# GLOB имеет похожий синтаксис:
# *: соответствует любому количеству символов
# ?: соответствует одному символу
# .: соответствует любому одиночному символу
# [символы]: соответствует любому одиночному символу из списка символов внутри скобок ([abc])
# [начальный_символ-конечный_символ]: соответствует любому одиночному символу из диапазона символов ([a-zA-Z0-9])
# ^: этот символ используется в начале списка символов и соответствует любому символу, которое НЕ входит в список ([^0-9])


# Примеры GLOB:
# WHERE name GLOB '*Pro': строка должна содержать оканчиваться на "Pro", например, T11 Pro, P40 Pro, iPhone X Pro
# WHERE name GLOB '*2?': строка должна иметь символ "2", перед которым может идти любое количество символов, а после - идет один символ, например, Nokia XR20, Galaxy S21
# WHERE name GLOB 'iPhone 1[012]': строка должна начинаться на iPhone 1, и затем идет одна цифра: 0, 1 или 2. Соответствует либо iPhone 10. либо iPhone 11, либо iPhone 12
# WHERE name GLOB 'iPhone [6-8]': строка должна содержать либо iPhone 6, либо iPhone 7, либо iPhone 8


# IS NULL
# Оператор IS NULL позволяет выбрать все строки, столбцы которых имеют значение NULL:
# С помощью добавления оператора NOT можно, наоброт, выбрать строки, столбцы которых не имеют значения NULL: