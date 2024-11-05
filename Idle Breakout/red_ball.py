import ball
import blocks
from wrap import sprite as sp
import wrap


class Red_ball(ball.Ball):
    def __init__(self,id=id):
        ball.Ball.__init__(self,id=id)
        wrap.sprite_text.set_text_color(self.name, 255, 59, 88)

    def check_collide_x(self):
        for one_block in blocks.Block.all_blocks:
            if sp.is_collide_sprite(self.name, one_block.name):
                blocks.Block.change_block(one_block, pover_ball=self.power)
                if one_block.value > 0:
                    self.speed_x = -self.speed_x
                    sp.move(self.name, self.speed_x, 0)
                    break

    def check_collide_y(self):
        for one_block in blocks.Block.all_blocks:
            if sp.is_collide_sprite(self.name, one_block.name):
                blocks.Block.change_block(one_block, pover_ball=self.power)
                if one_block.value > 0:
                    self.speed_y = -self.speed_y
                    sp.move(self.name, 0, self.speed_y)
                    break
