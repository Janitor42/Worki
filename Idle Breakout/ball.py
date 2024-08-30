import screen
import tkinter as tk


def buy_ball():
    Ball()


class Ball:
    count_ball = []

    def __init__(self):
        self.x = int(screen.x) // 2
        self.y = int(screen.y) // 2
        self.size = 15
        self.name = screen.can.create_oval(
            self.x, self.y, self.x + self.size, self.y + self.size,
            fill='yellow')
        self.power = 1


