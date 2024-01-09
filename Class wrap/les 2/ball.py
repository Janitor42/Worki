import wrap
from wrap import sprite as sp
from random import randint as rd


class Ball:
    def __init__(self,speed_x,speed_y,x,y):
        self.x=x
        self.y=y
        self.speed_x=speed_x
        self.speed_y=speed_y
        self.name = sp.add('pacman', self.x, self.y, 'player3')
        self.go=False

    def move_standard(self):
        sp.move(self.name, self.speed_x, self.speed_y)


    def change_speed_ball(self,speed_x,speed_y):
        self.speed_x=speed_x
        self.speed_y=speed_y



