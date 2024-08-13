import tkinter as tk
from tkinter import ttk
import help
import random
win = tk.Tk()

win.geometry('500x500')
win.config(background='white')

progress = None
p_value = 0.0
p_variable = tk.DoubleVar()


def start_p():
    progress.start(random.randint(2,15))


def stop_p():
    progress.stop()



def text_install():
    global progress
    tk.Label(win, text='Процесс установки ', background='white').pack(pady=200)

    progress = ttk.Progressbar(win, orient='horizontal', length=400,
                               )
    progress.pack()

    start = tk.Button(win, text='Начать', border=2, command=start_p)
    start.pack(side='right',padx=50,ipadx=20)

    stop = tk.Button(win, text='Остановить', border=2, command=stop_p)
    stop.pack(side='left',padx=50,ipadx=20)


def start_install():
    help.label_hello.destroy()
    help.label_hello2.destroy()
    button_start.destroy()
    text_install()


help.create_hello(win)

button_start = tk.Button(win, text='Начать установку', border=2, command=start_install)
button_start.pack(padx=(200, 0), pady=(100, 0))

win.mainloop()

# label_hello=tk.Label(win,text='Здравствуйте',
#                      font=('Helvetica',20),background='white',
#                      )
# label_hello2=tk.Label(win,text='Давайте приступим к установке',
#                      font=('Helvetica',18),background='white',
#                      )
# button_start=tk.Button(win,text='Начать установку',border=2)
#
#
# label_hello.pack(pady=(200,0))
# label_hello2.pack()
# button_start.pack(padx=(200,0),pady=(100,0))
