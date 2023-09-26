import wrap
from wrap import sprite
class Ball:
    def __init__(self,speed,x,y):
        self.a=speed
        self.name=sprite.add("mario-items",x,y,"coin")

    def add_five(self):
        self.a=self.a+5
    def add(self,speed):
        self.a=self.a+speed
    def goo(self):
        sprite.move(self.name,self.a,self.a)
        if sprite.get_y(self.name)>500:
            self.a=-self.a
        elif sprite.get_y(self.name)<0:
            self.a = abs(self.a)