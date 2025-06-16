import tkinter as tk
import object
import string
import random

window = tk.Tk()
window.title("first")
window.geometry("400x600")
window.config(background="Grey")
xb, yb, xl, yl = 80, 200, 80, 140
pole_whole = []
money = tk.Label(text=500)
money.place(x=350, y=550)


for i in range(3):
    pole = object.Button(xb, yb, xl, yl,money)
    xb += 100
    xl += 100
    pole_whole.append(pole)


def randomising():
    for elem in pole_whole:
        elem.change()
    money['text'] -= 10


r_button = tk.Button(text='random',
                     command=randomising)
r_button.place(x=50, y=550)




window.mainloop()
