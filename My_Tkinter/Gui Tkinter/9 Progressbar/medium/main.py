import tkinter as tk

import firs_screen

win = tk.Tk()

win.geometry('500x500')
win.config(background='white')

firs_screen.create_page_one(win)


win.mainloop()
