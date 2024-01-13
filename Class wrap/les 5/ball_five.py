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
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.__size = size
        self.choice_costume()
        sp.set_width_proportionally(self.name, self.__size)


    def choice_costume(self):
        if self.__size <= 30:
            self.name = sp.add('picture', self.__x, self.__y, 'red')
        elif 30 < self.__size <= 60:
            self.name = sp.add('picture', self.__x, self.__y, 'yellow')
        elif self.__size > 60:
            self.name = sp.add('picture', self.__x, self.__y, 'green')

