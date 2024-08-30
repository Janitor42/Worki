import tkinter as tk
import ball

class Gui:
    def __init__(self, win):
        self.buy_ball = tk.Button(win, text='o', font=('Arial', 20),command=ball.buy_ball)
        self.buy_ball.pack()
