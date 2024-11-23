import tkinter as tk
import random as rd
import object

all_fields = []
coord_fields = {}


def create_field(frame):
    row = 1
    column = 1
    for i in range(1, 17):
        Field(frame=frame, row=row, column=column)
        column += 1
        if i % 4 == 0:
            column = 1
            row += 1


class Field:
    count = 1

    def __init__(self, frame, row, column):
        self.label = (tk.Label(frame, background='green', width=10, height=5,
                               text=f'R{row}C{column}'))
        self.label.grid(row=row, column=column, padx=(10, 10), pady=(10, 10))

        self.row = row
        self.column = column
        self.state = 'open'
        self.button = None

        coord_fields[row, column] = self
        all_fields.append(self)

    def close_state(self):
        self.state = 'close'
        self.label.config(background='red')

    def open_state(self):
        self.state = 'open'
        self.label.config(background='green')