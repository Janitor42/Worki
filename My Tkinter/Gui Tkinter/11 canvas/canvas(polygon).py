import tkinter as tk

win = tk.Tk()
x = '500'
y = '500'
win.geometry(x + 'x' + y)
win.config(background='black')

# Для создания многоугольника применяется метод create_polygon().
# Он принимает в качестве обязательных параметров набор координатов точек:
# Для упрощения также можно передавать набор кортежей, где каждый кортеж представляет отдельную точку:
#
# points = (
#     (10, 30),
#     (200, 200),
#     (200, 30),


can = tk.Canvas(bg='white', width=int(x) - 50, height=int(y) - 50)
can.pack(expand=True)

# Параметры отрисовки
# Методы отрисовки имеют ряд параметров, которые позволяют настроить стилизацию фигур. Некоторые из этих параметров:
# fill: цвет заполнения фигуры
# width: ширина линий
# outline: для заполненных фигур цвет контура
# dash: устанавливает пунктирную линию
# stipple: устанавливает шаблон для заполнения фигуры (например, gray75, gray50, gray25, gray12)
# activefill: цвет заполнения фигуры при наведении курсора
# activewidth: ширина линий при наведении курсора
# activestipple: шаблон заполнения фигуры при наведении курсора

poli = (
    (10, 10),
    (30, 100),
    (100,200)
)

can.create_polygon(*poli, fill='lime', width=3, outline='blue', activefill='pink', activeoutline='black')



poli = (
    (200, 200),
    (150, 250),
    (200,300),
    (250,250)
)

can.create_polygon(*poli, fill='lime', width=3, outline='blue', activefill='pink', activeoutline='black')


win.mainloop()
