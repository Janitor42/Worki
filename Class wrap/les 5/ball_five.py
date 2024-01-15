import wrap
import time
from wrap import sprite as sp
from random import randint as rd
import random

win_x = 800
win_y = 800
wrap.add_sprite_dir("/Class wrap/les 4")


def rd_not_zero(min, max):
    return random.choice([i for i in range(min, max + 1) if i != 0])


class Ball:
    def __init__(self, x, y, speed_x, speed_y, size):


        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.size = size
        self.choice_costume()
        self.group = self.find_group()
        self.state='open'

        sp.set_width_proportionally(self.name, self.size)
        self.name_text = sp.add_text(str(self.group), self.x, self.y, bold=True)
        self.name_size = sp.add_text(str(self.size), self.x, self.y + 20, font_size=15)
        self.name_state= sp.add_text(str(self.state),self.x,self.y - 20)




    def find_group(self):
        if self.size<=25:
            return 'A'
        elif 50>=self.size>=26:
            return 'B'
        elif 75>=self.size>=51:
            return 'C'
        elif self.size>=76:
            return 'D'



    def check_window(self, name_square, max_save, min_save):
        pass
        if max_save>self.size>min_save:
            if sp.get_left(self.name) <= sp.get_left(name_square):
                self.speed_x = abs(self.speed_x)
            if sp.get_right(self.name) >= sp.get_right(name_square):
                self.speed_x = -self.speed_x

            if sp.get_top(self.name) <= sp.get_top(name_square):
                self.speed_y = abs(self.speed_y)
            if sp.get_bottom(self.name) >= sp.get_bottom(name_square):
                self.speed_y = -self.speed_y
        else:
            if sp.get_left(self.name) <= 0:
                self.speed_x = abs(self.speed_x)
            if sp.get_right(self.name) >= win_x:
                self.speed_x = -self.speed_x

            if sp.get_top(self.name) <= 0:
                self.speed_y = abs(self.speed_y)
            if sp.get_bottom(self.name) >= win_y:
                self.speed_y = -self.speed_y

    def move(self):
        sp.move(self.name, self.speed_x, self.speed_y)
        sp.move(self.name_text, self.speed_x, self.speed_y)
        sp.move(self.name_size, self.speed_x, self.speed_y)
        sp.move(self.name_state, self.speed_x,self.speed_y)

    def choice_costume(self):
        if self.size <= 30:
            self.name = sp.add('picture', self.x, self.y, 'red')
        elif 30 < self.size <= 60:
            self.name = sp.add('picture', self.x, self.y, 'yellow')
        elif self.size > 60:
            self.name = sp.add('picture', self.x, self.y, 'green')

    @staticmethod
    def rd_randrange():
        return random.randrange(10, 90, 20)
