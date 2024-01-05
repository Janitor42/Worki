import tkinter as tk

#простой print в консоль
def say_hello():
    print('Hello')

#создание нового label при вызова фун-ции
def add_label():
    label=tk.Label(win,text='New')
    label.pack()

def count():
    global count_use
    count_use+=1
    bt_count['text']=f'Счетчик: {count_use}'

count_use=0

win = tk.Tk()

win.title('firs')

win.geometry('500x500')
win.config(background='black')

#создание переменной bt1 - вызов класса Button(прописываем текст для кнопки,
# в параметр command - ложем фун-цию которая будет запускаться при нажатии
bt1=tk.Button(win,text='Hello',
              command=say_hello)
#расположение на экране
bt1.pack()



bt2=tk.Button(win,text='Add',
              command=add_label)
bt2.pack()



bt_count=tk.Button(win,text=f'Счетчик: {count_use}',
                   command=count,
                   activebackground='red',#цвет кнопки в момент ее нажатия
                   state=tk.DISABLED)#делает кнопку неактивной
bt_count.pack()



win.mainloop()