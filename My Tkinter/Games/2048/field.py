import tkinter as tk
import object

all_fields = []
busy_fields = []


def create_field(frame):
    row = 1
    column = 1
    for i in range(1, 17):
        Field(frame=frame,row=row, column=column)
        column += 1
        if i % 4 == 0:
            column = 1
            row += 1


class Field:
    def __init__(self, frame, row, column):
        self.label = (tk.Label(frame, background='green', width=10, height=5,
                               text=f'R{row}C{column}'))
        self.label.grid(row=row, column=column,padx = (10, 10), pady = (10, 10))

        self.row = row
        self.column = column
        self.state='open'

        all_fields.append(self)


def new_place(row, column, direction_row, direction_column):
    for i in all_fields:
        if 0 < row + direction_row < 5 or 0 < column + direction_column < 5:
            if [row + direction_row, column + direction_column] == [i.row, i.column]:
                return i
        else:
            return False


def this_place(row, column):
    for i in all_fields:
        if [row, column] == [i.row, i.column]:
            return i
