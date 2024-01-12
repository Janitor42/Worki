class Cat:

    def __init__(self,name):#магический метод присваивания  агрумента к экземпляру класса
        self.name=name
        print(f'Hello {self.name}')#просто вывод в консоль


cat1=Cat('tom')#создание экземпляра класса с уникальным атрибутом экземпляра класса(присваиваем в скобках)


class Cat2:
    """пример фактические или формальные параметры"""
    def __init__(self, name, age=0):#параметр age автоматически встает в 0, если мы хотим его указать , пишем при создании
        self.name = name
        self.age=age
        print(f'Hello {self.name} my age is {self.age}')


cat2 = Cat2('Jerry')#примеры
cat3=Cat2('lola',3)#примеры