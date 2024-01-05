import tkinter as tk

#создание окна(вызываем класс Тк
win = tk.Tk()

#Меняем имя окна
win.title('firs')

#Размеры окна
win.geometry('500x500')

#указываем минимальные размеры окна
win.minsize(100,100)
#указываем максимальные размеры окна
win.maxsize(500,500)

win.config(background='black')
#Возможность цеплять окно мышкой и делать шире\выше(True-можно менять, False - менять запрещено)
win.resizable(True,True)


#отображение окна
win.mainloop()