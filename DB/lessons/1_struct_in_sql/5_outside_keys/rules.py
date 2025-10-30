# Внешние ключи позволяют установить связи между таблицами.
# Внешний ключ устанавливается для столбцов из зависимой,
# подчиненной таблицы, и указывает на один из столбцов из главной таблицы.
# Как правило, внешний ключ указывает на первичный ключ из связанной главной таблицы.


import sqlite3

"PRIMARY KEY"
with sqlite3.connect('db_outside_keys.db') as db:
    db.execute("PRAGMA foreign_keys = ON") #включаем внешние ключи !!! обязательно!
    cursor = db.cursor()
    query = f"""CREATE TABLE IF NOT EXISTS Companies (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL);

CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
company_id INTEGER,
FOREIGN KEY(company_id) REFERENCES Companies (id)
)"""
    cursor.executescript(query)
    db.commit()

# FOREIGN KEY (указывается столбец таблицы, который будет представляет внешний ключ.)
# REFERENCES (указывается имя связанной таблицы,
# а затем в скобках имя связанного столбца, на который будет указывать внешний ключ)



# В данном случае определены таблицы companies и users.
# companies является главной и представляет компании,
# где может работать пользователь. users является зависимой и представляет пользователей.
# Таблица users через столбец company_id связана с таблицей companies и ее столбцом id.
# То есть столбец company_id является внешним ключом, который указывает на столбец id из таблицы companies.


"ON DELETE и ON UPDATE"
# С помощью выражений ON DELETE и ON UPDATE можно установить действия,
# которые выполняются соответственно при удалении и изменении связанной строки из главной таблицы.
# В качестве действия могут использоваться следующие опции:
#
# CASCADE: автоматически удаляет или изменяет строки из зависимой таблицы при удалении или изменении связанных строк
# в главной таблице.
#
# SET NULL: при удалении или обновлении связанной строки из главной таблицы устанавливает для столбца внешнего ключа
# значение NULL. (В этом случае столбец внешнего ключа должен поддерживать установку NULL)
#
# RESTRICT: отклоняет удаление или изменение строк в главной таблице при наличии связанных строк в зависимой таблице.
#
# NO ACTION: то же самое, что и RESTRICT.
#
# SET DEFAULT: при удалении связанной строки из главной таблицы устанавливает для столбца внешнего ключа значение
# по умолчанию, которое задается с помощью атрибуты DEFAULT.


# Каскадное удаление
# Каскадное удаление позволяет при удалении строки из главной таблицы автоматически удалить
# все связанные строки из зависимой таблицы. Для этого применяется опция CASCADE:
#короче трогая главную трогаем все остальное через внешний ключ
"""CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
company_id INTEGER,
FOREIGN KEY(company_id) REFERENCES Companies (id) ON DELETE CASCADE
)"""
# CASCADE
# SET NULL
# RESTRICT
# SET DEFAULT