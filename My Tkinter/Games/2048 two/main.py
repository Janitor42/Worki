import tkinter as tk
import field
import object

win = tk.Tk()
win.config(background='black')
win.geometry('600x600')

frame = tk.Frame(win, width=400, height=400)
frame.pack(anchor='center', pady=100)

field.create_field(frame=frame)
object.create_button(how_many=2,frame=frame)






def move_down(Event=None):
    object.move_down()
    object.create_button(how_many=1,frame=frame)







#
#
# def move_up(Event=None):
#     pass

#
# def move_left(Event):
#     pass

#
#
# def move_right(Event=None):
#     pass

#
win.bind("<Down>", move_down)
# win.bind("<Up>", move_up)
# win.bind("<Left>", move_left)
# win.bind("<Right>", move_right)

win.mainloop()
