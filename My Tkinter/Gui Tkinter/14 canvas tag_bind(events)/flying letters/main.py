import time

import letter
import time as ti
import tkinter as tk

def create_letter(event):
    letter.add_letter(can=can)



win = tk.Tk()
x = '800'
y = '800'
win.geometry(x + 'x' + y)
win.config(background='black')

can = tk.Canvas(bg='white', width=int(x) - 50, height=int(y) - 50)
can.pack(anchor='s', pady=10)



can.bind('<ButtonPress-1>', create_letter)





while True:

    letter.move_all(can=can)
    time.sleep(0.0001)
    win.update()

