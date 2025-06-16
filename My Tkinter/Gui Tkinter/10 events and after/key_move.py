import random
import tkinter as tk

win = tk.Tk()
size=20
win.geometry('500x500')
win.config(background='black')

x=30
y=30

dont_move=False

label3=None


count=tk.IntVar()
count.set(0)


def rd_place():
    return random.randrange(30,480,30)


def new_dot():
    global dot,dont_move,x_dot,y_dot,count
    count.set(int(count.get())+1)
    x_dot=rd_place()
    y_dot=rd_place()
    dot.place(x=x_dot,y=y_dot)
    dot.place(x=x_dot,y=y_dot)
    dont_move=False



x_dot=rd_place()
y_dot=rd_place()



def move_down(Event=None):
    global y
    if not dont_move:
        y=y+30
        button.place(x=x,y=y)
    fin()
def move_up(Event=None):
    global y
    if not dont_move:
        y = y - 30
        button.place(x=x, y=y)
    fin()
def move_left(Event):
    global x
    if not dont_move:
        x = x - 30
        button.place(x=x, y=y)
    fin()
def move_right(Event=None):
    global x
    if not dont_move:
        x = x + 30
        button.place(x=x, y=y)

    fin()

    # button.after(100,move_up)

def fin():
    global dont_move,label3
    print(button.winfo_rootx())
    if x==x_dot and y==y_dot:
        label3 = tk.Label(win, textvariable=f'{count}', font=('Arial',15), background='red',)
        label3.place(x=450, y=50)
        dont_move=True
        new_dot()

        # dot.after(1000,new_dot)



dot=tk.Label(win,text='     ',font=size,background='red')
dot.place(x=x_dot,y=y_dot)


button=tk.Button(win,text='go',font=size)
button.place(x=30,y=30)



win.bind("<Down>",move_down)
win.bind("<Up>",move_up)
win.bind("<Left>",move_left)
win.bind("<Right>",move_right)

win.mainloop()


























