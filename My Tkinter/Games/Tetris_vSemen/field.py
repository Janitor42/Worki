import json
import tkinter as tk, random, time


# x=70,y=75


class Field:
    LEFT_BORDER = 120
    RIGHT_BORDER = 354

    all_fields = []

    @classmethod
    def make_field(cls, win):

        y = 620
        column = 23
        place = 1
        for i in range(23):
            y -= 26
            x = 120

            row = 1

            for j in range(10):
                Field(win=win, x=x, y=y, row=row, column=column, place=place)
                place += 1
                x += 26
                row += 1
            column -= 1

    @classmethod
    def set_place(cls, start_place):
        for i in reversed(cls.all_fields):

            if [i.get_row(), i.get_column()] == start_place:
                return i

        return None

    def __init__(self, win, x, y, row, column, place):
        self.win = win

        self.state = "open"
        self.row = row
        self.column = column
        self.x = x
        self.y = y
        self.row_column = [row, column]
        self.place = place

        self.field_block = tk.Label(win, text=f"", background="blue4",
                                    foreground="white", font=("Arial", 10),
                                    height=1, width=2)
        self.field_block.place(x=self.x, y=self.y)

        Field.all_fields.append(self)



    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_pos(self):
        return [self.x, self.y]

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column
