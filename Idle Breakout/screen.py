import random as rd
import tkinter as tk
import time
import mouse


win = tk.Tk()
x = '800'
y = '600'
win.geometry(x + 'x' + y)
win.config(background='LightSteelBlue')

can = tk.Canvas(bg='white', width=int(x) - 50, height=int(y) - 100)
can.pack(anchor='s', pady=(15, 0))


