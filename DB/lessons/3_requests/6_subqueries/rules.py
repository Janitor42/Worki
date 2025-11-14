import sqlite3

with sqlite3.connect('db_subqueries.db') as db:
    cursor = db.cursor()
    cursor.execute("""DROP TABLE IF EXISTS Companies""")
    cursor.execute("""DROP TABLE IF EXISTS Users""")
    db.commit()

    # создадим 2таблицы
with sqlite3.connect('db_subqueries.db') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS Companies
    
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT);
    
    CREATE TABLE IF NOT EXISTS Users
    
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    company_id INTEGER);
    
    """
    cursor.executescript(query)  # обработка множественных запросов!!
    db.commit()

# Таблица users содержит поле company_id, которое будет представлять id компании из таблицы companies.


data = [('tom', 22, 'Microsoft'),
        ('bob', 41, 'Google'), ]

company = [('Microsoft',), ('Google',)]

# Добавим в таблицы некоторые данные:
with sqlite3.connect('db_subqueries.db') as db:
    cursor = db.cursor()

    query = """INSERT OR IGNORE INTO Companies(name) VALUES (?)"""
    cursor.executemany(query, company)

    query = """INSERT INTO Users(name, age, company_id) VALUES (?,?,(SELECT id FROM Companies WHERE name = ?))"""
    cursor.executemany(query, data)
    db.commit()

# SELECT id FROM Companies WHERE name = 'Microsoft'
# Предположим, возвращает: 1
# INSERT INTO Users(name, age, company_id) VALUES ('tom', 22, 1)


