import tkinter as tk
from tkinter import ttk #доступ к combobox

win = tk.Tk()

win.geometry('500x500')
win.config(background='black')






text_box1=['easy','medium','hard']#текст для бокса

box1=ttk.Combobox(win,values=text_box1,font=('Arial',20),#собстрвенно создание box
                  width=10,
                  state='readonly',
                  )#state- что можно делать с элементами
#(readonly , normal, disabled
box1.current(1)#выбирает что будет стоять в box по умолчанию
box1.pack(pady=100)



def change():
    text_box1.append('aaa')
    box1.config(values=text_box1)



button1=tk.Button(win,text='Go',font=('arial',20),command=change)#кнопка привязана следить что в боксе функ-ей
#и менять label
button1.pack(pady=10)





win.mainloop()
