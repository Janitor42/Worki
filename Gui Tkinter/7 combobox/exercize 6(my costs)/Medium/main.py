import tkinter as tk
from tkinter import ttk
import second
win = tk.Tk()

win.geometry('400x500+400+300')
win.config(background='black')

def choice_list():
    second.create_win(box.get())


text_box=['myself','my family','charity']
box=ttk.Combobox(win,values=text_box,font=('Arial',20),
                  state='readonly',
                  )
box.grid(pady=150,padx=40)


button = tk.Button(win, text='Go', font=('arial', 20),
                   command=choice_list)

button.place(x=150, y=400)

win.mainloop()
