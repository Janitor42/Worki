import tkinter as tk
import field
import random as rd

all_buttons = []
coord_buttons = {}


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


def move_down():
    for q in range(3, 0, -1):
        for i in coord_buttons:
            if i[0] == q:
                coord_buttons[i].move_now()
    print('-----------------------')


class Object:

    def __init__(self, frame, row, column):
        self.value = 2
        self.row = row
        self.column = column
        self.button = tk.Button(frame, text='2', font=('Arian', 20, 'bold'), width=3, padx=5, pady=10)
        self.button.grid(row=self.row, column=self.column, padx=(1, 0), pady=(1, 0))
        all_buttons.append(self)
        coord_buttons[row, column] = self

    def move_now(self):
        field.coord_fields[self.row,self.column].open_state()
        self.can_i_move()
        field.coord_fields[self.row,self.column].close_state()



    def can_i_move(self):
        while self.get_state() == 'open':
            self.row += 1
            self.button.grid(row=self.row, column=self.column)

    def get_state(self):
        if self.row+1 == 5:
            return False
        return field.coord_fields[self.row + 1, self.column].state

        # while self.get_state() != 'close':
        #     if self.row == 4:
        #         break
        #     self.state = 'open'
        #     self.label.config(background='green')
        #     self.row += 1
        #     self.button.grid(row=self.row, column=self.column)

    # def get_state(self):
    #
    #     for field in all_fields:
    #         if [field.row, field.column] == [self.row + 1, self.column]:
    #             return field.state
    #
    # def paint_it(self):
    #     coord_fields[self.row, self.column].label.config(background='red')
    #     coord_fields[self.row, self.column].state = 'close'
