class People:
    name='Sasha'# свойства класса


a1=People()#создание экземпляра класса и его сохранение
print(a1)

print(a1.name)#обращение к атрибудуту класса (сначала имя экземпляра класса, точка, вызов атрибута у экземпляра этого класса

a1.name='Grisha'#смена значения атрибута у экземпляра класса а1.(в самом классе People-все остается без изменений
#значение меняется только у данного экземпляра класса

#нельзя вызывать несущестующий атрибут (ни у экземпляра ни у класса-будет ошибка)

a1.age=10#создание нового атрибута в экземпляре класса (у а1 - будет поле age и значение 10, у класса People - этого поля не будет)

print(a1.name)
del a1.name #удаление атрибута класса удалит его значение из экземпляра(Grisha)
#при вызове a1.name - будем получать 'Sasha' т. к в самом экземпляре уже ничего нет, будем брать поле в самом классе Peole
print(a1.name)