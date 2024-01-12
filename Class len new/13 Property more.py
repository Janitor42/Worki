class Info:
#классметод - проверки перед созданием
# к полю __fio только get
#остальные поля меняются и узнаются через set и get
    def __init__(self, fio, age, passport, mass):
        self.verify_fio(fio)

        self.__fio = fio
        self.age = age
        self.passport = passport
        self.mass = mass

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("должна быть строка")

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат ФИО')

    @classmethod
    def verify_age(cls, age):
        if type(age) != int or age < 14 or age > 120:
            raise TypeError('Возвраст должен быть целым числом в диапазоне [14,120]')

    @classmethod
    def verify_mass(cls, mass):
        if type(mass) != float or mass < 20:
            raise TypeError('Вес должен быть вещественным числом от 20 и выше')

    @classmethod
    def verify_passport(cls, passport):
        if type(passport) != str:
            raise ValueError('Паспорт должен быть строкой')

        s = passport.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Неверный формат паспорта')

    def get_fio(self):
        return self.__fio

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.verify_age(age)
        self.__age=age

    fio = property(get_fio)
    age=property(get_age,set_age)

name = Info('Сигизмунд Фрейд Олегович', 119, '3311 995511', 149.9)
# print(name.__dict__)

print(name.fio)
print(name.age)
name.age=55
print(name.age)