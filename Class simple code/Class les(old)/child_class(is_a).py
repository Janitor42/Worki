class Human:

    how_many=0
    def __init__(self,name,age):
        self.name = name
        self.surname = age


    def say_hello(self):
        print(f'{self.name} says hello!')

# p1=Human('Tom',15)
# p1.say_hello()

class Student(Human):
    def __init__(self,name,age,average_grade):
        # Human.__init__(self,name,age)
        super().__init__(name,age)
        self.average_grade=average_grade

    def study(self):
        print(f'{self.name} учиться')
    def say_hello(self):
        super().say_hello()
        print(f'Ga ga {self.name} says hello!')

class Teacher(Human):
    def teach(self):
        print(f'{self.name} преподает')


# s1 = Student('Mike',18,4.5)
# t1 =Teacher('Oleg',35)


def introduce(people):
    print('Now a person will say Hello')
    people.say_hello()


people_arr=[Student('Tom',18,3.5),Teacher('Sonya',35),Student('Bob',26,4.8)]

for i in people_arr:
    introduce(i)

# s1.say_hello()
# s1.study()
# t1.say_hello()
# t1.teach()