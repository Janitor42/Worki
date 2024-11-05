import tkinter as tk
import random as rd
import ball
import screen_wrap
import finance

import creator_balls

prices = [25, 200, 1500, 10000, 30, 75000]  # [25, 200, 1500, 10000, 75000, 75000]
colors = ['yellow', 'purple', 'green', 'blue', 'red', 'black']


def create_shop(win):
    frame_balls = tk.Frame(win, background='green')
    frame_balls.place(x=0, y=0, width=400, height=80)
    for i in range(6):
        Shop_ball(frame_balls, column=i, price=prices[i], all_colors=colors)


id = 0
person_id = []


def creator_id():
    global id
    id += 1
    person_id.append(id)


class Shop_ball:
    def __init__(self, frame_balls, column, price, all_colors):
        self.name = all_colors[column]
        self.price_and_text = tk.Label(frame_balls, text=f'{price}')
        self.price_and_text.grid(row=0, column=column, padx=(17, 0), pady=(5, 0))

        self.button = tk.Button(frame_balls, text='O', font=('Arial', 15, 'bold')
                                , foreground=all_colors[column], background='#bfbccf',
                                width=3, command=self.buy_ball)
        self.button.grid(row=1, column=column, padx=(17, 0))

    def buy_ball(self):
        if finance.Finance.money >= int(self.price_and_text['text']):
            creator_id()
            self.redefinition(id)
            price = self.price_and_text['text']
            finance.subtraction_money(int(price))
            self.price_and_text['text'] = int(int(self.price_and_text['text']) * 1.5)

    def redefinition(self, id):
        creator_balls.create_new_record(self.name, id)

# todo (база данных покемонов) pokeapi
# todo object lock in module Thread
