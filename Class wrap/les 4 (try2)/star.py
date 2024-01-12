import time
from wrap import sprite as sp
from random import randint as rd


class Star:
    def __init__(self, x, y, size, number, list_star):
        self.x = x
        self.y = y
        self.size = size
        self.number = number
        self.live = True

        self.name = sp.add('mario-items', self.x, self.y, 'star')
        self.name_number = sp.add_text(str(self.number), self.x, self.y, text_color=(255, 255, 255), bold=True,
                                       back_color=(0, 0, 0))
        sp.set_width_proportionally(self.name, self.size)

    def __del__(self):
        sp.remove(self.name)
        sp.remove(self.name_number)

    def light_star(self, i):
        if self.size < 60:
            self.size += 1
            sp.set_width_proportionally(self.name, self.size)
        else:
            self.size = 20

    def check_star(self, remove):
        if not self.live:
            remove(self)
