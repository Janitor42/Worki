import tkinter as tk
from tkinter import ttk

win = None

'myself', 'my family', 'charity'

name = None
sale = None

text = None
value = None


row = None

myself = []
def work_second():

    create_win()


def create_win():
    global win, name, sale, text, value,row
    if win !=None:
        win.destroy()
    win = tk.Toplevel()
    win.geometry('610x500+800+300')
    win.config(background='black')
    win.title('spend')
    tk.Label(win, text='Ваши траты', font=('Arial', 20)).grid(row=0, columnspan=2, stick='we', padx=[10, 0])
    tk.Label(win, text='Наименование', font=('Arial', 20), width=20).grid(row=1, column=0, padx=[10, 0], stick='we')
    tk.Label(win, text='Стоимость', font=('Arial', 20), width=16).grid(row=1, column=1, stick='we')

    text = tk.Entry(win, font=('Arial', 20))
    text.place(x=10, y=400)
    value = tk.Entry(win, font=('Arial', 20))
    value.place(x=300, y=400)
    tk.Button(win, text='write', font=('Arial', 20), foreground='red', command=add_write).place(x=250, y=450)
    row=2

    for i in range(0,len(myself),2):
            tk.Label(win, text=myself[i], font=('Arial', 20),width=20,anchor='e').grid(row=row,column=0,padx=[10,0],stick='we')
            tk.Label(win, text=myself[i+1], font=('Arial', 20), width=16, anchor='e').grid(row=row, column=1, stick='we')
            row+=1



def add_write():
    global row
    row+=1

    a=tk.Label(win, text=text.get(), font=('Arial', 20),width=20,anchor='e')
    myself.append(text.get())
    a.grid(row=row,column=0,padx=[10,0],stick='we')

    b=tk.Label(win, text=value.get(), font=('Arial', 20), width=16,anchor='e')
    myself.append(value.get())
    b.grid(row=row, column=1, stick='we')

