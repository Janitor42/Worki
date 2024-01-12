#свойства
class Dog:

    __colors=['black','white','red']#на уровне класса список цветов
    def __init__(self,name,color=None,breed=None):
        self.name=name
        self.color=color
        self.__breed=breed

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name

    def get_breed(self):
        return self.__breed


    name = property(get_name,set_name)#использует декоратор который определяет логику
    #применяя методы get_name и set_name пропуская их через проперти

    breed=property(get_breed)#такой вар-т проперти позволяет только узнать пароду но не изменить ее



d1=Dog('Gogo')
print(d1.name)
d1.name='Shi'
print(d1.name)

print(d1.breed)







