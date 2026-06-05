import json
from calendar import firstweekday

import constants
import tkinter as tk, random, time


class Field:
    # region Классовые переменные
    all_fields = {}
    buttons = []

    # endregion

    # region Логика cоздания поля
    @classmethod
    def make_field(cls, win):
        """Создание поля"""
        y = 830

        y_field = 1
        x_field = 1
        place = 0

        for i in range(10):
            y -= constants.DISTANCE_Y
            x = 40
            y_field += 1
            x_field = 1
            for j in range(10):
                color = random.choice(constants.COLORS)
                Field(win=win, x=x, y=y, y_field=y_field, x_field=x_field, place=place, color=color)
                place += 1
                x += constants.DISTANCE_X
                x_field += 1

    # endregion

    # region сборка поля до состояния в котором нет совпадений
    @classmethod
    def find_three(cls):
        flag = 0
        for value in cls.all_fields.values():
            horizontal = cls.it_exist(offset=constants.OFFSET_X, first=value)
            vertical = cls.it_exist(offset=constants.OFFSET_Y, first=value)
            flag += cls.three_same(data=horizontal)
            flag += cls.three_same(data=vertical)
        if flag:
            cls.find_three()

    @classmethod
    def it_exist(cls, offset, first):
        first: Field
        x, y = first.get_x(), first.get_y()
        second = f'{x + offset["x2"]} {y + offset["y2"]}'
        third = f'{x + offset["x3"]} {y + offset["y3"]}'
        if third in cls.all_fields:
            second = cls.all_fields[second]
            third = cls.all_fields[third]
            return [first, second, third]
        return None

    @staticmethod
    def three_same(data):
        flag = 0
        if not data:
            return 0
        x = {i.get_color() for i in data}
        if len(x) == 1:
            third = data[-1]
            colors = constants.COLORS.copy()
            colors.remove(third.get_color())
            third.set_color(color=random.choice(colors))
            flag = 1

        return flag

    # endregion

    # region Клик

    @classmethod
    def find_two_buttons_near(cls):
        button1 = cls.buttons[0]
        button2 = cls.buttons[1]
        for options in constants.OPTIONS_X_OR_Y:
            distance_x = options[0]
            distance_y = options[1]
            if [button1.get_x(), button1.get_y()] == [button2.get_x() + distance_x, button2.get_y() + distance_y]:
                return True
        return False

    @classmethod
    def change_two_buttons_colors(cls):
        button1 = cls.buttons[0]
        button2 = cls.buttons[1]
        color_1=button1.get_color()
        button1.set_color(color=button2.get_color())
        button2.set_color(color=color_1)

    # endregion

    # region init
    def __init__(self, win, x, y, y_field, x_field, place, color):
        self.color = color
        self.place = place
        self.state = "open"
        self.place_x = x_field
        self.place_y = y_field
        self.win = win
        self.x = x
        self.y = y
        self.field_block = tk.Button(win, text=f"{place}", background=self.color, foreground="white",
                                     font=("Arial", 13), height=3,
                                     width=6, command=self.click)
        self.field_block.place(x=self.x, y=self.y)
        Field.all_fields[f'{self.x} {self.y}'] = self

    # endregion

    # region get
    def get_color(self):
        """Возвращает цвет экземляра"""
        return self.color

    def get_x(self):
        """Возвращает x экземляра"""
        return self.x

    def get_y(self):
        """Возвращает y экземляра"""
        return self.y

    def get_pos(self):
        return f'{self.x} {self.y}'

    # endregion

    # region set
    def set_color(self, color):
        self.field_block['background'] = color
        self.color = color

    # endregion

    # region click
    def click(self):
        Field.buttons.append(self)
        if len(Field.buttons) < 2:
            return
        if Field.find_two_buttons_near():
            Field.change_two_buttons_colors()
            # todo вот здесь будем писать метод который запустит логику уничтожения части поля и т.д
        Field.buttons.clear()

    # endregion
