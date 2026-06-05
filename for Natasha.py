import random


class Server:
    def __init__(self, state=None, booklet=None):
        self.name = "Sam"
        self.state = state
        self.booklet = {}
        self.menu = ["Fish", "Salad", "Soup"]

    def welcoming(self):
        print(f'"Hello my name is",{self.name}')
        return self.menu

    def get_order(self, table, order):
        self.booklet = {"table": table, "order": order}
        return self.booklet


class Visitor:
    def __init__(self, table=None, order=None):
        self.menu = None
        self.name = "Lily"
        self.table = table
        self.order = order

    def make_order(self):
        self.order = random.choice(self.menu)
        return f'{self.name},{self.table},"Sat for 2 seconds and ordered:",{self.order}'

    def get_menu(self, menu):
        self.menu = menu


server1 = Server()

visitor1 = Visitor(table=27)
visitor1.get_menu(menu=server1.welcoming())
print(visitor1.make_order())
print(server1.get_order(table=visitor1.table, order=visitor1.order))

#Допиши 3 класс Кухня (она общается только с официаном - официант приходит на кухню и говорит что заказали
#после этого кухня создает это блюдо и сообщает официанту что оно готово, официант после готовности блюда
#забирает его и он передает его посетителю
#ИТОГ: посетитель получает блюдо от официанта!