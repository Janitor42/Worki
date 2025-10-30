import tkinter as tk

import time
from turtledemo.sorting_animate import Block


def make_field(win):
    x = 80
    y = 120
    place_y = 1
    place_x = 1
    place = 1
    for i in range(35):
        Field(win=win, x=x, y=y, place_y=place_y, place_x=place_x, place=place)
        place += 1
        place_x += 1
        x += 70
        if x >= 380:
            place_y += 1
            place_x = 1
            x = 80
            y += 75


# x=70,y=75
class Field:
    all_fields = {}

    @classmethod
    def get_state_under_field(cls, key):
        field = cls.all_fields[key]
        return field.get_state()

    @classmethod
    def find_field(cls, block):
        text = block.fall_block['text']
        background = block.fall_block['background']
        cords = block.get_cords_block()

        for key, field in cls.all_fields.items():
            if field.get_cords() == cords:
                field.write_field(text, background)
                cls.find_neighbors(me=field)

    @classmethod
    def find_neighbors(cls, me):
        key = me.place
        text_me = me.field_block['text']

        neighbors = [cls.check_key(key=key, modify=+1),
                     cls.check_key(key=key, modify=+5),
                     cls.check_key(key=key, modify=-1),
                     cls.check_key(key=key, modify=-5)]

        for key in neighbors:
            if key:
                text = cls.all_fields[key].field_block['text']
                if text_me == text:
                    cls.all_fields[key].write_field(text='!!!', background='red')
                    me.write_field(text='!!!', background='red')

    @classmethod
    def find_place(cls, block):
        cords_block = block.get_cords_block()

        text = block.fall_block['text']
        background = block.fall_block['background']

        for key, field in cls.all_fields.items():
            cords_field = field.get_cords()
            cords_field = [cords_field[0], cords_field[1] - 70]
            if cords_field == cords_block and field.state == 'close' and cls.check_key(key=key, modify=-5):
                me = cls.all_fields[key - 5]
                me.write_field(text, background)
                cls.find_neighbors(me=me)
                return True

        return False

    @classmethod
    def check_key(cls, key, modify):
        key = key + modify
        if 0 < key < 36:
            return key
        return False

    def __init__(self, win, x, y, place_y, place_x, place):
        self.state = "open"

        self.place_y = place_y
        self.place_x = place_x
        self.place = place

        self.win = win
        self.x = x
        self.y = y
        self.field_block = tk.Label(win, text=f"", background="blue4", foreground="white", font=("Arial", 15), height=3,
                                    width=6,
                                    relief=tk.SOLID)
        self.field_block.place(x=self.x, y=self.y)
        Field.all_fields[self.place] = self

    def get_cords(self):
        return [self.x, self.y]

    def get_state(self):
        return self.state

    def write_field(self, text, background):
        self.state = "close"
        self.field_block.config(text=text, background=background)
