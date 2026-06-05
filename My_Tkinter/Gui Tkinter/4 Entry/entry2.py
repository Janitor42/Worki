import tkinter as tk

win = tk.Tk()

win.geometry('500x500')
win.config(background='black')


def on_key(event=None):
    print(entry.get())

a=tk.StringVar()
a.set('Hello World')

tk.Label(win, text='Имя',font=('arial',20)).grid(row=0, column=0, stick='we')

entry = tk.Entry(win,font=('arial',20),textvariable=a)
entry.grid(row=0, column=1)

entry.bind('<KeyRelease>', on_key)


win.mainloop()
