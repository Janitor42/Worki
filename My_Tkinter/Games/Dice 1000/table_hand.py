import tkinter as tk


class Table_hand:
    hand = []

    @classmethod
    def create_table_hand(cls, x, y, screen):
        for i in range(5):
            Table_hand(x=x, y=y, screen=screen)
            x += 80

    @classmethod
    def clear_dices(cls):
        for i in cls.hand:
            i.hide_dice()

    @classmethod
    def write_dices(cls, data):
        for text in data:
            for i in cls.hand:
                if i.dice['text'] == '':
                    i.write_dice(text=text)
                    break

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.dice = tk.Label(self.screen, text='',
                             background='white', font=('arial', 80))
        self.dice.place(x=self.x, y=self.y, width=50, height=50)
        Table_hand.hand.append(self)

    def hide_dice(self):
        self.dice.config(text='', background='green', foreground='black')

    def write_dice(self, text):
        self.dice.config(text=text, background='black', foreground='white')
