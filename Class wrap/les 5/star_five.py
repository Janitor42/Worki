import time
import wrap
from wrap import sprite as sp
from random import randint as rd

wrap.add_sprite_dir("C:/Users/i'm/PycharmProjects/Worki/Class wrap/les 5")


class Star:
    def __init__(self, x, y, size, number, list_stars):
        self.x = x
        self.y = y
        self.size = size
        self.number = number
        self.live = True
        self.list_stars = list_stars

        self.name = sp.add('picture', self.x, self.y, 'star_five')
        self.name_number = sp.add_text(str(self.number), self.x, self.y,
                                       text_color=(255, 255, 255),
                                       bold=True, back_color=(0, 0, 0))

        sp.set_width_proportionally(self.name, self.size)

    def __del__(self):
        sp.remove(self.name)
        sp.remove(self.name_number)

    def light_star(self):
        if self.size < 60:
            self.size += 1
            sp.set_width_proportionally(self.name, self.size)
        else:
            self.size = 20

    def check_star_on_del(self):
        if not self.live:
            self.list_stars.remove(self)




