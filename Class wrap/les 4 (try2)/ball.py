import wrap
import time
from wrap import sprite as sp
from random import randint as rd
import random
win_x = 500
win_y = 500
wrap.add_sprite_dir("C:/Users/i'm/PycharmProjects/Worki/Class wrap/les 4")

def rd_not_zero(min, max):
    return random.choice([i for i in range(min, max + 1) if i != 0])
class Ball:
    number = 1

    def __init__(self, x, y, speed_x, speed_y, size):
        self.__x = x
        self.__y = y
        self.__speed_x = speed_x
        self.__speed_y = speed_y

        self.__size = size
        self.choice_costume()
        sp.set_width_proportionally(self.name, self.__size)
        self.name_number = sp.add_text(str(self.number), self.__x, self.__y, bold=True)
        self.name_size = sp.add_text(str(self.__size), self.__x, self.__y + 20, font_size=15)
        Ball.number += 1

    def __del__(self):
        sp.remove(self.name)
        sp.remove(self.name_number)
        sp.remove(self.name_size)

    def choice_costume(self):
        if self.__size <= 30:
            self.name = sp.add('picture', self.__x, self.__y, 'red')
        elif 30 < self.__size <= 60:
            self.name = sp.add('picture', self.__x, self.__y, 'yellow')
        elif self.__size > 60:
            self.name = sp.add('picture', self.__x, self.__y, 'green')

    def move(self):
        self._check_window()
        sp.move(self.name, self.__speed_x, self.__speed_y)
        sp.move(self.name_number, self.__speed_x, self.__speed_y)
        sp.move(self.name_size, self.__speed_x, self.__speed_y)

    def collide(self, stars):
        for star in stars:
            if sp.is_collide_sprite(self.name, star.name):
                self._change_size(star.number)
                self._maybe_change_costume()
                star.live = False

    def _change_size(self, number):
        self.__size += number
        sp.set_width_proportionally(self.name, self.__size)
        wrap.sprite_text.set_text(self.name_size, str(self.__size))

    def check_ball(self,remove_ball,add_three_ball):
        if self.__size<=4:
            remove_ball(self)
        if self.__size>=100:
            add_three_ball(self)
            remove_ball(self)


    def _maybe_change_costume(self):
        if 0 < self.__size <= 30:
            sp.set_costume(self.name, 'red')
        if 30 < self.__size <= 60:
            sp.set_costume(self.name, 'yellow')
        if 100 > self.__size > 60:
            sp.set_costume(self.name, 'green')

    def _check_window(self):

        if sp.get_left(self.name) <= 0:
            self.__speed_x = abs(self.__speed_x)
        if sp.get_right(self.name) >= win_x:
            self.__speed_x = -self.__speed_x

        if sp.get_top(self.name) <= 0:
            self.__speed_y = abs(self.__speed_y)
        if sp.get_bottom(self.name) >= win_y:
            self.__speed_y = -self.__speed_y
