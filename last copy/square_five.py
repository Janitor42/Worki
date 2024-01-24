import wrap
from wrap import sprite as sp
from random import randint as rd
import random
import ball_five

win_x = 800
win_y = 800
wrap.add_sprite_dir("C:/Users/i'm/PycharmProjects/Worki/Class wrap/les 5")


class Square:
    place = 1
    save_size = 20

    def __init__(self, size, x, y, list_square, list_balls):

        if self._find_place():
            self.min_save = Square.save_size
            self.max_save = self.min_save + 20
            Square.save_size += 20
        else:
            self.x = x
            self.y = y
            self.min_save = self.rd_randrange()
            self.max_save = self.min_save + 20
            self.group = random.choice(['A', 'B', 'C', 'D'])

        self.list_square = list_square
        self.list_balls = list_balls
        self.size = size

        self.name = sp.add('picture', self.x, self.y, costume='square_five')
        self.name_text = sp.add_text('Для шаров ' + str(self.group), self.x, self.y - self.size * 0.6)
        sp.set_width_proportionally(self.name, self.size)
        Square.place += 1

    def test(self):
        for one_ball in self.list_balls:
            if self.group == one_ball.group and sp.is_collide_sprite(self.name, one_ball.name):

                if one_ball.state == 'open':
                    sp.move_to(one_ball.name, self.x, self.y)
                    sp.move_to(one_ball.name_text, self.x, self.y)
                    sp.move_to(one_ball.name_size, self.x, self.y + 20)
                    sp.move_to(one_ball.name_state, self.x, self.y - 20)
                    one_ball.state = 'loct'
                    wrap.sprite_text.set_text(one_ball.name_state, one_ball.state)

            if one_ball.state == 'loct' and sp.is_collide_sprite(self.name, one_ball.name):
                if sp.get_right(one_ball.name) >= sp.get_right(self.name):
                    one_ball.speed_x = -abs(one_ball.speed_x)
                if sp.get_left(one_ball.name) <= sp.get_left(self.name):
                    one_ball.speed_x = abs(one_ball.speed_x)
                if sp.get_bottom(one_ball.name) >= sp.get_bottom(self.name):
                    one_ball.speed_y = -abs(one_ball.speed_y)
                if sp.get_top(one_ball.name) <= sp.get_top(self.name):
                    one_ball.speed_y = abs(one_ball.speed_y)

            if one_ball.state == 'open':
                if sp.get_left(one_ball.name) <= 0:
                    one_ball.speed_x = abs(one_ball.speed_x)
                if sp.get_right(one_ball.name) >= win_x:
                    one_ball.speed_x = -abs(one_ball.speed_x)
                if sp.get_top(one_ball.name) <= 0:
                    one_ball.speed_y = abs(one_ball.speed_y)
                if sp.get_bottom(one_ball.name) >= win_y:
                    one_ball.speed_y = -abs(one_ball.speed_y)

    def _find_place(self):
        if Square.place < 5:
            x = 200
            y = 200
            group = 'A'
            for i in range(1, 5):
                if Square.place == i:
                    if i == 2:
                        x = 500
                        group = 'B'
                    elif i == 3:
                        y = 500
                        group = 'C'
                    elif i == 4:
                        x, y = 450, 450
                        group = 'D'
                    self.x, self.y = x, y
                    self.group = group
                    return True
        else:
            return False

    @staticmethod
    def rd_not_zero(min, max):
        return random.choice([i for i in range(min, max + 1) if i != 0])

    @staticmethod
    def rd_randrange():
        return random.randrange(20, 100, 20)
