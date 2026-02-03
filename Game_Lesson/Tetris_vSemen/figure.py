import tkinter as tk
import field
from type_figure import Type_figure

class Figure:
    def __init__(self, win):
        self.win = win
        self.figure=Type_figure(self.win)
        print(self.figure)

        self.win.bind("<Left>", self.move_left)
        self.win.bind("<Right>", self.move_right)
        self.win.bind("<Key-e>", self.rotate)
    def move_left(self,event):
        self.figure.move_left()
    def move_right(self,event):
        self.figure.move_right()
    def rotate(self, event):
        self.figure.rotate()
    # def move_right(self,event):
    #     self.fall_figure = tk.Label(win, text=f"", background="yellow", foreground="white",
    #                                 font=("Arial", 13), height=1,
    #                                 width=2)
    #     center_block=field.Field.get_block(index=195)
    #     self.speed=2
    #     self.fall_figure.place(x=center_block.x, y=center_block.y)
    #     self.win.bind("<KeyPress>",self.set_faster_speed)
    #     self.win.bind("<KeyRelease>",self.set_normal_speed)
    #     self.win.bind("<Left>", self.move_left)
    #     self.win.bind("<Right>", self.move_right)
    #     self.x=center_block.x
    #     self.y=center_block.y
    #     self.position=195
    #     self.win.after(10, self.fall)
    # def move_left(self, event=None):
    #     if self.x > 120 :
    #         self.x -= 26
    #         self.position +=1
    #         self.fall_figure.place(x=self.x, y=self.y)
    #
    # def move_right(self, event=None):
    #     if self.x < 354 :
    #         self.x += 26
    #         self.position -= 1
    #         self.fall_figure.place(x=self.x, y=self.y)
    # def set_normal_speed(self,event=None):
    #     self.speed=2
    # def set_faster_speed(self, event=None):
    #     if event.keysym == "space":
    #         self.speed=4
    # def fall(self):
    #     print(self.speed)
    #     if self.down_position():
    #         self.y+=self.speed
    #         self.fall_figure.place(x=self.x, y=self.y)
    #         self.win.after(10, self.fall)
    # def down_position(self):
    #     if self.y>595:
    #         return True
    #     return False
