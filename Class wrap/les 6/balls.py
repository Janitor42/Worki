import random
import time
import wrap
from wrap import sprite as sp
from wrap import sprite_text as sp_t
from random import randint as rd

wrap.add_sprite_dir("C:/Users/i'm/PycharmProjects/Worki/Class wrap/les 6/images")

win_x = 600
win_y = 800


def rd_not_zero(min, max):
    return random.choice([i for i in range(min, max + 1) if i != 0])


class Balls:

    def __init__(self):
        self.max_height = rd(50, 150)
        self.status='down'

        self._x = rd_not_zero(-3, 3)
        self.x_original = self._x

        self._y = 5
        self.y_original = self._y

        self.name = sp.add('ball(enemy)', 300, 300, 'yellow')
        sp.set_width_proportionally(self.name, 100)

    def move_ball(self, wall_block):
        print(self.x_original)

        sp.move(self.name, self._x, self._y)
        # self._slowdown_x()
        # self._slowdown_y()
        self._collide(wall_block)

    def _slowdown_x(self):
        # max_height_collide
        if sp.get_top(self.name) <= self.max_height + 15:
            if self._x < -0.5 or self._x > 0.5:
                self._x = self._x * 0.99

        elif not sp.get_top(self.name) <= self.max_height + 15:
            if self._x > 0 and self._x < self.x_original:
                self._x = self._x * 1.02
            if self._x < 0 and self._x > self.x_original:
                self._x = self._x * 1.02

    def _slowdown_y(self):
        # max_height_collide
        if sp.get_top(self.name) <= self.max_height + 15:
            if self._y < -0.3 or self._y > 0.3:
                self._y = self._y * 0.89


        elif not sp.get_top(self.name) <= self.max_height + 15:
            if self._y > 0 and self._y < self.y_original:
                self._y = self._y * 1.02
            if self._y < 0 and self._y > self.y_original:
                self._y = self._y * 1.02


    def _collide(self, wall_block):
        # left and right collide
        if sp.get_left(self.name) <= 0:
            self._x = abs(self._x)
            if self.status=='down':
                self._y=abs(self._y)

        if sp.get_right(self.name) >= win_x:
            self._x = -abs(self._x)
            if self.status=='down':
                self._y=abs(self._y)


        # wall_block_in down collide
        if sp.is_collide_sprite(self.name, wall_block.name):
            self.status='down'
            self._y = -abs(self._y)
            self.max_height = rd(50, 150)

        # max_height_collide
        if sp.get_top(self.name) <= self.max_height:
            self._y = abs(self._y)

            if self._x < 0:
                self.x_original = rd(1, 3)
                self._x = abs(self._x)

            else:
                self.x_original = rd(-3, -1)
                self._x = -abs(self._x)

