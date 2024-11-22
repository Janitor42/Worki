import time
import ball
import blocks
from wrap import sprite as sp
import wrap
import screen_wrap


class Purple_ball(ball.Ball):
    def __init__(self,id=id):


        # purple
        self.max_size_contour = 60
        self.size_contour = 60
        self.x = screen_wrap.x // 2
        self.y = screen_wrap.y // 2
        self.contour = sp.add_text('O', self.x, self.y,
                                   font_name='Arial',
                                   text_color=(218, 71, 255),
                                   bold=True, visible=False)

        ball.Ball.__init__(self,id=id)

        wrap.sprite_text.set_text_color(self.name, 218, 71, 255)



    def move_contour(self):
        sp.move_to(self.contour, sp.get_x(self.name), sp.get_y(self.name))
        self.size_contour = self.max_size_contour
        sp.show(self.contour)

    def work_contour(self):
        for one_block in blocks.Block.all_blocks:
            if wrap.sprite.is_collide_sprite(self.contour, one_block.name):
                blocks.Block.change_block(one_block, pover_ball=self.power)

    def check_collide_x(self):
        for one_block in blocks.Block.all_blocks:
            if sp.is_collide_sprite(self.name, one_block.name):
                self.move_contour()
                self.work_contour()
                self.speed_x = -self.speed_x
                sp.move(self.name, self.speed_x, 0)
                break

    def check_collide_y(self):
        for one_block in blocks.Block.all_blocks:
            if sp.is_collide_sprite(self.name, one_block.name):
                self.move_contour()
                self.work_contour()
                self.speed_y = -self.speed_y
                sp.move(self.name, 0, self.speed_y)
                break

    def add_actions(self):
        sp.set_width_proportionally(self.contour, self.size_contour)
        self.size_contour -= 2
        if self.size_contour <= 10:
            self.size_contour = self.max_size_contour
            sp.hide(self.contour)
