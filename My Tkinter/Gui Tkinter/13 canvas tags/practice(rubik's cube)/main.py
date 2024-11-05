import tkinter as tk
import help
import random as rd

win = tk.Tk()
x = '500'
y = '500'
win.geometry(x + 'x' + y)
win.config(background='black')

can = tk.Canvas(bg='white', width=int(x), height=int(y) - 100)  # канвас
can.place(x=0, y=0)

field_x = []
help.create_field_x(field_x,can)
field_y = []
help.create_field_y(field_y,can)
field_z = []
help.create_field_z(field_z,can)

all_field=field_x+field_y+field_z


color_x=['red',"blue",'orange']
color_y=['pink',"purple",'gray']
color_z=['yellow','lime','green']





can.itemconfig('x',fill=rd.choice(color_x))
can.itemconfig('y',fill=rd.choice(color_y))
can.itemconfig('z',fill=rd.choice(color_z))

#todo сделать что бы цвета были случайные а при помощи тега все менялось на правильные места

tk.mainloop()
