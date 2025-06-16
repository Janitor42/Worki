import time
import random

import tkinter as tk


win = tk.Tk()

win.geometry('800x800+100+200')
win.config(background='black')

can = tk.Canvas(width=800, height=800, bg='gray25')
can.place(x=0, y=0)
colors = ['red', 'white', 'blue', 'green', 'purple']

switch = False

all_objects = []


def create_circles():
    global switch
    for z in range(5):
        x = random.choice([-2, -1, 1, 2])
        y = random.choice([-2, -1, 1, 2])
        s = can.create_text(random.randint(20, 780), random.randint(20, 780), fill=colors[0], text='o',
                            font=('Arial', 30))

        diki = {'figure': s, 'coord_x': x, 'coord_y': y}
        all_objects.append(diki)

    switch = True


def go():

    for i in all_objects:
        can.move(i['figure'], i['coord_x'], i['coord_y'])
        touch(i)
    #     value = value + 1


# def delete():
#     for i in range(3):
#         a = random.choice(square)
#         s = square.index(a)
#         coords.remove(s)
#         print(s)
#         can.delete(a)
#         square.remove(a)


def touch(object):
    x, y = can.coords(object['figure'])

    if x >= 780:
        object['coord_x'] = -int(object['coord_x'])
        # coords[value][0] = -coords[value][0]
    # if cords[1] >= 780:
    #     coords[value][1] = -coords[value][1]
    # if cords[0] <= 20:
    #     coords[value][0] = abs(coords[value][0])
    # if cords[1] <= 20:
    #     coords[value][1] = abs(coords[value][1])


button_go = tk.Button(win, text='go', font=('Arial', 15, "bold"), width=10, command=create_circles)
button_go.place(x=175, y=400)
# button_del = tk.Button(win, text='del', font=('Arial', 15, "bold"), width=10, command=delete)
# button_del.place(x=350, y=400)
while True:
    win.update()
    if switch:
        go()
    time.sleep(0.01)
