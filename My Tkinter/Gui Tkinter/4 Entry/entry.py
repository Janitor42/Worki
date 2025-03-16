import tkinter as tk

win = tk.Tk()

win.geometry('500x500')
win.config(background='black')


def get_entry():  # создание фун-ции для кнопки
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty Entry')


def del_entry():
    name.delete(0, tk.END)
    # в параметрах delete 1 обязательный аргумент , если указать число 3 то из строки удалиться символ с этим индексом
    # сейчас там написана запись как удалить из нее все tk.END - константа котороая ссылается и распознается как - конец строки


def insert_entry():
    name.insert(0, 'hello')
    # вызывает метод insert у name и по индексу вставляет то что нам необходимо
    # при многократном исп-нии будет повторно вставлять эти же данные на это же место


tk.Label(win, text='Имя').grid(row=0, column=0, stick='we')  # создание lable с текстом (на против ввода)

name = tk.Entry(win)  # создание виджета для ввода, сохранение его в переменную
name.grid(row=0, column=1)  # отрисовка\отображение на экране

tk.Button(win, text='get', command=get_entry).grid(row=1, column=1,
                                                   stick='we')  # создание кнопки - фун-ция которой отлавливать
# что находится в name проходить условия и печатать в консоль

tk.Button(win, text='del', command=del_entry).grid(row=1, column=3, stick='we',
                                                   ipadx=40)  # создание кнопки - фун-ция которой
# удалять у name ее значение

tk.Button(win, text='insert', command=insert_entry).grid(row=1, column=4, stick='we',
                                                         ipadx=40)  # создание кнопки - фун-ция которой
# вставлять какие то данные в существующую позицию




win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()
