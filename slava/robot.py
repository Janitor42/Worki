import tkinter as tk

class Robot:

    def __init__(self,callback):
        self.callback=callback

        self.edit_win = tk.Toplevel()
        self.edit_win.title('Напиши имя Роботу')
        self.edit_win.geometry('500x300-750+0')
        self.edit_win.config(background='brown')



        self.edit_win.grab_set()
        self.edit_win.focus_set()
        self.edit_win.lift()

        self.label=tk.Label(self.edit_win,text='пиши имя этому дебилу')
        self.label.place(x=50,y=100)

        self.entry_1=tk.Entry(self.edit_win)
        self.entry_1.place(x=50,y=125)

        self.label=tk.Label(self.edit_win,text='пиши номер модели дебила')
        self.label.place(x=50,y=150)

        self.entry_2=tk.Entry(self.edit_win)
        self.entry_2.place(x=50,y=175)

        self.bt_confirm=tk.Button(self.edit_win,text='подтвердить',command=self.action_confirm)
        self.bt_confirm.place(x=200,y=125)


    def action_confirm(self):
        hero=self.entry_1.get()+' '+self.entry_2.get()
        self.callback(hero)


        self.edit_win.destroy()

        self.edit_win.mainloop()