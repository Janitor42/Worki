import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.geometry('500x500')
win.config(background='white')
#n, ne, e, se, s, sw, w, nw


def send_message():
    text1.delete(0,tk.END)
    text2.delete(0,tk.END)
    text3.delete(1.0,tk.END)

frame=tk.Frame(win,background='gainsboro',borderwidth=3,cursor='hand2')
label1=tk.Label(frame,text='Тема: ',background='gainsboro',font=('Arial',15))
label2=tk.Label(frame,text='Автор: ',background='gainsboro',font=('Arial',15))
label3=tk.Label(frame,text='Отзыв: ',background='gainsboro',font=('Arial',15))

text1=tk.Entry(frame,font=('Arial',20,))
text2=tk.Entry(frame,font=('Arial',20))
text3=tk.Text(frame,font=('Arial',20),width=20,height=10)

button1=tk.Button(frame,text='Send',background='chartreuse3'
                  ,font=('Arial',10,'bold'),command=send_message)

label1.grid(padx=(0,30),pady=(10,0),row=0,column=0)
text1.grid(row=0,column=1,pady=(10,10),sticky='w')

label2.grid(padx=(0,30),pady=(10,0))
text2.grid(row=1,column=1,pady=(10,10),sticky='w')

label3.grid(padx=(0,30),pady=(10,0),sticky='n')
text3.grid(row=2,column=1,pady=10)

button1.place(x=440,y=450)

frame.pack(fill=tk.BOTH,expand=True)






win.mainloop()

