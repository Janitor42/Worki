import random

import tkinter as tk

from field import Field


class Square:
    me = None

    value_and_color = {
        2: "green1", 4: "DarkOliveGreen3", 8: "LightSalmon1", 16: "magenta",
        32: "medium purple", 64: "MediumTurquoise", 128: "MediumAquamarine",
        256: "medium sea green"
    }

    def __init__(self, win):
        self.win = win
        self.key = random.choice(list(Square.value_and_color.keys()))
        self.color = Square.value_and_color[self.key]
        self.fall_block = tk.Label(self.win, text=self.key, background=self.color, foreground="white",
                                   font=("Arial", 15), height=3, width=6, relief=tk.SOLID)
        self._x = 220
        self._y = 30
        self.place_x = 3
        self.place_y = 0
        self.fall_block.place(x=self._x, y=self._y)
        self._state = "active"

        self.win.bind("<a>", self.move_left)
        self.win.bind("<d>", self.move_right)
        self.win.bind("<space>", self.action)

        Square.me = self

    def update_block(self):
        self._x = 220
        self._y = 30
        self.place_x = 3
        self.place_y = 0
        self._state = "active"
        self.key = random.choice(list(Square.value_and_color.keys()))
        self.color = Square.value_and_color[self.key]
        self.fall_block.config(text=self.key, background=self.color)
        self.fall_block.place(x=self._x, y=self._y)

    def get_cords_block(self):
        return [self._x, self._y]

    def move_left(self, event=None):
        if self._x > 80 and self._state in "active":
            self._x -= 70
            self.place_x -= 1
            self.fall_block.place(x=self._x, y=30)

    def move_right(self, event=None):
        if self._x < 360 and self._state in "active":
            self._x += 70
            self.place_x += 1
            self.fall_block.place(x=self._x, y=30)

    def check_down_border(self):
        if self._y >= 570:
            self._y = 570
            self.fall_block.place(x=self._x, y=self._y)
            self._state = "disabled"

    def search_place(self):
        if Field.find_place(block=self):
            self._state = "disabled"

    def move_down(self):
        self._y += 5
        self.fall_block.place(x=self._x, y=self._y)
        self._state = "falling"

    def action(self, event=None):
        if Field.get_state_under_field(key=self.place_x) in 'open':
            self.fall()

    def fall(self, event=None):
        if self._state in ["active", 'falling']:
            self.move_down()
            self.check_down_border()
            self.search_place()
            self.win.after(10, self.fall)

        else:
            self.rewrite_new_block()
            return

    def rewrite_new_block(self):
        Field.find_field(block=self)
        self.update_block()
