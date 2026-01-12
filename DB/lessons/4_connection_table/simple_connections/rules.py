import sqlite3

# with sqlite3.connect('db1.db') as db:
#     cursor = db.cursor()
#     cursor.execute("""DROP TABLE IF EXISTS users""")
#     cursor.execute("""DROP TABLE IF EXISTS product""")
#     db.commit()
#
# # создадим таблицы
# with sqlite3.connect('db1.db') as db:
#     cursor = db.cursor()
#     query = """CREATE TABLE IF NOT EXISTS users
#     (id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT UNIQUE)"""
#     cursor.execute(query)

#     query="""CREATE TABLE IF NOT EXISTS product
#     (id INTEGER PRIMARY KEY AUTOINCREMENT,
#     description_id INTEGER,
#     description TEXT,
#     FOREIGN KEY (description_id) REFERENCES users(id))"""
#     cursor.execute(query)
#
#     db.commit()
#
# data = [
#     ('apple', 'Canada', 3.44),
#     ('banana', 'Thailand', 2.45),
#     ('plump', 'Canada', 4),
#     ('strawberry', 'Canada', 3.44),
#     ('watermelon', 'China', 2.95)
# ]
#
# with sqlite3.connect('db1.db') as db:
#
#     cursor=db.cursor()
#     query="""INSERT INTO users(name) VALUES (?)"""
#     cursor.execute(query,('robert',))
#     cursor.execute(query,('koko',))
#     db.commit()
#
#     query="""INSERT INTO product(description_id,description) values (?,?)"""
#     cursor.execute(query,(1,'lets go'))
#     cursor.execute(query,(1,'com one'))
#     cursor.execute(query,(1,'bandit'))


with sqlite3.connect('db1.db') as db:
    db.row_factory=sqlite3.Row

    cursor=db.cursor()
    query="""SELECT id,name FROM users"""
    cursor.execute(query)
    result=cursor.fetchall()
    print(result)
    for i in result:
        print(i['name'])



    query ="""SELECT description from product WHERE description_id=1"""
    cursor.execute(query)
    result=cursor.fetchone()


