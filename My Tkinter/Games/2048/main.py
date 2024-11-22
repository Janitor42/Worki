import tkinter as tk
import field
import object

win = tk.Tk()
win.config(background='black')
win.geometry('600x600')

frame = tk.Frame(win, width=400, height=400)
frame.pack(anchor='center', pady=100)

field.create_field(frame=frame)

object.create_object(how_many=1, frame=frame)


# for i in field.all_fields:
#     print(i.state)
# print('-----------------')


def move_down(Event=None):
    for i in object.all_objects:
        print(i.row, i.column)
        for count in range(3, 0, -1):
            print(i.row, i.column + count)
            for place in field.all_fields:
                if [i.row, i.column + count] == [place.row, place.column] and place.state == 'open':
                    i.row=i.row+count
                    i.button.grid(row=i.row, column=i.column)
                    break



def move_up(Event=None):
    pass
    for i in object.all_objects:
        new_place = field.new_place(row=i.row, column=i.column,
                                    direction_row=-1, direction_column=0)
        this_place = field.this_place(i.row, i.column)

        if new_place.state == 'open':
            i.row = new_place.row
            i.column = new_place.column
            i.button.grid(row=new_place.row, column=new_place.column)

            new_place.label.config(background='firebrick4')
            new_place.state = 'busy'

            this_place.label.config(background='green')
            this_place.state = 'open'


def move_left(Event):
    pass
    for i in object.all_objects:
        new_place = field.new_place(row=i.row, column=i.column,
                                    direction_row=0, direction_column=-1)
        this_place = field.this_place(i.row, i.column)
        if new_place.state == 'open':
            i.row = new_place.row
            i.column = new_place.column
            i.button.grid(row=new_place.row, column=new_place.column)

            new_place.label.config(background='firebrick4')
            new_place.state = 'busy'

            this_place.label.config(background='green')
            this_place.state = 'open'


def move_right(Event=None):
    pass
    for i in object.all_objects:
        new_place = field.new_place(row=i.row, column=i.column,
                                    direction_row=0, direction_column=1)
        this_place = field.this_place(i.row, i.column)
        if new_place.state == 'open':
            i.row = new_place.row
            i.column = new_place.column
            i.button.grid(row=new_place.row, column=new_place.column)

            new_place.label.config(background='firebrick4')
            new_place.state = 'busy'

            this_place.label.config(background='green')
            this_place.state = 'open'


win.bind("<Down>", move_down)
win.bind("<Up>", move_up)
win.bind("<Left>", move_left)
win.bind("<Right>", move_right)

win.mainloop()
