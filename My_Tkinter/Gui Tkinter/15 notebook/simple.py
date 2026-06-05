import tkinter as tk
from tkinter import ttk
from tkinter import ttk

win = tk.Tk()

win.geometry('300x500')
win.config(background='white')

notebook= ttk.Notebook()
notebook.place(x=50,y=200)
frame=ttk.Frame(notebook)
notebook.add(frame,text='ooo')






# frame=tk.Frame(win,relief='raised',pady=10,borderwidth=3,cursor='hand2',)
# label1=tk.Label(frame,text='Hello',background='pink')
# label2=tk.Label(frame,text='you!',background='pink')
# button1=tk.Button(frame,text='Helo and you',background='yellow')
#
#
# label1.grid(padx=(0,100),pady=(0,100))
# button1.grid()
# label2.grid(padx=(100,0),pady=(100,0))
# frame.grid(pady=100,padx=[65,0])
# frame.config(background='pink')



win.mainloop()
