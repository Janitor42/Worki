import tkinter as tk
import time

win = tk.Tk()
win.geometry('500x500')
win.config(background='black')
size = ('Arial', 20)

count = tk.StringVar()
count.set('0:0:00')

hou = 0
min = 0
sec = 0

come = False
come_int=0
start = False


def in_pos(event=None):
    global come
    come = True

def on_pos(event=None):
    global come
    come = False



def reset_time(event_None):
    global start, go,one_click
    count.set('0:0:00')
    start = False
    go_bt.place(x=100, y=400)

pause = False


def pause_time(event_None):
    global pause
    if start:
        pause = not pause

state=False
def go_time(event=None):
    global start, sec, min, hou, begin, after

    if start == False and come:
        after=0
        begin = 0
        hou = 0
        min = 0
        sec = 0
        start = True

    if pause:
        label.after(10, go_time)


    if start and not pause:
        after+=1
        sec = after - begin
        if sec >= 60:
            min += 1
            after = 0
        if min >= 60:
            hou += 1
            min = 0
            after = 0
        sec=round(sec,2)
        all_time = f'{hou}:{min}:{sec}'

        count.set(all_time)
        label.after(10, go_time)
        go_bt.place(x=-100,y=-100)


text = tk.Label(win, text='Stopwatch', font=size)
text.place(x=175, y=50)

go_bt = tk.Button(win, text='go', font=size, width=5,state='normal')
go_bt.place(x=100, y=400)

pause_bt = tk.Button(win, text='pause', font=size, width=5)
pause_bt.place(x=200, y=400)

reset_bt = tk.Button(win, text='reset', font=size)
reset_bt.place(x=300, y=400)

label = tk.Label(win, textvariable=count, font=('Times', 30, 'bold'), background='black', fg='white')
label.place(x=200, y=200)

go_bt.bind('<Enter>', in_pos)
go_bt.bind('<Leave>', on_pos)
go_bt.bind("<Button>", go_time)

pause_bt.bind('<Button>', pause_time)

reset_bt.bind('<Button>', reset_time)

win.mainloop()
# https://metanit.com/python/tkinter/2.20.php
