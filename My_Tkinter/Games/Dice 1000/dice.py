import tkinter as tk
import random as rd


class Dice:
    dice_faces = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

    def __init__(self, screen, x, y):
        self.screen = screen

        self.x = x
        self.y = y
        self.value = rd.randint(1, 6)
        self.dice = tk.Button(self.screen, text=Dice.dice_faces[self.value - 1],
                              background='white', font=('arial', 80), command=self.action)
        self.dice.place(x=self.x, y=self.y, width=50, height=50)

        self.rotate_cube = tk.Button(self.screen, text='->', command=self.rotate)
        self.rotate_cube.place(x=self.x, y=self.y - 50)

    def reroll(self):
        self.value = rd.randint(1, 6)
        self.dice['text'] = Dice.dice_faces[self.value - 1]

    def rotate(self):
        if self.value == 6:
            self.value = 1
            self.dice['text'] = Dice.dice_faces[self.value - 1]
        else:
            self.value += 1
            self.dice['text'] = Dice.dice_faces[self.value - 1]

    def action(self):
        if self.dice['bg'] == 'white':
            self.dice['bg'] = 'red'
        else:
            self.dice['bg'] = 'white'

    def get_color(self):
        return self.dice['bg']

    def get_value(self):
        return self.value

    def get_text(self):
        return self.dice['text']