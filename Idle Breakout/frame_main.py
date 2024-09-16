import tkinter as tk
from tkinter import ttk

colors = ['yellow', 'purple', 'green', 'blue', 'red', 'black']


def create_frame_main(win):
    frame = tk.Frame(win, background='orange')
    frame.place(x=0, y=80, width=400, height=360)
    for i in range(len(colors)):
        Main_frame(frame, i)


class Main_frame:

    def __init__(self, frame, i):
        self.frame=frame
        self.bt = tk.Button(frame, text=colors[i],background=colors[i],foreground='gray80',font=('Arial',10,'bold'),
                            command=self.entrance)
        self.bt.grid(row=i, column=0, pady=(27, 0),sticky='we')


    def entrance(self):
        self.frame.config(background=self.bt['text'])