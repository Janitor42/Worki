import tkinter as tk

import field,figure,type_figure

win = tk.Tk()
type_figure.win=win
win.title("First")
win.geometry("500x700+740+250")
win.minsize(200, 200)
win.maxsize(1000, 1000)
win.config(background="black")

field.Field.make_field(win=win)
figure.Figure(win=win)
win.mainloop()