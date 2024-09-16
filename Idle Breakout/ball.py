import screen_wrap
import blocks
from wrap import sprite as sp
import random as rd
import frame_statistics


def rd_not_zero(mini, maxi):
    return rd.choice([i for i in range(mini, maxi + 1) if i != 0])


def define_y(x):
    if x > 0:
        return 5 - x
    else:
        return -(5 + x)


class Ball:
    max_ball = 50
    all_balls = []

    def __init__(self):
        self.power = 1
        self.x = screen_wrap.x // 2
        self.y = screen_wrap.y // 2
        self.speed_x = rd_not_zero(-3, 3)
        self.speed_y = define_y(self.speed_x)

        self.name = sp.add_text('O', self.x, self.y,
                                font_name='Arial',
                                text_color=(255, 255, 0),
                                bold=True)
        sp.set_width_proportionally(self.name, 16)

        Ball.all_balls.append(self)

        frame_statistics.Screen_statistics.all_statistics.inf_balls_on_screen[
            'text'] = f' Balls \n{len(Ball.all_balls)}/50'

    def _check_window(self):

        if sp.get_left(self.name) <= 0:
            self.speed_x = abs(self.speed_x)
        if sp.get_right(self.name) >= screen_wrap.x:
            self.speed_x = -self.speed_x

        if sp.get_top(self.name) <= 0:
            self.speed_y = abs(self.speed_y)
        if sp.get_bottom(self.name) >= screen_wrap.y:
            self.speed_y = -self.speed_y

    def move(self):
        self._check_window()
        sp.move(self.name, self.speed_x, 0)
        self.check_collide_x()
        sp.move(self.name, 0, self.speed_y)
        self.check_collide_y()

    def check_collide_x(self):
        for one_block in blocks.Block.all_blocks:
            if sp.is_collide_sprite(self.name, one_block.name):
                blocks.Block.change_block(one_block, pover_ball=self.power)
                self.speed_x = -self.speed_x
                sp.move(self.name, self.speed_x, 0)
                break

    def check_collide_y(self):
        for one_block in blocks.Block.all_blocks:
            if sp.is_collide_sprite(self.name, one_block.name):
                blocks.Block.change_block(one_block, pover_ball=self.power)
                self.speed_y = -self.speed_y
                sp.move(self.name, 0, self.speed_y)
                break
    def effects(self):
        pass