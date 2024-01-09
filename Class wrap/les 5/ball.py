import wrap
from wrap import sprite as sp
import figure

win_x = 500
win_y = 500


class Ball(figure.Figure):
    number = 1

    def __init__(self, x, y, speed_x, speed_y, size):
        super().__init__(x, y, size)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.choice_costume()
        sp.set_width_proportionally(self.name, self.size)
        self.name_number = sp.add_text(str(self.number), self.x, self.y, bold=True)
        self.name_size = sp.add_text(str(self.size), self.x, self.y + 20, font_size=15)
        Ball.number += 1

    def choice_costume(self):
        if self.size <= 30:
            self.name = sp.add('picture', self.x, self.y, 'red')
        if 30 < self.size <= 60:
            self.name = sp.add('picture', self.x, self.y, 'yellow')
        if self.size > 60:
            self.name = sp.add('picture', self.x, self.y, 'green')

    def move(self):
        self._check_window()
        sp.move(self.name, self.speed_x, self.speed_y)
        sp.move(self.name_number, self.speed_x, self.speed_y)
        sp.move(self.name_size, self.speed_x, self.speed_y)

    def collide(self, stars):
        for star in stars:
            if sp.is_collide_sprite(self.name, star.name):
                self._change_size(star.number)
                self._maybe_change_costume()
                star.live = False

    def maybe_division(self):
        if self.size >= 100:
            return True

    def del_obj_ball(self):
        sp.remove(self.name)
        sp.remove(self.name_number)
        sp.remove(self.name_size)

    def _check_window(self):
        if sp.get_x(self.name) <= self.size // 2:
            self.speed_x = abs(self.speed_x)
        if sp.get_x(self.name) >= win_x - self.size // 2:
            self.speed_x = -(self.speed_x)
        if sp.get_y(self.name) <= self.size // 2:
            self.speed_y = abs(self.speed_y)
        if sp.get_y(self.name) >= win_x - self.size // 2:
            self.speed_y = -(self.speed_y)

    def _change_size(self, number):
        self.size += number
        sp.set_width_proportionally(self.name, self.size)
        wrap.sprite_text.set_text(self.name_size, str(self.size))

    def _maybe_change_costume(self):
        if 0 < self.size <= 30:
            sp.set_costume(self.name, 'red')
        if 30 < self.size <= 60:
            sp.set_costume(self.name, 'yellow')
        if 100 > self.size > 60:
            sp.set_costume(self.name, 'green')
