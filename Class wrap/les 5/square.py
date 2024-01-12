import wrap
import time
from wrap import sprite as sp
from random import randint as rd
import random

win_x = 500
win_y = 500
wrap.add_sprite_dir("C:/Users/i'm/PycharmProjects/Worki/Class wrap/les 5")


class Square:
    number = 1
    x = 10
    y = 10
    place = 1

    def __init__(self, size):
        self.__size = size
        self.__name = sp.add('picture', Square.x, Square.y, costume='square')
        Square.place += 1

    @classmethod
    def define_place(cls):
        if cls.place <= 4:
            cls.x = cls.x + cls.x
            cls.place += 1
