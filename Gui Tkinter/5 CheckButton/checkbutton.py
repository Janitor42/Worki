import tkinter as tk

win = tk.Tk()


def select_all():
    for i in [meat, fish, bread]:
        i.select()


def deselect_all():
    for i in [meat, fish, bread]:
        i.deselect()


def show():
    print('fish', one.get(), 'meat', two.get())


win.geometry('500x500')
win.config(background='black')


#tk.StringVar и tk.IntVar() обьявление внутренних переменных в классе тк которые могут выступать в качесте
#значений флажка
#обычные переменные использовать нельзя. они не имеют get и set при обращении к ним будет ошибка

one = tk.StringVar()
one.set('No')


two = tk.IntVar()
two.set(0)

meat = tk.Checkbutton(win, text='Do you eat meat?',
                      font=('Arial', 15),
                      width=15,
                      anchor='w',
                      variable=two,# определяем переменную к этому флажку
                      offvalue=0,#значение когда галка не стоит
                      onvalue=1#значение когда галка стоит
                      )  # создание класса Checkbutton и
# сохранение его экземпляра в переменной meat

fish = tk.Checkbutton(win, text='Do you eat fish?', font=('Arial', 15),
                      width=15,
                      anchor='w',
                      variable=one,
                      offvalue='No',
                      onvalue='Yes')

bread = tk.Checkbutton(win, text='Do you eat bread?',
                       font=('Arial', 15),
                       width=15,
                       anchor='w',
                       )

bread2 = tk.Checkbutton(win, text='Do you eat bread?',
                        font=('Arial', 15),
                        width=15,
                        anchor='w',
                        indicatoron=0)  # превращает фраг в кнопку которую можно нажимать и отжимать

# cоздание кнопок смысл которых включение всех галок select и выключение deselect
tk.Button(win, text='select_all', command=select_all).grid()
tk.Button(win, text='deselect_all', command=deselect_all).grid()

tk.Button(win, text='show', command=show).grid()

meat.grid(padx=150, pady=[150, 0])
fish.grid()
bread.grid()
bread2.grid()

# отображение окна
win.mainloop()
# ,width=30,height=10


# ctrl alt l преображает текст
