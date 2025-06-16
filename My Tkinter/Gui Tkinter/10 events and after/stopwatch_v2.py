import tkinter as tk
import time

win = tk.Tk()
win.geometry('500x500')
win.config(background='black')
size = ('Arial', 20)

count = tk.DoubleVar(value=0)
state = 'pause'


def go_time(event):
    global state
    state = 'play'


def pause_time(event):
    global state
    state = 'pause'


def reset_time(event):
    global state
    state = 'reset'


text = tk.Label(win, text='Stopwatch', font=size)
text.place(x=175, y=50)

go = tk.Button(win, text='go', font=size, width=5, state='normal')
go.place(x=100, y=400)

pause = tk.Button(win, text='pause', font=size, width=5)
pause.place(x=200, y=400)

reset = tk.Button(win, text='reset', font=size)
reset.place(x=300, y=400)

label = tk.Label(win, textvariable=count, font=('Times', 30, 'bold'), background='black', fg='white')
label.place(x=200, y=200)

go.bind("<Button>", go_time)
pause.bind('<Button>', pause_time)
reset.bind('<Button>', reset_time)
time_start = 0

all_time = 0
time_a = 0

while True:
    if state in ['pause']:
        time_start = time.time()
        time_a = all_time

    elif state in 'play':
        time_b = round(time.time() - time_start, 2)
        all_time = round(time_a + time_b, 2)
        count.set(all_time)

    elif state in 'reset':
        all_time = 0
        time_a = 0
        time_start = time.time()
        count.set(0)

    win.update()










































