import tkinter as tk

win = tk.Tk()

win.geometry('500x500')
win.config(background='black')


bt1=tk.Button(win,text='Hello')
bt1_5=tk.Button(win,text='Hello')
bt2=tk.Button(win,text='Hello you')
bt3=tk.Button(win,text='Hello')
bt4=tk.Button(win,text='Hello!')

#grid - метон позволяющий распологать виджеты- параметры row(ряд)column-(колонка)
bt1.grid(row=0,column=0,stick='ns',rowspan=2)
bt1_5.grid(row=0,column=1,stick='we')
bt2.grid(row=1,column=1,stick='we')
bt3.grid(row=3,column=0,columnspan=2,stick='we')
bt4.grid(row=0,column=2,rowspan=4,stick='ns')


win.grid_columnconfigure(0,minsize=25)#метод применяется к окну,указывается индекс колонки, задает минимальный размер
win.grid_columnconfigure(1,minsize=100)#метод применяется к окну,указывается индекс колонки, задает минимальный размер

win.mainloop()



