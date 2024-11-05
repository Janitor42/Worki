from tkinter import *

root = Tk()
root.title("METANIT.COM")
root.geometry("400x400")

red = "red"
blue = "blue"
green = "green"
selected_color = StringVar(value=red)
selected_color_roof = StringVar(value=red)

canvas = Canvas(bg="white", width=250, height=150)
canvas.place(x=100, y=200)

canvas.create_rectangle((10, 80, 130, 130), fill=selected_color.get(), outline="black", tags="house")
canvas.create_polygon((10, 80), (70, 30), (130, 80), fill=selected_color.get(), outline="black", tags="roof")


def select():
    canvas.itemconfig("house", fill=selected_color.get())
    canvas.itemconfigure("roof", fill=selected_color_roof.get())


(Radiobutton(text=red, value=red, variable=selected_color, command=select, font=('Arial', 20)).
 grid(row=1, column=0,sticky='w'))
(Radiobutton(text=blue, value=blue, variable=selected_color, command=select, font=('Arial', 20)).
 grid(row=2, column=0,sticky='w'))
(Radiobutton(text=green, value=green, variable=selected_color, command=select, font=('Arial', 20)).
 grid(row=3, column=0,sticky='w'))

(Radiobutton(text=red, value=red, variable=selected_color_roof, command=select, font=('Arial', 20)).
 grid(row=1, column=1,sticky='w'))
(Radiobutton(text=blue, value=blue, variable=selected_color_roof, command=select, font=('Arial', 20)).
 grid(row=2, column=1,sticky='w'))
(Radiobutton(text=green, value=green, variable=selected_color_roof, command=select, font=('Arial', 20)).
 grid(row=3, column=1,sticky='w'))
root.mainloop()
