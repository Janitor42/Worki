import ball
import blocks
from wrap import sprite as sp
import wrap
import screen_wrap
import blue_children


class Blue_ball(ball.Ball):
    def __init__(self, id=id):
        ball.Ball.__init__(self, id=id)
        wrap.sprite_text.set_text_color(self.name, 0, 30, 201)

    def _check_window(self):

        if sp.get_left(self.name) <= 0:
            self.speed_x = abs(self.speed_x)
            self.create_children()

        if sp.get_right(self.name) >= screen_wrap.x:
            self.speed_x = -self.speed_x
            self.create_children()

        if sp.get_top(self.name) <= 0:
            self.speed_y = abs(self.speed_y)
            self.create_children()

        if sp.get_bottom(self.name) >= screen_wrap.y:
            self.speed_y = -self.speed_y
            self.create_children()

    def create_children(self):
        for i in range(2):
            ball.Ball.numbers -= 1
            blue_children.Blue_children(self)

