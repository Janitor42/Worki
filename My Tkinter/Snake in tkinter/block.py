import tkinter as tk
import model
import string
import target
import time


class Block:

    def __init__(self, screen, x, y, part='Head'):
        self.name = tk.Button(screen, text=' 8 ', font=('Arial', 15))
        self.step = 0
        self.steps = []

        self.x = x
        self.y = y
        self.name.place(x=self.x, y=self.y)
        self.collide_x = [i for i in range(self.x, self.x + 41)]
        self.collide_y = [i for i in range(self.y, self.y + 41)]
        self.part = part

        if self.part=='Head':
            self.steps=[[250,250] for i in range(10)]
    def move(self, x, y):
        if self.part == 'Head':
            self.x = x
            self.y = y
            self.name.place(x=x, y=y)
            self.collide_x = [i for i in range(self.x, self.x + 41)]
            self.collide_y = [i for i in range(self.y, self.y + 41)]

            if len(self.steps) < 10:
                self.steps.append([self.x, self.y])
            if len(self.steps) > 9:
                self.steps.remove(self.steps[0])

        if self.part == 'Body':
            self.x = x
            self.y = y
            self.name.place(x=x, y=y)

            if len(self.steps) < 10:
                self.steps.append([self.x, self.y])
            if len(self.steps) > 9:
                self.steps.remove(self.steps[0])

    def check_collide(self, my_target):
        if self.part == 'Head':
            if ((my_target.collide_x + 20 in self.collide_x or my_target.collide_x - 20 in self.collide_x) and
                    (my_target.collide_y + 20 in self.collide_y or my_target.collide_y - 20 in self.collide_y)):
                my_target.next_target(model.screen)
                return True

