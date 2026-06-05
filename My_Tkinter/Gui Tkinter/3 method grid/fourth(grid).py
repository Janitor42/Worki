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
bt1.grid(row=0,column=0)
bt1_5.grid(row=0,column=1,stick='we')#растягиваем кнопку 1_5 по длинне кнопки Hello you путем stik от запада до востока
bt2.grid(row=1,column=1)
bt3.grid(row=3,column=0,columnspan=2,stick='we')#columnspan - обьединение колонок
bt4.grid(row=0,column=2,rowspan=4,stick='ns')#rowspan - обьединение рядов


win.mainloop()



