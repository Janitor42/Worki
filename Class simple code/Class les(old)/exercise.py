class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'This {self.name} is eating')


class Dog(Animal):
    def __init__(self,  name,breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f'Dog {self.name} is barking')


class Cat(Animal):
    def meow(self):
        print(f'Cat {self.name} is speak Meow')


class Frog(Animal):
   def eat(self):
        print(f'Frog with {self.name} is eating')




arr=[Animal('Gaw,Black_dog'),Cat('Cati'),Frog('Frogi')]

def animals_says(this_animal):
    this_animal.eat()

for i in arr:
    animals_says(i)



d=Dog('Vala','White')
d.eat()
d.bark()
print(d.breed)