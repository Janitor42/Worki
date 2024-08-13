import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.geometry('300x300')
win.config(background='white')

#Виджет Progressbar предназначен для отображения хода выполнения какого-либо процесса. Основные параметры Progressbar:

# value: текущее значение виджета (тип float)
# maximum: максимальное значение (тип float)
# variable: определяет переменную IntVar/DoublerVar, которая хранит текущее значение виджета
# mode: определяет режим, принимает значения "determinate" (конечный) и "indeterminate" (бесконечный)
# orient: определяет ориентацию виджета, принимает значения "vertical" (вертикальый) и "horizontal" (горизонтальный)
# length: длина виджета

tk.Label(win,text='Loading...',background='white').place(x=125,y=130)

prog=ttk.Progressbar(win,orient='horizontal',length=100,value=15,maximum=100)
prog.place(x=100,y=150)

# start([interval]): запускает перемещение индикатора через определенные интервалы времени.
# Каждый раз, когда пройдет очередной интервал, индикатор смещается на одно деление вперед.
#По умолчанию интервал равен 50 миллисекунд

# step([delta]): увеличивает значение индикатора на значение из параметра delta (по умолчанию равен 1.0)
# stop(): останавливает перемещение индикатора



win.mainloop()
