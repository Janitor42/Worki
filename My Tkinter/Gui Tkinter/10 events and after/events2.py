import tkinter as tk

win = tk.Tk()
size=20
win.geometry('500x500')
win.config(background='black')

def big(event):
    button.config(height=5,width=10,background='red')


def small(event):
    button.config(height=2,width=5,background='yellow')



button=tk.Button(win,text='go',font=size,height=2,width=5,background='yellow')
button.place(x=200,y=200)


button.bind("<Enter>",big)
button.bind('<Leave>',small)

win.mainloop()
# https://metanit.com/python/tkinter/2.20.php