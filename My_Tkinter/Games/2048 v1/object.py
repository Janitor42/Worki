import tkinter as tk
import field
import random as rd
import time

all_buttons = []
coord_buttons = {}

count = 1


def create_button(how_many, frame):
    close_places = []
    for i in all_buttons:
        close_places.append([i.row, i.column])

    for i in range(how_many):
        rd_place = [rd.randint(1, 4), rd.randint(1, 4)]

        while rd_place in close_places:
            rd_place = [rd.randint(1, 4), rd.randint(1, 4)]

        Object(frame=frame, row=rd_place[0], column=rd_place[1])
        close_places.append(rd_place)
        field.coord_fields[rd_place[0], rd_place[1]].close_state()


def move(side, plus_row, plus_column, index):
    for q in range(side[0], side[1], side[2]):
        for i in coord_buttons:
            if i[index] == q:
                coord_buttons[i].move_now(plus_row=plus_row, plus_column=plus_column)


class Object:

    def __init__(self, frame, row, column):
        self.value = 2
        self.row = row
        self.column = column
        self.button = tk.Button(frame, text=self.value, font=('Arian', 20, 'bold'), width=3, padx=5, pady=10)
        self.button.grid(row=self.row, column=self.column, padx=(1, 0), pady=(1, 0))
        self.state = True
        all_buttons.append(self)
        coord_buttons[row, column] = self

    def __del__(self):
        self.button.destroy()
        for i in all_buttons:
            if i==self:
                all_buttons.remove(i)
        self.button.destroy()

    def move_now(self, plus_row, plus_column):
        field.coord_fields[self.row, self.column].open_state()
        self.can_i_move(plus_row, plus_column)
        field.coord_fields[self.row, self.column].close_state()

    def can_i_move(self, plus_row, plus_column):
        while self.get_state(plus_row, plus_column) == 'open':
            self.row += plus_row
            self.column += plus_column
            self.button.grid(row=self.row, column=self.column)

        if self.get_state(plus_row, plus_column) == 'close':
            self.find_button(plus_row=plus_row, plus_column=plus_column)

    def find_button(self, plus_row, plus_column):
        for i in all_buttons:
            if [i.row, i.column] == self.get_coord(plus_row=plus_row, plus_column=plus_column):
                if i.value == self.value and self.state==True and i.state==True:
                    self.row = i.row
                    self.column = i.column
                    self.button.grid(row=self.row, column=self.column)
                    self.value = self.value * 2
                    self.button.config(text=self.value)
                    i.state = False
                    break
    def remove_button(self):
        if not self.state:
            self.__del__()

    def get_coord(self, plus_row, plus_column):
        return [field.coord_fields[self.row + plus_row, self.column + plus_column].row,
                field.coord_fields[self.row + plus_row, self.column + plus_column].column]

    def get_state(self, plus_row, plus_column):
        if not self.state:
            return False
        if plus_row == 1:
            if self.row + plus_row == 5:
                return False
        if plus_row == -1:
            if self.row + plus_row == 0:
                return False
        if plus_column == 1:
            if self.column + plus_column == 5:
                return False
        if plus_column == -1:
            if self.column + plus_column == 0:
                return False

        return field.coord_fields[self.row + plus_row, self.column + plus_column].state

def recording_key():
    coord_buttons.clear()
    for i in all_buttons:
        row = i.row
        column = i.column
        coord_buttons[row, column] = i

def remove_buttons():
    for i in all_buttons:
        i.remove_button()
