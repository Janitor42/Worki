import random
import tkinter as tk

win = tk.Tk()
win.geometry('500x500')
win.config(background='black')
size = 20

x_bt = 450
y_bt = 450

x_dot = 50
y_dot = 50

count = tk.IntVar()
count.set(0)

click = False


def rd_place():
    return random.randint(15, 485)


def collide():
    global x_dot, y_dot
    if (x_bt + 10 in [i for i in range(x_dot - 10, x_dot + size + 10)]
            and y_bt + 10 in [i for i in range(y_dot - 10,y_dot + size + 10)]):
        button.place(x=x_dot, y=y_dot)
        count.set(int(count.get()) + 1)
        x_dot = rd_place()
        y_dot = rd_place()
        dot.place(x=x_dot, y=y_dot)


def on_click(event=None):
    global click
    click = True


def out_click(event=None):
    global click
    click = False
    collide()


def move_to_me(event):
    global x_bt, y_bt
    if click:
        x_bt = x_bt + event.x - 10
        y_bt = y_bt + event.y - 10
        button.place(x=x_bt, y=y_bt)


dot = tk.Label(win, text='     ', font=size, background='red')
dot.place(x=x_dot, y=y_dot)

label3 = tk.Label(win, textvariable=f'{count}', font=('Arial', 15), background='red', )
label3.place(x=450, y=50)

button = tk.Button(win, text='go', font=size)
button.place(x=x_bt, y=y_bt)

button.bind('<ButtonPress>', on_click)
button.bind('<ButtonRelease>', out_click)
win.bind('<Motion>', move_to_me)

win.mainloop()
