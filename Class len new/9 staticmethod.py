
#работает независимо
class Vector:
    min_x=0
    max_x=100


    @classmethod
    def validate(cls,arg):
        return cls.min_x<=arg<=cls.max_x

    def __init__(self,x,y):
        self.x=self.y=0
        if self.validate(x):
            self.x=x
            self.y=y

        print(self.square(self.x))#запуск статичного метода в создании экземпляра

    def get_x(self):
        return self.x



    """обьявление статичного метода (независимая статичная функция для класса)"""
    @staticmethod#обьявление статичного метода в классе
    def square(x):#нет параметра cls или self (работает только с указаными аргументами как обычная фун-ия)
        return x*x#результат работы


vec1=Vector(110,20)
x_vec1=vec1.get_x()


print(Vector.square(4))#работа статического метода
