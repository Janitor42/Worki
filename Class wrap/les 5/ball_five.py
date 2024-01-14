import wrap
import time
from wrap import sprite as sp
from random import randint as rd
import random

win_x = 800
win_y = 800
wrap.add_sprite_dir("C:/Users/i'm/PycharmProjects/Worki/Class wrap/les 4")


def rd_not_zero(min, max):
    return random.choice([i for i in range(min, max + 1) if i != 0])


class Ball:
    number = 1

    def __init__(self, x, y, speed_x, speed_y, size):
        self.__x = x
        self.__y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.__size = size
        self.choice_costume()
        sp.set_width_proportionally(self.name, self.__size)
        self.name_number = sp.add_text(str(self.number), self.__x, self.__y, bold=True)
        self.name_size = sp.add_text(str(self.__size), self.__x, self.__y + 20, font_size=15)
        Ball.number += 1

    def choice_costume(self):
        if self.__size <= 30:
            self.name = sp.add('picture', self.__x, self.__y, 'red')
        elif 30 < self.__size <= 60:
            self.name = sp.add('picture', self.__x, self.__y, 'yellow')
        elif self.__size > 60:
            self.name = sp.add('picture', self.__x, self.__y, 'green')



    def check_window(self,name_square,max_save,min_save):
        if max_save>self.__size>min_save:
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
        sp.move(self.name_number, self.speed_x, self.speed_y)
        sp.move(self.name_size, self.speed_x, self.speed_y)



