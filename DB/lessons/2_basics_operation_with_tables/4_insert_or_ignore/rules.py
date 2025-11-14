import sqlite3

#как добавлять в таблицу только если такого не существует ?
#INSERT OR IGNORE
with sqlite3.connect('db_insert_or_ignore.db') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS People
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    price REAL)"""
    cursor.execute(query)
    db.commit()

data = [
    ('Banana', 100),
    ('Banana', 150),#эта не записывается
    ('Orange', 200)
]

#записать но в едиственном имени
with sqlite3.connect('db_insert_or_ignore.db') as db:
    cursor = db.cursor()
    query = """INSERT OR IGNORE INTO People(name, price) VALUES(?,?)"""#смотри сюда
    cursor.executemany(query, data)
    db.commit()

#посмотреть
with sqlite3.connect('db_insert_or_ignore.db') as db:
    cursor = db.cursor()
    query = """SELECT * FROM People"""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)