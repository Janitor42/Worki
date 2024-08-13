import tkinter as tk
import model
import controller

all_gui = None
a=0

def create_tk():

    global lab_how_much,a
    dici = {}
    win = tk.Tk()
    win.geometry('300x800+890+70')
    a=tk.StringVar()
    a.set(f'Now we see {len(model.all_sym)}')
    lab_how_much = tk.Label(win, textvariable=a)
    lab_how_much.pack()


    bt_del = tk.Button(win, text='Del', command=controller.clear_all_letters)
    bt_del.pack()

    bt_add1 = tk.Button(win, text='Add 1', command=controller.add_one_letter)
    bt_add1.pack()

    bt_add5 = tk.Button(win, text='Add 5', command=controller.add_five_letter)
    bt_add5.pack()

    bt_add25 = tk.Button(win, text='Add 25', command=controller.add_twenty_five_letter)
    bt_add25.pack()
    win.mainloop()
