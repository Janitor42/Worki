import tkinter as tk
import field
import object
import time
win = tk.Tk()
win.config(background='black')
win.geometry('600x600')

frame = tk.Frame(win, width=400, height=400)
frame.pack(anchor='center', pady=100)

field.create_field(frame=frame)

side_more = [1, 5, 1, ]
side_less = [4, 0, -1, ]


def move_down(Event=None):
    object.move(side=side_less, plus_row=+1, plus_column=0,index=0)
    object.remove_buttons()
    object.recording_key()


    object.create_button(how_many=1, frame=frame)


def move_up(Event=None):
    object.move(side=side_more, plus_row=-1, plus_column=0,index=0)
    object.remove_buttons()
    object.recording_key()


    object.create_button(how_many=1, frame=frame)


def move_left(Event=None):
    object.move(side=side_more, plus_row=0, plus_column=-1,index=1)
    object.remove_buttons()
    object.recording_key()


    object.create_button(how_many=1, frame=frame)


def move_right(Event=None):
    object.move(side=side_less, plus_row=0, plus_column=1,index=1)
    object.remove_buttons()
    object.recording_key()


    object.create_button(how_many=1, frame=frame)




win.bind("<Down>", move_down)
win.bind("<Up>", move_up)
win.bind("<Left>", move_left)
win.bind("<Right>", move_right)

win.mainloop()
