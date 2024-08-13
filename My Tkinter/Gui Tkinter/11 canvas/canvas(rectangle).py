import tkinter as tk

win = tk.Tk()
x='500'
y='500'
win.geometry(x+'x'+y)
win.config(background='black')


# Для отрисовки прямоугольника применяется метод create_rectangle(),
# которому обязательно передаются координаты верхнего левого и правого нижнего угла:
# create_rectangle(__x0: float, __y0: float, __x1: float, __y1: float)

can=tk.Canvas(bg='white',width=int(x)-50,height=int(y)-50)
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

can.create_rectangle(50,150,300,100,fill='lime',width=3,outline='blue',activefill='pink',activeoutline='black')



win.mainloop()