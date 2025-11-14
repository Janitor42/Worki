import tkinter as tk
from tkinter import ttk


def action():
    count = int(StartScreen.box.get())
    StartScreen.frame.destroy()
    !!!!

class StartScreen:
    root = tk.Tk()
    root.geometry('600x400')

    frame = tk.Frame(root, width=900, height=600, bg='black')
    frame.place(x=0, y=0)

    box = ttk.Combobox(frame, values=['1', '2', '3', '4', '5'])
    box.place(x=130, y=70)

    tk.Label(frame, text='bj').place(x=20, y=0)

    bt = tk.Button(frame, text='accept', command=action)
    bt.place(x=130, y=100)

    @classmethod
    def mainloop(cls):
        cls.root.mainloop()
