#1
#инкапсуляция

#атрибут с __ перед названием - private (доступа не имеем) - доступ только внутри класса
#атрибут с _ перед названием - protected (доступ защищен) - доступ внутри класса и всех дочерних(дети) классах
#атрибут без __ перед названием - public (общедоступный) - доступ везде
"""Protected"""
class Point:
    def __init__(self,x,y):
        self._x=x#protected(сигнал для програмиста о том что ненадо менять его из вне) говорит нам о том что это
        #внутренняя служебная переменная !! Не меняй ее извне!
        self._y=y


d=Point(5,10)

print(d._x,d._y)#работать мы с ним можем как и впедь



#2
"""Private"""
class Point2:
    def __init__(self, x, y):
        self.__x = x  #private(
        self.__y = y
        print(f'сейчас  x and y  = {self.__x} {self.__y}')

    """set - сеттер"""
    def set_pos(self,x,y):# при помощи этого метода мы и меняем координаты на уровне работы внутри класса а не из вне
        if type(x) in (int,float) and type(y) in (int,float):#доп проверка на тип данных для присвоении новых значений
            self.__x=x
            self.__y=y
            print(f'поменяли x and y  на {self.__x} {self.__y}')
        else:
            raise  ValueError('координаты должны быть числами ') #бросаем исключение

    """get - геттер"""
    def get_pos(self):
        return self.__x,self.__y


d2=Point2(5,10)

#print(d.__x)#при вызове поля экземпляра получим ошибку т.к. поле private (мы не имеем доступа на работы экземпляра класса!)
#но можем спокойно работать с ним внутри класса


d2.set_pos(15,30)
print(d2.get_pos())








#2.1
class Point3:
    def __init__(self, x, y):
        self.__x=self.__y=0
        if self.__check_value(x) and self.__check_value(y):  # переделали проверку используя private метод класса
            self.__x = x
            self.__y = y
            print(f'сейчас  x and y  = {self.__x} {self.__y}')
        else:
            raise  ValueError('координаты должны быть числами ')

    @classmethod
    def __check_value(cls,a):#private  метод класса который проверяет что это число
        return type(a) in (int,float)
    def set_pos(self,x,y):
        if self.__check_value(x) and self.__check_value(y):#переделали проверку используя private метод класса
            self.__x=x
            self.__y=y
            print(f'поменяли x and y  на {self.__x} {self.__y}')
        else:
            raise  ValueError('координаты должны быть числами ')


    def get_pos(self):
        return self.__x,self.__y


d3=Point3(5,10)


d3.set_pos(15,30)
print(d2.get_pos())