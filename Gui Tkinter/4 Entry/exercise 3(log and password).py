import tkinter as tk

win = tk.Tk()

win.geometry('500x500')
win.config(background='black')


def get_text():
    if len(name.get()) + len(password.get())>0:
        if name.get()==password.get():
            answer['background']='green'
            answer['text']= 'You are greate'
            del_all_text()

        else:
            answer['background'] = 'yellow'
            answer['text'] = 'Text passwords it is different'
            del_all_text()
    else:
        answer['background']='red'
        answer['text']='You are not input text'



def del_all_text():
    name.delete(0,tk.END)
    password.delete(0,tk.END)



tk.Label(win,text='Пароль').grid(row=0,column=0,stick='we',ipady=20,ipadx=40,padx=[40,0],pady=[40,0])
tk.Label(win,text='Повторите пароль').grid(row=1,column=0,stick='we',ipady=20,ipadx=40,padx=[40,0])

name=(tk.Entry(win))
name.grid(row=0,column=1,stick='w',ipady=20,ipadx=40,padx=[0,40],pady=[40,0])

password=tk.Entry(win)
password.grid(row=1,column=1,stick='w',ipady=20,ipadx=40,padx=[0,0],pady=[0,0])

button=tk.Button(win, text='Send your  password',background='pink',font=('Arial',15),
                 command=get_text)
button.grid(row=2, column=0, stick='we',ipady=20, padx=40,columnspan=2)


answer=tk.Label(win,text=' ',background='black',font=('Arial',15))
answer.grid(row=3,column=0,stick='we',ipady=20,padx=40,columnspan=2,pady=80)



win.mainloop()
