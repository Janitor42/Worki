import json
import tkinter as tk, random, time



# x=70,y=75
class Field:
    all_fields = {}

    @classmethod
    def make_field(cls, win):
        y = 620


        y_field = 1
        x_field = 1
        place = 1
        for i in range(21):
            y -= 26
            x = 120
            y_field += 1
            x_field = 1
            for j in range(10):
                Field(win=win, x=x, y=y, y_field=y_field, x_field=x_field, place=place)
                place += 1
                x += 26
                x_field += 1
    @classmethod
    def edit_block(cls,index):
        block=Field.all_fields[index]
        block.state="close"
        block.field_block.config(background="red",text="")
    @classmethod
    def get_block(cls,index):
        return cls.all_fields[index]






    def __init__(self, win, x, y, y_field, x_field, place):
        self.place = place
        self.state = "open"
        self.place_x = x_field
        self.place_y = y_field
        self.win = win
        self.x = x
        self.y = y
        self.field_block = tk.Label(win, text=f"{place}", background="blue4", foreground="white",
                                    font=("Arial", 13), height=1,
                                    width=2)
        self.field_block.place(x=self.x, y=self.y)
        Field.all_fields[self.place] = self

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
