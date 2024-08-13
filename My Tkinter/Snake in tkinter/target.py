import tkinter as tk
import random as rd


class Target:
    def __init__(self, screen):
        self.name = tk.Button(screen, text=' 3 ', font=('Arial', 15))
        self.x=rd.randint(50, 550)
        self.y=rd.randint(50, 550)
        self.name.place(x=self.x, y=self.y)

        self.collide_x = self.x+20
        self.collide_y = self.y+20

    def __del__(self):
        self.name.destroy()

    def next_target(self,screen):
        self.__del__()
        self.__init__(screen)