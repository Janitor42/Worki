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
                 padx=20,pady=40,#отступ х отступ у
                 width=10,height=1,#ширина и высота в знаках
                 anchor='sw',#ценровка текста в label (север юг запад восток)
                 relief=tk.RAISED,#отображение границ label
                 bd=10,#ширина границы label
                 justify=tk.CENTER) #Прижатие теста к стороне в 2 button и более строчки
#расположение на экране
label_1.pack()



#отображение окна
win.mainloop()