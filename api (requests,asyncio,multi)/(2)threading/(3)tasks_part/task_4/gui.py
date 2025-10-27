import tkinter as tk
import search
import queue


class Gui:

    def __init__(self):
        self.factory = None
        self.win = tk.Tk()
        self.win.geometry('500x800')

        tk.Label(self.win, text='Количество пользователей: ', font=('Arial', 20)).place(x=60, y=100)
        tk.Label(self.win, text='Возраст: ', font=('Arial', 20)).place(x=180, y=250)
        tk.Label(self.win, text='от: ', font=('Arial', 20)).place(x=60, y=300)
        tk.Label(self.win, text='до: ', font=('Arial', 20)).place(x=260, y=300)

        self.quantity = tk.Entry(self.win, font=('Arial', 20), width=20)
        self.quantity.place(x=80, y=150)

        self.age_min = tk.Entry(self.win, font=('Arial', 20), width=10)
        self.age_min.place(x=100, y=300)
        self.age_max = tk.Entry(self.win, font=('Arial', 20), width=10)
        self.age_max.place(x=300, y=300)

        self.bt_go = tk.Button(self.win, text='Find', font=('Arial', 20), bg='green', command=self.start)
        self.bt_go.place(x=60, y=600)

        self.all_p = 0
        self.found_p = 0
        self.all_people = tk.Label(self.win, text='Проверено 0', font=('Arial', 15))
        self.all_people.place(x=300, y=650)
        self.found_people = tk.Label(self.win, text='Найдено 0', font=('Arial', 15))
        self.found_people.place(x=320, y=680)

        self.win.mainloop()

    def start(self):
        search.factory.new_thread(obj=self)

        def after():
            while not search.factory.q.empty():
                event, data = search.factory.q.get()
                if event == 'all_true':
                    self.all_p += 1
                    self.all_people['text'] = f'Проверено {self.all_p}'
                elif event == 'user':
                    self.found_p += 1
                    self.found_people['text'] = f'Найден  {self.found_p}'

            self.win.after(ms=30, func=after)

        after()


