import ball
import blocks
from wrap import sprite as sp
import wrap
import screen_wrap


class Blue_children(ball.Ball):
    def __init__(self, parent):
        ball.Ball.__init__(self)
        self.x = sp.get_x(parent.name)
        self.y = sp.get_y(parent.name)
        sp.move_to(self.name, self.x, self.y)

        wrap.sprite_text.set_text_color(self.name, 0, 30, 201)
        sp.set_width_proportionally(self.name, 11)

    def __del__(self):
        sp.remove(self.name)
        sp.remove(self.contour)

    def move(self):
        self._check_window()
        if self.state != 'del':
            sp.move(self.name, self.speed_x, 0)
            self.check_collide_x()
        if self.state != 'del':
            sp.move(self.name, 0, self.speed_y)
            self.check_collide_y()
        if self.state == 'del':
            ball.Ball.all_balls.remove(self)

    def check_collide_x(self):

        for one_block in blocks.Block.all_blocks:
            if sp.is_collide_sprite(self.name, one_block.name):
                blocks.Block.change_block(one_block, pover_ball=self.power)
                self.speed_x = -self.speed_x
                sp.move(self.name, self.speed_x, 0)
                self.state = 'del'
                break

    def check_collide_y(self):
        for one_block in blocks.Block.all_blocks:
            if sp.is_collide_sprite(self.name, one_block.name):
                blocks.Block.change_block(one_block, pover_ball=self.power)
                self.speed_y = -self.speed_y
                sp.move(self.name, 0, self.speed_y)
                self.state = 'del'
                break
