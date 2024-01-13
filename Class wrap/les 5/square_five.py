import wrap
import time
from wrap import sprite as sp
from random import randint as rd
import random
import ball_five

win_x = 500
win_y = 500
wrap.add_sprite_dir("C:/Users/i'm/PycharmProjects/Worki/Class wrap/les 5")


def rd_not_zero(min, max):
    return random.choice([i for i in range(min, max + 1) if i != 0])
class Square:
    def __init__(self, size, x, y, count_ball):
        self.balls = []
        self.__x = x
        self.__y = y
        self.__size = size
        self.__count_ball = count_ball
        self.__create_ball()
        self.name = sp.add('picture', self.__x, self.__y, costume='square_five')
        sp.set_width_proportionally(self.name, self.__size)

    def __create_ball(self):
        for i in range(self.__count_ball):
            self.balls.append(ball_five.Ball(x=self.__x, y=self.__y, speed_x=rd_not_zero(-3, 3),
                                             speed_y=rd_not_zero(-3, 3), size=rd(20, 80)))

    def move_all(self):
        for i in self.balls:
            self._check_window(i, self.__x, self.__y, self.__size)
            sp.move(i.name, i.speed_x, i.speed_y)

    @staticmethod
    def _check_window(self, x, y, size):
        if sp.get_left(self.name) <= x - size // 2:
            self.speed_x = abs(self.speed_x)
        if sp.get_right(self.name) >= size // 2 + x:
            self.speed_x = -self.speed_x

        if sp.get_top(self.name) <= y - size // 2:
            self.speed_y = abs(self.speed_y)
        if sp.get_bottom(self.name) >= size // 2 + y:
            self.speed_y = -self.speed_y
