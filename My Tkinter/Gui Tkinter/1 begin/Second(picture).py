import tkinter as tk


win = tk.Tk()

win.title('firs')

win.geometry('500x500')
win.config(background='black')

#вызов класса Label который показывает на окне
label_1=tk.Label(win,text='''Hello''',
                 background='white',#задник
                 foreground='green',#цвет текста
                 font=('Arial',15,'bold'),#параметры текста
                 width=20,height=4,#ширина и высота в знаках
                 anchor='sw',#ценровка текста в label (север юг запад восток)
                 #центровка происходит только тогда когда заданы width и или height
                 relief=tk.RAISED,#отображение границ label
                 bd=10,#ширина границы relief
                 ) #Прижатие теста к стороне работает в 2 button и более строчки

#расположение на экране(отрисовка)
label_1.place(x=100,y=100)



#отображение окна
win.mainloop()