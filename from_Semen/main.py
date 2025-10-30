import tkinter as tk

import field
from from_Semen.square import Square

win = tk.Tk()
win.title("First")
win.geometry("500x700+740+250")
win.minsize(200, 200)
win.maxsize(1000, 1000)
win.config(background="black")

field.make_field(win=win)
Square(win=win)

win.mainloop()
