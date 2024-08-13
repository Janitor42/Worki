import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.geometry('300x500')
win.config(background='white')
#n, ne, e, se, s, sw, w, nw

#frame - область в которой будет все что она содержит и ее позиционирование на экране
#borderwidth: толщина границы фрейма, по умолчанию равно 0
# relief: определяет тип границы, может принимать значения sunken, raised, groove, ridge (как будет выглядеть )
# cursor: устанавливает курсор при наведении на фрейм (смена того как выглядит мышь) к примеру 'hand2'
# height: высота фрейма
# width: ширина фрейма


frame=tk.Frame(win,relief='raised',pady=10,borderwidth=3,cursor='hand2',)
label1=tk.Label(frame,text='Hello',background='pink')
label2=tk.Label(frame,text='you!',background='pink')
button1=tk.Button(frame,text='Helo and you',background='yellow')


label1.grid(padx=(0,100),pady=(0,100))
button1.grid()
label2.grid(padx=(100,0),pady=(100,0))
frame.grid(pady=100,padx=[65,0])
frame.config(background='pink')



win.mainloop()
