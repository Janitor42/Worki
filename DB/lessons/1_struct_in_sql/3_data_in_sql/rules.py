import sqlite3

with sqlite3.connect('db_dates.db') as db:
    cursor = db.cursor()
    query = f"""CREATE TABLE IF NOT EXISTS Test (
field1 INTEGER,
field2 REAL,
field3 TEXT,
field4 NULL,
field5 BLOB,
field6 NUMERIC
)"""
    cursor.execute(query)
    db.commit()

# NULL: указывает фактически на отсутствие значения (тот же NONE)

# INTEGER: представляет целое число, которое может быть положительным и отрицательным и в зависимости
# от своего значения может занимать 1, 2, 3, 4, 6 или 8 байт

# REAL: представляет число с плавающей точкой, занимает 8 байт в памяти

# TEXT: строка текста в одинарных кавычках, которая сохраняется в кодировке базы данных (UTF-8, UTF-16BE или UTF-16LE)

# BLOB: бинарные данные

# NUMERIC -Этот идентификатор не представляет отдельного типа данных.
# А фактически представляет столбец, который может хранить данные всех пяти выше перечисленных типов
# (в терминологии SQLite NUMERIC еще называется type affinity)
