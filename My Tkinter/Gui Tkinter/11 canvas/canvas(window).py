import tkinter as tk

win = tk.Tk()
x = '500'
y = '500'
win.geometry(x + 'x' + y)
win.config(background='black')

# Добавление виджетов
# Одной из замечательных особенностей Canvas является то,
# что он позволяет добавлять другие виджеты и таким образом создавать сложные по композиции интерфейсы.
# Для этого применяется метод create_window().

can = tk.Canvas(bg='white', width=int(x) - 50, height=int(y) - 50)
can.pack(expand=True)


# Параметры
# _x и _y или __coords: координаты точки размещения виджета. По умолчанию представляет центр виджета
# _anchor: устанавливает положение виджета относительно координат
# height: высота виджета
# width: ширина виджета
# state: состояние виджета
# tags: набор тегов, связанных с виджетом
# В качестве результата этот метод возвращает идентификатор добавленного метода.




bt=tk.Button(text='So so so')
can.create_window(10,100,anchor=tk.NW,window=bt,height=50,width=100)




win.mainloop()