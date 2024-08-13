import tkinter as tk
from tkinter import ttk #доступ к combobox

win = tk.Tk()

win.geometry('500x500')
win.config(background='black')


def change_text():
    text1.set('вы выбрали '+box1.get())

text1=tk.StringVar()
text1.set('не выбрано ничего')

text2=tk.StringVar()



label1=ttk.Label(win,textvariable=text1,font=('arial',20))#нужен что бы видеть что выбрано в box на экране
label1.pack()





text_box1=['easy','medium','hard']#текст для бокса

box1=ttk.Combobox(win,values=text_box1,font=('Arial',20),#собстрвенно создание box
                  width=10,
                  state='readonly',
                  textvariable=text2
                  )#state- что можно делать с элементами
#(readonly , normal, disabled
box1.current(1)#выбирает что будет стоять в box по умолчанию
box1.pack(pady=100)

button1=tk.Button(win,text='Go',font=('arial',20),command=change_text)#кнопка привязана следить что в боксе функ-ей
#и менять label
button1.pack(pady=10)


label=ttk.Label(win,textvariable=text2,font=('arial',20))#привязка бокса сразу к label минуя кнопку и ее фун-цию
label.pack()



win.mainloop()
