import tkinter as tk

win = tk.Tk()
x = '500'
y = '500'
win.geometry(x + 'x' + y)
win.config(background='black')

# Для отрисовки дуги применяется метод create_arc(), который принимает набор точек:
#


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


# a=can.create_arc((200,200,400,400), fill='lime', width=3, outline='blue', activefill='pink', activeoutline='black')
# can.create_arc((400,400,200,200), fill='orange', width=3,stat='hidden',
#                extent=270,outline='blue', activefill='pink', activeoutline='black')

# can.create_arc((400,400,200,200), fill='black', width=3,
#                extent=20,outline='blue', activefill='pink', activeoutline='black')
#
# can.create_arc((400,200,200,400), fill='red', width=3,
#                extent=45,outline='blue', activefill='pink', activeoutline='black')
#



win.mainloop()
# import tkinter as tk
#
# root = tk.Tk()
# canvas = tk.Canvas(root, width=400, height=400)
# canvas.pack()
#
# # Рисуем дугу по часовой стрелке
# canvas.create_arc(50, 50, 350, 350, start=0, extent=170, outline="blue", width=3)
#
# # Рисуем дугу против часовой стрелки
# canvas.create_arc(50, 50, 350, 350, start=0, extent=-90, outline="red", width=3)
#
# root.mainloop()