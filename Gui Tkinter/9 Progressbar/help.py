import tkinter as tk
from tkinter import ttk



label_hello=None
label_hello2=None
button_start=None

def create_hello(win):


    global label_hello,label_hello2,button_start
    label_hello=tk.Label(win,text='Здравствуйте',
                         font=('Helvetica',20),background='white',
                         )
    label_hello2=tk.Label(win,text='Нажмите "Начать установку" ',
                         font=('Helvetica',18),background='white',
                         )



    label_hello.pack(pady=(200,0))
    label_hello2.pack()


