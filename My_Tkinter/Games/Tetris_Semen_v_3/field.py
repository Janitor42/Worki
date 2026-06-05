import json
import tkinter as tk, random, time
import constants
from square import Square

# x=70,y=75


class Field:
    LEFT_BORDER = 120
    RIGHT_BORDER = 354

    all_fields = []
    all_fields_pos = {}
    first_deleted_column = False
    fallen_figure=[]
    """Поле"""
    #region

    @classmethod
    def find_field(cls, row, column):
        for i in cls.all_fields:
            if i.row_column == [row, column]:
                return i

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

    #endregion

    """методы set, get и т.д."""
    #region
    @classmethod
    def set_place(cls, start_place):
        for i in reversed(cls.all_fields):
            if [i.get_row(), i.get_column()] == start_place:
                return i
        return None

    # endregion

    """Удаление , Падение колонок"""
    #region
    @classmethod
    def check_fill_columns(cls):
        cls.first_deleted_column = False
        for i in range(constants.MIN_COLUMN_FIELD, constants.MAX_COLUMN_FIELD):
            start = 230 - (i * 10 + 9)
            end = 230 - (i * 10 - 1)
            all_index_column = [i for i in range(start, end)]
            cls.check_column(all_index_column)
        if cls.first_deleted_column!=False:
            cls.find_fallen_figure()
    @classmethod
    def check_column(cls, all_index_column):
        for b in all_index_column:
            if Field.all_fields[b - 1].state == "open":
                return
        else:
            cls.delete_column(all_index_column)

    @classmethod
    def delete_column(cls, all_index_column):
        for b in all_index_column:
            Field.all_fields[b - 1].play_square.place_forget()
            Field.all_fields[b - 1].state = "open"
        if cls.first_deleted_column==False:
            cls.first_deleted_column=all_index_column

    @classmethod
    def find_fallen_figure(cls):
        fallen_figure=[]
        for i in cls.all_fields:
            index=cls.first_deleted_column[0]
            other_column=i.get_column()
            deleted_column=cls.all_fields[index].get_column()
            x = Square(win=i.win, x=i.get_x(),
                       y=i.get_y(),
                       row=i.get_row(), column=i.get_column(),
                       color=i.play_square["background"])
            if other_column<deleted_column:
                if i.state=="close":
                    fallen_figure.append(x)


        cls.fallen_figure=fallen_figure


    #endregion

    def __init__(self, win, x, y, row, column, place):
        self.win = win

        self.state = "open"
        self.row = row
        self.column = column
        self.x = x
        self.y = y
        self.row_column = [row, column]
        self.place = place
        self.play_square = tk.Label(win, text=f"{column}", background="blue4",
                                    foreground="white", font=("Arial", 10),
                                    height=1, width=2)
        self.play_square.place_forget()
        self.field_block = tk.Label(win, text=f'{place}', background="blue4",
                                    foreground="white", font=("Arial", 10),
                                    height=1, width=2)
        self.field_block.place(x=self.x, y=self.y)

        Field.all_fields.append(self)
        Field.all_fields_pos[self.get_pos()] = self

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_pos(self):
        return f"{self.x, self.y}"

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column
