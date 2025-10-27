import random as rd
import threading

from wrap import sprite

balls = []
balls_lock = threading.Lock()


def make_balls(count):
    with balls_lock:
        for i in range(count):
            balls.append(Ball())


def find_ball(part_gui):
    with balls_lock:
        for i in balls:
            if part_gui.number_value == i.number_value:
                return i


class Ball:
    count = 0

    def __init__(self):
        self.name = sprite.add('pacman',
                               rd.randint(20, 480),
                               rd.randint(20, 480),
                               'player3')
        Ball.count += 1
        self.number_value = Ball.count
        self.number_text = sprite.add_text(str(Ball.count),
                                           sprite.get_x(self.name),
                                           sprite.get_y(self.name))
        self.x = rd.choice([-2, -1, 1, 2])
        self.y = rd.choice([-2, -1, 1, 2])

        self.left = 0
        self.right = 0
        self.up = 0
        self.down = 0

    def change_position(self):
        self.check_position()
        sprite.move(self.name, self.x, self.y)
        sprite.move(self.number_text, self.x, self.y)

    def check_position(self):

        if sprite.get_left(self.name) <= 0:
            self.x = abs(self.x)
            self.left += 1
        if sprite.get_right(self.name) >= 500:
            self.x = -self.x
            self.right += 1

        if sprite.get_top(self.name) <= 0:
            self.y = abs(self.y)
            self.up += 1
        if sprite.get_bottom(self.name) >= 500:
            self.y = -self.y
            self.down += 1
