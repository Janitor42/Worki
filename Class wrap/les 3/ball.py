import wrap
from wrap import sprite as sp
from random import randint as rd


class Ball:
    def __init__(self, type):
        self.define_ball(type)
        self.name = sp.add('pacman', self.x, self.y, 'player3')
        self.go=False

    def move_standard(self):
        sp.move(self.name, self.speed_x, self.speed_y)

    def define_ball(self, type):
        if type == 'hard':
            self.x = int(input('x '))
            self.y = int(input('y '))
            self.speed_x = int(input('speed x '))
            self.speed_y = int(input('speed y '))
        else:
            self.x = rd(10, 470)
            self.y = rd(10, 470)
            self.speed_x = 1
            self.speed_y = 0

    def change_speed_ball(self):
        self.speed_x = int(input('new speed x '))
        self.speed_y = int(input('new speed y '))



