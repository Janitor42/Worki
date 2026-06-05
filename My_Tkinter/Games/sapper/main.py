import tkinter as tk
import field

win = tk.Tk()
win.config(background='black')
win.geometry('600x600')

can = tk.Canvas(background='yellow', width=500, height=500)
can.place(x=10, y=10)

field.Field(can=can)
win.mainloop()
