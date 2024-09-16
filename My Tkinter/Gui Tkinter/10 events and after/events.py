import tkinter as tk

win = tk.Tk()
size=20
win.geometry('500x500')
win.config(background='black')

def change_text(Event=None):
    label['text']=entry.get()
    entry.delete(0,tk.END)



label=(tk.Label(win,text='Hello',font=size))
label.grid()


entry=(tk.Entry(win,font=size))
entry.grid()

button=tk.Button(win,text='go',font=size)
button.grid()


button.bind("<Button>",change_text)
win.bind('<Return>',change_text)


win.mainloop()
# https://metanit.com/python/tkinter/2.20.php