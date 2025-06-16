import tkinter as tk
import string
import random

class Button:

    def __init__(self, xb, yb, xl, yl,money):
        self.bt_left = tk.Button(text='<',
                                command=self.left)
        self.bt_left.place(x=xb, y=yb)
        self.bt_right = tk.Button(text='>',
                                 command=self.right)
        self.bt_right.place(x=xb+58, y=yb)
        self.lb = tk.Label(text=random.choice(list(string.ascii_lowercase)),
                           font=("Arial", 40),
                           width=3)
        self.lb.place(x=xl, y=yl)

        self.money=money

    def change(self):
        self.lb['text'] = random.choice(list(string.ascii_lowercase))

    def right(self):
        letters = list(string.ascii_lowercase)
        for i in range(len(letters)):
            if letters[i] == self.lb['text']:
                if i == len(letters) - 1:
                    self.lb['text'] = letters[0]
                    self.money['text']=int(self.money['text']-1)
                else:
                    self.lb['text'] = letters[i + 1]
                    self.money['text']=int(self.money['text']-1)
                break

    def left(self):
        letters = list(string.ascii_lowercase)
        letter_now = self.lb['text']
        index_now = letters.index(letter_now)
        if index_now == 0:
            letter_next = letters[25]
        else:
            letter_next = letters[index_now - 1]
        self.lb['text'] = letter_next