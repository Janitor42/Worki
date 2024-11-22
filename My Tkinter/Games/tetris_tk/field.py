import tkinter as tk


def create_field(can):
    x = 2
    y = 2
    for i in range(1, 201):
        if x > 272:
            x = 2
            y += 30
        a = Field(can=can, x=x, y=y, number=i)
        all_places.append(a)
        x += 30


all_places = []


class Field:
    def __init__(self, can, x, y, number):
        self.x = x
        self.y = y
        self.name = can.create_rectangle(self.x, self.y, self.x + 30, self.y + 30, fill='yellow')
        self.number = number
        self.count = can.create_text(self.x + 15, self.y + 15, text=str(self.number))
        self.state = 'open'
