#self - 1-ый параметр в методе класса который автоматически будет подставлять именно этот экземпляр класса в вызываевом методе

class People:
    name='Sasha'

    def get_name(self):#создание метода с параметром self
        print(f'My name is {self.name}')#результат работы метода


a1=People()#создание экземпляра класса
a1.get_name()#вызов метода у экземпляра класса


#People.get_name()#если вызвать через класс - получим ошибку
People.get_name(a1)#а так ошибки не будет ( мы указываем у кого вызываем этот метод


class Square:

    def set_pos(self,x,y):#метод который присваивает 2 параметра экземпляру класса
        self.x=x
        self.y=y

    def get_x(self):#метод который при вызове возвращает значение атрибута(поля) у вызванного экземпляра
        return self.x


s1=Square()#создание экземпляра класса
s1.set_pos(5,10)#вызов метода - присваивание атрибутов для экземпляра класса
print(s1.x,s1.y)#печать x и y(для наглядности)


print(s1.get_x())#возвращает значение атрибута(поля) у вызванного экземпляра