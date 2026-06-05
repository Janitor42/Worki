import tkinter as tk
import second
win = tk.Tk()

win.geometry('800x500+100+200')
win.config(background='black')
win.title('my cat')

def create_choice():
    second.create_win2()
    second.create_variables()
    second.create_radiobutton()

    state_cat = tk.Label(win, textvariable=second.main_text, font=('Arial', 20))
    state_cat.place(x=200, y=400)

def begin():
    hello.destroy()
    button.destroy()
    create_choice()

hello = tk.Label(win, text='Ухаживай за котиком!', font=('Arial', 20))
hello.pack(pady=100)

button = tk.Button(win, text='GO', command=begin, font=('Times', 40, 'bold'), background='yellow')
button.pack()

win.mainloop()
