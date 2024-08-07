import random as rd
import string as st
from wrap import sprite as sp

count = 0
screen_x = 800
screen_y = 800


def rd_not_zero(mini, maxi):
    return rd.choice([i for i in range(mini, maxi + 1) if i != 0])


class Character:
    count = 0

    def __init__(self, speed_x, speed_y):

        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__impulse = rd_not_zero(-10, 10)
        self.name = sp.add_text(rd.choice(st.ascii_lowercase), rd.randint(50, 750), rd.randint(50, 750),
                                bold=True, font_size=rd.randint(20, 40),
                                text_color=(rd.randint(20, 254), rd.randint(20, 254), rd.randint(20, 254)),
                                font_name='Comic Sans MS')
        Character.count += 1

    def __del__(self):
        Character.count -= 1
        sp.remove(self.name)

    def _check_window(self):

        if sp.get_left(self.name) <= 0:
            self.__speed_x = abs(self.__speed_x)
        if sp.get_right(self.name) >= screen_x:
            self.__speed_x = -self.__speed_x

        if sp.get_top(self.name) <= 0:
            self.__speed_y = abs(self.__speed_y)
        if sp.get_bottom(self.name) >= screen_y:
            self.__speed_y = -self.__speed_y

    def move(self):
        self._check_window()
        sp.move(self.name, self.__speed_x, self.__speed_y)
        sp.set_angle(self.name, sp.get_angle(self.name) + self.__impulse)

    @staticmethod
    def move_all(all_sym):
        for i in all_sym:
            i.move()
