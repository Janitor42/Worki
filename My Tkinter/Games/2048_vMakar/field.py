import tkinter as tk
import random
import time


class Field:
    my_field = {}
    animate_speed = 0.004
    collapse = False

    @classmethod
    def find_place_down(cls, next_place_cube):
        obj_field = cls.my_field[next_place_cube]
        return obj_field

    @classmethod
    def rewrite_place(cls, obj_cube):
        number_on_desk = obj_cube.get_cube_place_on_desk()
        if number_on_desk >= 1:
            obj_field = cls.my_field[number_on_desk]
            obj_field.create_play_square(cube=obj_cube)

    @classmethod
    def fall_all_play_squares(cls):

        play_square = cls.find_all_play_squares()

        for obj_field in play_square:
            obj_field: Field

            place_down = obj_field.get_number_on_desk() + 5

            if place_down in cls.my_field.keys() and cls.my_field[place_down].state == 'open':
                neighbor = cls.my_field[place_down]
                obj_field.animate_cube_to_cube(neighbor=neighbor)

                neighbor.set_new_value(old_value=obj_field.play_square['text'])
                obj_field.reset_play_square()
                Field.collapse = True
                return cls.fall_all_play_squares()

        return False

    @classmethod
    def find_all_play_squares(cls):
        play_square = []

        for im in cls.my_field:
            obj_field = cls.my_field[im]
            obj_field: Field
            if obj_field.get_state() != 'open':
                play_square.append(obj_field)

        return play_square

    @classmethod
    def connect_all_play_squares(cls):
        play_square = cls.find_all_play_squares()
        for obj_field in play_square:
            obj_field: Field

            neighbors = Field.find_him_neighbors(obj_field.number_on_desk)
            if Field.check_him_neighbors(neighbors=neighbors, obj_field=obj_field):
                Field.collapse = True
                return Field.connect_all_play_squares()

        return False

    @staticmethod
    def find_him_neighbors(im):
        # top side (номера 1-5)
        if im <= 5:
            if im == 1:  # левый верхний угол
                return [im + 1, im + 5]
            elif im == 5:  # правый верхний угол
                return [im - 1, im + 5]
            else:  # верхний ряд, не углы
                return [im + 1, im - 1, im + 5]

        # right side (правый край)
        elif im % 10 in [0, 5]:
            if im == 30:  # правый нижний угол
                return [im - 1, im - 5]
            return [im + 5, im - 1, im - 5]

        # left side (левый край)
        elif im % 10 in [6, 1]:
            if im == 26:  # левый нижний угол
                return [im + 1, im - 5]
            return [im + 1, im + 5, im - 5]

        # default side (середина поля)
        else:
            if im in [27, 28, 29]:  # нижний ряд, не углы
                return [im + 1, im - 1, im - 5]
            return [im + 1, im + 5, im - 1, im - 5]

    @classmethod
    def check_him_neighbors(cls, neighbors, obj_field):
        for number in neighbors:
            neighbor = cls.my_field[number]
            neighbor: Field

            if neighbor.get_state() != 'open' and obj_field.get_value() == neighbor.get_value():
                obj_field.animate_cube_to_cube(neighbor=neighbor)
                neighbor.set_new_value()
                obj_field.reset_play_square()
                return True

        return False

    def animate_cube_to_cube(self, neighbor):
        self.play_square.lower()
        self.animate_square = tk.Label(self.screen, width=7, height=3,
                                       text=self.play_square['text'],
                                       font=('arial', 13), background=self.play_square['background'])

        self.animate_square.place(x=self.get_x(), y=self.get_y())

        self.screen.update_idletasks()

        t_start = time.time()

        while [self.animate_square.winfo_x(), self.animate_square.winfo_y()] != neighbor.get_pos():
            t_run = time.time()
            if t_run > t_start + Field.animate_speed:
                self.move_square_to_square(neighbor=neighbor)

                t_start = time.time()

            self.screen.update()
        self.animate_square.destroy()
        self.play_square.lift()

    def move_square_to_square(self, neighbor):
        neighbor: Field

        if self.animate_square.winfo_y() > neighbor.get_y():
            self.animate_square.place(x=self.animate_square.winfo_x(), y=self.animate_square.winfo_y() - 1)
        if self.animate_square.winfo_y() < neighbor.get_y():
            self.animate_square.place(x=self.animate_square.winfo_x(), y=self.animate_square.winfo_y() + 1)

        if self.animate_square.winfo_x() > neighbor.get_x():
            self.animate_square.place(x=self.animate_square.winfo_x() - 1, y=self.animate_square.winfo_y())
        if self.animate_square.winfo_x() < neighbor.get_x():
            self.animate_square.place(x=self.animate_square.winfo_x() + 1, y=self.animate_square.winfo_y())

    def __init__(self, screen, x, y, number):
        self.screen = screen

        self.number_on_desk = number
        self.x = x
        self.y = y
        self.pos = [x, y]

        self.state = "open"

        self.label = tk.Label(self.screen, width=9, height=4)
        self.label.place(x=self.x, y=self.y)

        self.play_square = tk.Label(self.screen, width=7, height=3, font=('arial', 13))
        self.play_square.place_forget()

        self.animate_square = None

        Field.my_field[self.number_on_desk] = self

    """set methods"""

    # region

    def create_play_square(self, cube):
        self.play_square.config(text=cube.cube['text'], background='yellow')
        self.play_square.place(x=cube.get_x(), y=cube.get_y())
        self.close_state()

    def close_state(self):
        self.state = "close"

    def open_state(self):
        self.state = 'open'

    def reset_play_square(self):
        self.open_state()
        self.play_square.config(text='')
        self.play_square.place_forget()

    def set_new_value(self, old_value=None):
        if self.play_square['text'] != '':
            self.play_square.config(text=int(self.play_square['text']) * 2)
        else:
            self.play_square.config(text=int(old_value))
            self.close_state()
            self.play_square.place(x=self.x, y=self.y)

    # endregion
    """get methods"""

    # region
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_pos(self):
        return [self.x, self.y]

    def get_number_on_desk(self):
        return self.number_on_desk

    def get_state(self):
        return self.state

    def get_value(self):
        return self.play_square['text']

    # endregion


def make_fields(screen):
    number = 0
    x = 0
    y = 0
    for i in range(6):
        x = 100
        y += 70
        for a in range(5):
            number += 1
            Field(screen, x, y, number)
            x += 73
