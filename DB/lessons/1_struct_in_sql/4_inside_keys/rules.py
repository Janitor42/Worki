import sqlite3

"PRIMARY KEY"
with sqlite3.connect('db_inside_keys.db') as db:
    cursor = db.cursor()
    query = f"""CREATE TABLE IF NOT EXISTS Test1 (
id INTEGER PRIMARY KEY,
name TEXT
)"""
    cursor.execute(query)
    db.commit()

    # Атрибут PRIMARY KEY задает первичный ключ таблицы.
# Здесь столбец id выступает в качестве первичного ключа,
# он будет уникально идентифицировать строку и его значение должно быть уникальным.
# То есть у нас не может быть таблице users более одной строки, где в столбце id было бы одно и то же значение.


with sqlite3.connect('db_inside_keys1.db') as db:
    cursor = db.cursor()
    query = f"""CREATE TABLE IF NOT EXISTS Test2 (
id INTEGER,
name TEXT,
PRIMARY KEY(id)
)"""
    cursor.execute(query)
    db.commit()
# Установка первичного ключа на уровне таблицы:
# то есть мы устанавливаем id сами,а потом указываем ему где взять уникальный ключ


with sqlite3.connect('db_inside_keys1.db') as db:
    cursor = db.cursor()
    query = f"""CREATE TABLE IF NOT EXISTS Test3 (
id INTEGER,
name TEXT,
PRIMARY KEY(id,name)
)"""
    cursor.execute(query)
    db.commit()

# В данном случае в качестве первичного ключа выступает связка столбцов id и name.
# То есть в таблице users не может быть двух строк, где для обоих из этих полей
# одновременно были бы одни и те же значения.

"AUTOINCREMENT"
with sqlite3.connect('db_inside_keys1.db') as db:
    cursor = db.cursor()
    query = f"""CREATE TABLE IF NOT EXISTS Test4 (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT
)"""
    cursor.execute(query)
    db.commit()

# Ограничение AUTOINCREMENT позволяет указать, что значение столбца будет автоматически
# увеличиваться при добавлении новой строки.
# Данное ограничение работает для столбцов, которые представляют тип INTEGER с ограничением PRIMARY KEY:

# В данном случае значение столбца id каждой новой добавленной строки будет увеличиваться на единицу.

"UNIQUE"
with sqlite3.connect('db_inside_keys1.db') as db:
    cursor = db.cursor()
    query = f"""CREATE TABLE IF NOT EXISTS Test5 (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT UNIQUE
)"""
    cursor.execute(query)
    db.commit()
# Ограничение UNIQUE указывает, что столбец может хранить только уникальные значения.
# В данном случае столбец email, который представляет телефон пользователя, может хранить только уникальные значения.
# И мы не сможем добавить в таблицу две строки, у которых значения для этого столбца будет совпадать.

# !!! можно делать вот так!
# query = f"""CREATE TABLE IF NOT EXISTS Test (
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT,
# email TEXT,
# UNIQUE(email, name)
# )"""

"NULL NOT NULL"
with sqlite3.connect('db_inside_keys1.db') as db:
    cursor = db.cursor()
    query = f"""CREATE TABLE IF NOT EXISTS Test6 (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL
)"""
    cursor.execute(query)
    db.commit()
# По умолчанию любой столбец, если он не представляет первичный ключ, может принимать значение NULL,
# то есть фактически отсутствие формального значения. Но если мы хотим запретить подобное поведение и установить,
# что столбец обязательно должен иметь какое-либо значение, то для него следует установить ограничение NOT NULL:

# В данном случае столбец name не допускает значение NULL.

"DEFAULT"
with sqlite3.connect('db_inside_keys1.db') as db:
    cursor = db.cursor()
    query = f"""CREATE TABLE IF NOT EXISTS Test7 (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER DEFAULT 18
)"""
    cursor.execute(query)
    db.commit()

# Ограничение DEFAULT определяет значение по умолчанию для столбца.
# Если при добавлении данных для столбца не будет предусмотрено значение,
# то для него будет использоваться значение по умолчанию.


"CHECK"
with sqlite3.connect('db_inside_keys1.db') as db:
    cursor = db.cursor()
    query = f"""CREATE TABLE IF NOT EXISTS Test8 (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL CHECK (name !=''),
age INTEGER NOT NULL CHECK (age >0 AND age <100)
)"""
    cursor.execute(query)
    db.commit()
# Ограничение CHECK задает ограничение для диапазона значений, которые могут храниться в столбце.
# Для этого после CHECK указывается в скобках условие, которому должен соответствовать столбец или несколько столбцов.
# Например, возраст пользователей не может быть меньше 0 или больше 100:
#
# Кроме проверки возраста здесь также проверяется, что столбец name не может иметь пустую строку в качестве значения
# (пустая строка не эквивалентна значению NULL).

# Для соединения условий используется ключевое слово AND.
# Условия можно задать в виде операций сравнения больше (>), меньше (<), не равно (!=).
#ПРИМЕР
# query = f"""CREATE TABLE IF NOT EXISTS Test (
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# age INTEGER NOT NULL,
# CHECK ((age>0 AND age<100) AND (name!=''))
# """


"CONSTRAINT"
'latest'

