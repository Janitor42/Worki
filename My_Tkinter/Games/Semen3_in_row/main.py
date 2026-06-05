import tkinter as tk
from field import Field
win = tk.Tk()
win.title("First")
win.geometry("770x900+500+100")
win.minsize(200, 200)
win.maxsize(1000, 1000)
win.config(background="green")

Field.make_field(win=win)
Field.find_three()
win.mainloop()