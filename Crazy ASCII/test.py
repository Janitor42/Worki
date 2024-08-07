import tkinter as tk
import model


def cl_all():
    model.all_sym.clear()


def create_tk():
    win = tk.Tk()
    bt1 = tk.Button(win, text='Hello',
                    command=
                    cl_all)
    # расположение на экране
    bt1.pack()
    win.mainloop()


