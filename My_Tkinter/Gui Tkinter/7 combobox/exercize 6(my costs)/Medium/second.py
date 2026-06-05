import tkinter as tk
from tkinter import ttk

win = None

'myself', 'my family', 'charity'
a=0
name = None
sale = None

text = None
value = None

row = None

myself = []
my_family = []
charity = []


def create_win(choice_box):
    global win, name, sale, text, value, row
    if win != None:
        win.destroy()
    win = tk.Toplevel()
    win.geometry('610x500+800+300')
    win.config(background='black')
    win.title('spend')
    tk.Label(win, text=f'Ваши траты {choice_box}', font=('Arial', 20)).grid(row=0, columnspan=2, stick='we',
                                                                            padx=[10, 0])
    tk.Label(win, text='Наименование', font=('Arial', 20), width=20).grid(row=1, column=0, padx=[10, 0], stick='we')
    tk.Label(win, text='Стоимость', font=('Arial', 20), width=16).grid(row=1, column=1, stick='we')

    text = tk.Entry(win, font=('Arial', 20))
    text.place(x=10, y=400)
    value = tk.Entry(win, font=('Arial', 20))
    value.place(x=300, y=400)
    row = 2
    if choice_box == 'myself':
        create_myself_data()
    if choice_box == 'my family':
        create_my_family_data()
    if choice_box == 'charity':
        create_charity_data()


def create_myself_data():
    global row
    tk.Button(win, text='write', font=('Arial', 20), foreground='red', command=add_write_myself).place(x=250, y=450)
    for i in range(0, len(myself), 2):
        tk.Label(win, text=myself[i], font=('Arial', 20), width=20, anchor='e').grid(row=row, column=0, padx=[10, 0],
                                                                                     stick='we')
        tk.Label(win, text=myself[i + 1], font=('Arial', 20), width=16, anchor='e').grid(row=row, column=1, stick='we')
        row += 1


def create_my_family_data():
    global row
    tk.Button(win, text='write', font=('Arial', 20), foreground='red', command=add_write_my_family).place(x=250, y=450)
    for i in range(0, len(my_family), 2):
        tk.Label(win, text=my_family[i], font=('Arial', 20), width=20, anchor='e').grid(row=row, column=0, padx=[10, 0],
                                                                                        stick='we')
        tk.Label(win, text=my_family[i + 1], font=('Arial', 20), width=16, anchor='e').grid(row=row, column=1,
                                                                                            stick='we')
        row += 1


def create_charity_data():
    global row
    tk.Button(win, text='write', font=('Arial', 20), foreground='red', command=add_write_charity).place(x=250, y=450)
    for i in range(0, len(charity), 2):
        tk.Label(win, text=charity[i], font=('Arial', 20), width=20, anchor='e').grid(row=row, column=0, padx=[10, 0],
                                                                                      stick='we')
        tk.Label(win, text=charity[i + 1], font=('Arial', 20), width=16, anchor='e').grid(row=row, column=1, stick='we')
        row += 1


def add_write_myself():
    global row
    row += 1
    a = tk.Label(win, text=text.get(), font=('Arial', 20), width=20, anchor='e')
    myself.append(text.get())
    a.grid(row=row, column=0, padx=[10, 0], stick='we')

    b = tk.Label(win, text=value.get(), font=('Arial', 20), width=16, anchor='e')
    myself.append(value.get())
    b.grid(row=row, column=1, stick='we')


def add_write_my_family():
    global row
    row += 1
    a = tk.Label(win, text=text.get(), font=('Arial', 20), width=20, anchor='e')
    my_family.append(text.get())
    a.grid(row=row, column=0, padx=[10, 0], stick='we')

    b = tk.Label(win, text=value.get(), font=('Arial', 20), width=16, anchor='e')
    my_family.append(value.get())
    b.grid(row=row, column=1, stick='we')


def add_write_charity():
    global row
    row += 1
    a = tk.Label(win, text=text.get(), font=('Arial', 20), width=20, anchor='e')
    charity.append(text.get())
    a.grid(row=row, column=0, padx=[10, 0], stick='we')

    b = tk.Label(win, text=value.get(), font=('Arial', 20), width=16, anchor='e')
    charity.append(value.get())
    b.grid(row=row, column=1, stick='we')
