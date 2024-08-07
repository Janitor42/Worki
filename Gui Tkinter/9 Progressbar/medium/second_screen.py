import tkinter as tk
import random
from tkinter import ttk

all_el = []
screen = None

progress = None



def start_p():
    progress.start(100)



def stop_p():
    progress.stop()


def create_page_two(screen):
    global progress
    p_value = tk.IntVar(value=0)
    tk.Label(screen, text='Процесс установки ', background='white').pack(pady=200)
    tk.Label(screen, textvariable=p_value , background='white').pack(pady=0)

    progress = ttk.Progressbar(screen, orient='horizontal', length=400,variable=p_value,
                               maximum=10,mode='determinate'
                               )
    progress.pack()

    start = tk.Button(screen, text='Начать', border=2, command=start_p)
    start.pack(side='right', padx=50, ipadx=20)

    stop = tk.Button(screen, text='Остановить', border=2, command=stop_p)
    stop.pack(side='left', padx=50, ipadx=20)

