import time as ti
import tkinter as tk
import field
import figure

# def create_letter(event):
#     letter.add_letter(can=can)



win = tk.Tk()
x = '600'
y = '700'
win.geometry(x + 'x' + y)
win.config(background='black')

can = tk.Canvas(bg='white', width=302, height=602)
can.pack(anchor='sw', pady=(80,10),padx=(20,0))
field.create_field(can=can)

x=32
y=32



button=tk.Button(can,text='go',font=20,background='red')
button.place(x=30,y=30)

def move_down(Event=None):
    global y
    y=y+30
    button.place(x=x,y=y)

def move_up(Event=None):
    global y
    y = y - 30
    button.place(x=x, y=y)

def move_left(Event=None):
    global x
    x = x - 30
    button.place(x=x, y=y)

def move_right(Event=None):
    global x
    x = x + 30
    button.place(x=x, y=y)


win.bind("<Down>",move_down)
win.bind("<Up>",move_up)
win.bind("<Left>",move_left)
win.bind("<Right>",move_right)


while True:


    win.update()
