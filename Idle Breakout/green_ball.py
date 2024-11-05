import random
import time
import ball
import blocks
from wrap import sprite as sp
import wrap
import screen_wrap


class Green_ball(ball.Ball):

    def __init__(self,id=id):

        ball.Ball.__init__(self,id=id)
        wrap.sprite_text.set_text_color(self.name, 16, 145, 1)


        # green
        self.target_x = 0
        self.target_y = 0
        self.speed_x_and_y = 6
        self.choice = None
        self.state = False


    def move(self):

        self._check_window()
        if not self.state:
            sp.move(self.name, self.speed_x, 0)
            self.check_collide_x()
            sp.move(self.name, 0, self.speed_y)
            self.check_collide_y()
        else:
            if self.choice.state:
                sp.move_at_angle_point(self.name, self.target_x, self.target_y, self.speed_x_and_y)
                self.check_collide_x()
                self.check_collide_y()
            else:
                self.state = False

    def move_to(self):

        self.choice = random.choice(blocks.Block.all_blocks)
        self.target_x = wrap.sprite.get_x(self.choice.name)
        self.target_y = wrap.sprite.get_y(self.choice.name)

    def check_collide_x(self):
        for one_block in blocks.Block.all_blocks:
            if sp.is_collide_sprite(self.name, one_block.name):
                blocks.Block.change_block(one_block, pover_ball=self.power)
                self.speed_x = -self.speed_x
                sp.move(self.name, self.speed_x, 0)
                self.state = False
                break

    def check_collide_y(self):

        for one_block in blocks.Block.all_blocks:
            if sp.is_collide_sprite(self.name, one_block.name):
                blocks.Block.change_block(one_block, pover_ball=self.power)
                self.speed_y = -self.speed_y
                sp.move(self.name, 0, self.speed_y)
                self.state = False
                break

    def _check_window(self):

        if sp.get_left(self.name) <= 0:
            self.speed_x = abs(self.speed_x)
            self.state = True
            self.move_to()

        if sp.get_right(self.name) >= screen_wrap.x:
            self.speed_x = -self.speed_x
            self.state = True
            self.move_to()

        if sp.get_top(self.name) <= 0:
            self.speed_y = abs(self.speed_y)
            self.state = True
            self.move_to()

        if sp.get_bottom(self.name) >= screen_wrap.y:
            self.speed_y = -self.speed_y
            self.state = True
            self.move_to()
