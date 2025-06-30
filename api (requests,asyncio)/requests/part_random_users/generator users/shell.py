import tkinter as tk
from tkinter import ttk

import search_factory
import user


class Shell:

    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry('500x900+1200+50')
        self.errors = []

        # Количество пользователей
        tk.Label(self.win, text='Количество пользователей: ', font=('Arial', 20)).place(x=60, y=100)

        self.quantity = tk.Entry(self.win, font=('Arial', 20), width=20)
        self.quantity.place(x=80, y=150)

        # Возраст
        tk.Label(self.win, text='Возраст: ', font=('Arial', 20)).place(x=180, y=250)
        tk.Label(self.win, text='от: ', font=('Arial', 20)).place(x=60, y=300)
        tk.Label(self.win, text='до: ', font=('Arial', 20)).place(x=260, y=300)

        self.age_min = tk.Entry(self.win, font=('Arial', 20), width=10)
        self.age_min.place(x=100, y=300)
        self.age_max = tk.Entry(self.win, font=('Arial', 20), width=10)
        self.age_max.place(x=300, y=300)

        # Пол
        tk.Label(self.win, text='Пол: ', font=('Arial', 20)).place(x=60, y=400)
        self.gender = ttk.Combobox(self.win, values=['мужчина', 'женщина', 'любой'],
                                   font=('Arial', 20), width=10, state='readonly')
        self.gender.set('любой')
        self.gender.place(x=150, y=400)

        # Статус
        # self.lb_find = tk.Label(self.win, text='Найдено:', font=('Arial', 16))
        # self.lb_checks = tk.Label(self.win, text='Проверено:', font=('Arial', 16))
        # self.lb_find.place(x=60, y=500)
        # self.lb_checks.place(x=250, y=500)

        # Кнопки
        self.bt_go = tk.Button(self.win, text='Generate', font=('Arial', 20), bg='green', command=self.start)
        self.bt_go.place(x=60, y=600)

        self.bt_clean = tk.Button(self.win, text='Clean', font=('Arial', 20), bg='orange', command=self.clean_fields)
        self.bt_clean.place(x=300, y=600)

        self.bt_show_users = tk.Button(self.win, text='Show users', font=('Arial', 20), bg='purple',
                                       command=self.open_top_levels)
        self.bt_show_users.place(x=60, y=700)

        self.win.mainloop()

    def error_text(self, x, y, text):
        error = tk.Label(self.win, text=text, font=('Arial', 10), background='red')
        error.place(x=x, y=y)
        self.errors.append(error)

    def start(self):
        self.clear_errors()
        self.check_quantity()
        self.check_age()
        if not self.errors:
            search_factory.create_users(self)
            user.create_documentation()

    def clear_errors(self):
        for i in self.errors:
            i.destroy()
        self.errors.clear()

    def check_quantity(self):
        line = self.quantity.get()
        line = line.strip()
        if not line.isdigit() or line == '' or not 500 >= int(line) >= 1:
            self.error_text(x=80, y=200, text='Ошибка только цифры от 1 до 500')

    def check_age(self):
        one = False
        two = False
        age_1 = self.age_min.get().strip()
        if age_1.isdigit() and age_1 != '' and 90 >= int(age_1) >= 20:
            one = int(self.age_min.get())
        else:
            self.error_text(x=80, y=350, text='Ошибка только цифры от 20 до 90')

        age_2 = self.age_max.get().strip()
        if age_2.isdigit() and age_2 != '' and 90 >= int(age_2) >= 20:
            two = int(self.age_max.get())
        else:
            self.error_text(x=80, y=350, text='Ошибка только цифры от 20 до 90')

        if one and two:
            if not two >= one:
                self.error_text(x=80, y=350, text='Ошибка: "до" должно быть больше или равно "от"')

    def clean_fields(self):
        self.quantity.delete(0, tk.END)
        self.age_min.delete(0, tk.END)
        self.age_max.delete(0, tk.END)
        self.gender.set('любой')
        self.clear_errors()
        self.close_top_levels()

    def close_top_levels(self):
        for i in user.all_top_levels:
            i.destroy()

    def open_top_levels(self):
        self.close_top_levels()
        user.create_documentation()
