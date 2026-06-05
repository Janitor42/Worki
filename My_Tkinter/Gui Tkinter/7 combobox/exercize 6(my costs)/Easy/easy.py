import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.geometry('1000x500')
win.config(background='black')
money = tk.IntVar()
money.set(10000)
text_money=tk.StringVar()
text_money.set(f'Потратьте {money.get()}')

row=0

def work_inp():
    create_new_label()
    del_inp()


def del_inp():
    inp.delete(0,tk.END)



def create_new_label():
    global row
    sale=inp.get()
    if int(sale)>int(money.get()):
        return
    new_label=tk.Label(win,text=sale,font=('Arial',20),anchor='w')
    new_label.grid(row=row,column=4,stick='we',padx=100)
    money.set(money.get() - int(sale))
    text_money.set(f'У вас осталось {money.get()}')
    row+=1




label_text = ttk.Label(win, font=('arial', 20),textvariable=text_money)
label_text.grid()

inp=tk.Entry(win,font=('Arial',20))
inp.grid()


button= tk.Button(win, text='Go', font=('arial', 20),
                    command=work_inp)

button.place(x=100,y=400)

win.mainloop()
