import tkinter as tk
from tkinter import ttk
import finance
import events

all_tk = None


def run_tk_gui():
    global all_tk
    all_tk = Screen_tk()
    all_tk.win.mainloop()


class Screen_tk:
    def __init__(self):
        # окно
        self.win = tk.Tk()
        self.win.geometry('300x500')
        self.win.minsize(300, 500)

        # количество уже уничтоженных блоков
        self.label_damage = tk.Label(self.win,
                                     text=f'Bricks damage \n{0}',
                                     font=('Arial', 14))
        self.label_damage.pack(side='right', anchor='se')

        # отображение денег
        self.label_money = tk.Label(self.win, text=f' $ \n{0}',
                                    font=('Arial', 14))
        self.label_money.pack(side='left', anchor='se')

        # тестовая кнопка на покупку шара
        self.bt = tk.Button(self.win, text='O', font=('Arial', 15, 'bold'), foreground='yellow', background='#b4b9d4',
                            command=events.giv_money)
        self.bt.pack(side='right', anchor='nw')



