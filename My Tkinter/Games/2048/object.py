import tkinter as tk
import field
import random as rd

all_objects = []


def create_object(how_many, frame):
    for i in range(how_many):

        # if len(field.busy_fields)==16:
        #     print('game over')

        choice_field = rd.choice(field.all_fields)
        while choice_field in field.busy_fields:
            choice_field = rd.choice(field.all_fields)
        field.busy_fields.append(choice_field)

        choice_field.state = 'busy'
        choice_field.label.config(background='firebrick4')
        Object(frame=frame, row=choice_field.row, column=choice_field.column)


class Object:

    def __init__(self, frame, row, column):
        self.value=2
        self.row=row
        self.column=column
        self.button = tk.Button(frame, text='2', font=('Arian',20,'bold'),width=3,padx=5,pady=10)
        self.button.grid(row=self.row, column=self.column,padx=(1,0),pady=(1,0))
        all_objects.append(self)

