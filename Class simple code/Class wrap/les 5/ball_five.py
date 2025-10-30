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
    def __init__(self, x, y, speed_x, speed_y, size, list_stars, list_balls):

        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.size = size
        self.list_stars = list_stars
        self.list_balls = list_balls
        self.choice_costume()
        self.group = self._find_group()
        self.state = 'open'

        sp.set_width_proportionally(self.name, self.size)
        self.name_text = sp.add_text(str(self.group), self.x, self.y, bold=True)
        self.name_size = sp.add_text(str(self.size), self.x, self.y + 20, font_size=15)
        self.name_state = sp.add_text(str(self.state), self.x, self.y - 20)

    def __del__(self):
        sp.remove(self.name)
        sp.remove(self.name_text)
        sp.remove(self.name_state)
        sp.remove(self.name_size)

    def _find_group(self):
        if self.size <= 25:
            return 'A'
        elif 50 >= self.size >= 26:
            return 'B'
        elif 75 >= self.size >= 51:
            return 'C'
        elif self.size >= 76:
            return 'D'

    def move(self):
        sp.move(self.name, self.speed_x, self.speed_y)
        sp.move(self.name_text, self.speed_x, self.speed_y)
        sp.move(self.name_size, self.speed_x, self.speed_y)
        sp.move(self.name_state, self.speed_x, self.speed_y)
        self._check_ball_collide_stars()

    def _check_ball_collide_stars(self):
        for star in self.list_stars:
            if sp.is_collide_sprite(self.name, star.name):
                star.live = False
                self._replace_options_ball(star)

    def _replace_options_ball(self, star):
        # size
        self.size = self.size + star.number
        sp.set_width_proportionally(self.name, self.size)
        wrap.sprite_text.set_text(self.name_size, str(self.size))
        self._maybe_change_costume()
        if self.size <= 4:
            self.list_balls.remove(self)
        if self.size >= 101:
            self._create_three_ball()
            self.list_balls.remove(self)
        else:
            # group
            old_group = self.group
            self.group = self._find_group()
            wrap.sprite_text.set_text(self.name_text, str(self.group))
            # state
            if old_group != self.group:
                self.state = 'open'
                wrap.sprite_text.set_text(self.name_state, str(self.state))

    def _maybe_change_costume(self):
        if 0 < self.size <= 30:
            sp.set_costume(self.name, 'red')
        if 30 < self.size <= 60:
            sp.set_costume(self.name, 'yellow')
        if 100 > self.size > 60:
            sp.set_costume(self.name, 'green')

    def choice_costume(self):
        if self.size <= 30:
            self.name = sp.add('picture', self.x, self.y, 'red')
        elif 30 < self.size <= 60:
            self.name = sp.add('picture', self.x, self.y, 'yellow')
        elif self.size > 60:
            self.name = sp.add('picture', self.x, self.y, 'green')

    def _create_three_ball(self):
        for q in range(3):
            self.list_balls.append(Ball(x=sp.get_x(self.name),
                                        y=sp.get_y(self.name),
                                        speed_x=rd_not_zero(-3, 3),
                                        speed_y=rd_not_zero(-3, 3),
                                        size=self.size // 3,
                                        list_stars=self.list_stars,
                                        list_balls=self.list_balls))

    @staticmethod
    def rd_randrange():
        return random.randrange(10, 90, 20)
