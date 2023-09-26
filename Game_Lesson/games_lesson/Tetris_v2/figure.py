import random

from wrap import sprite
import menu

log_turn = True
danger = False


class Figure:
    def __init__(self):
        self.names = []
        self.this_figure = 1
        self.calk_pos = []
        self.check = False
        self.turn = 0
        self._create_figure()

    def _clear_all(self):
        self.names.clear()
        self.calk_pos.clear()
        self.check = False
        self.turn = False
        self.this_figure = random.randint(1, 1)  # random value in one for 6

    def _create_figure(self):
        self._clear_all()
        if self.this_figure == 1:
            x = 110
            y = 0
            for i in range(4):
                self.names.append(sprite.add('pacman', x, y, 'dot'))
                sprite.set_size(self.names[-1], 28, 28)
                x += 30

    def move_figure(self, they):
        self.check = self._touch_line() or self._touch_blocks(they)
        self._move_figure()

    def _touch_line(self):
        return sprite.is_collide_any_sprite(menu.line3, self.names)

    def _touch_blocks(self, they):
        for g in they:
            if sprite.is_collide_any_sprite(g['name'], self.names):
                return True
        return False

    def _move_figure(self):
        if self.check:
            return
        for i in self.names:
            sprite.move(i, 0, 5)

    def remove_figure_and_add_up(self):
        if not self.check:
            return
        for i in self.names:
            sprite.hide(i)
            sprite.remove(i)
        self._create_figure()
        self.check = not self.check

    def left(self, field):
        moving(self.calk_pos, self.names, 20, -30, 'right', field)

    def right(self, field):
        moving(self.calk_pos, self.names, 280, 30, "left", field)

    def down(self):
        for i in self.names:
            sprite.move(i, 0, 30)

    def Turn(self, work_fields):
        old_angle = sprite.get_angle(self.names[0])
        self._choice_direction(self._self_old_param())
        if self._check_in_collide_all(menu.line_left, menu.line_right, work_fields):
            sprite.set_angle(self.names[0], old_angle)
            self._return_old_pos()

    def _choice_direction(self, one):
        if sprite.get_angle(self.names[0]) == 90:
            self._returns(one, 30, 0, 30, 0)
        elif sprite.get_angle(self.names[0]) == 180:
            self._returns(one, 0, 30, 0, 30)
        elif sprite.get_angle(self.names[0]) == -90:
            self._returns(one, -30, 0, -30, 0)
        else:
            self._returns(one, 0, -30, 0, -30)

    def _self_old_param(self):
        self.calk_pos.clear()
        one = self.names[0]
        sprite.set_angle(self.names[0], sprite.get_angle(self.names[0]) + 90)
        for i in self.names:
            old_pos_x = sprite.get_x(i)
            old_pos_y = sprite.get_y(i)
            self.calk_pos.append(old_pos_x)
            self.calk_pos.append(old_pos_y)
        return one

    def _check_in_collide_all(self, line_left, line_right, work_fields):
        if sprite.is_collide_any_sprite(line_left, self.names) or sprite.is_collide_any_sprite(line_right, self.names):
            return True
        for i in work_fields:
            if sprite.is_collide_any_sprite(i['name'], self.names):
                return True

    def _return_old_pos(self):
        n = 0
        for i in self.names:
            sprite.move_to(i, self.calk_pos[n], self.calk_pos[n + 1])
            n += 2

    def _returns(self, one, x, y, add_x, add_y):
        for i in self.names:
            if one == i:
                continue
            else:
                sprite.move_to(i, sprite.get_x(one) + x, sprite.get_y(one) + y)
                x += add_x
                y += add_y


def moving(calk_pos, names, count, move, left, field):
    global danger
    calk_pos.clear()
    moving = True
    for i in names:
        x = sprite.get_x(i)
        calk_pos.append(x)
    for i in calk_pos:
        if i >= count and left == "left":
            moving = False
        if i <= count and left == "right":
            moving = False
    calk_pos.clear()
    for i in names:
        old_x = sprite.get_x(i)
        old_y = sprite.get_y(i)
        calk_pos.append(old_x)
        calk_pos.append(old_y)
    for i in names:
        if moving:
            sprite.move(i, move, 0)
            for q in field:
                if sprite.is_collide_sprite(q['name'], i):
                    danger = True
                    break
    if danger == True:
        n = 0
        for i in names:
            sprite.move_to(i, calk_pos[n], calk_pos[n + 1])
            n += 2
    danger = False
