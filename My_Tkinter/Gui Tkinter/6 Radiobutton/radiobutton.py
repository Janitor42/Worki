import tkinter as tk

win = tk.Tk()

win.geometry('500x500')
win.config(background='black')


#фун-ция see  обрабатывает значение (get) переменной color, проверяет и меняет переменную text
#что в свою очередь меняет текст который пишется под флажками
#win.config вызывается в каждом if и меняет экран на другой цвет (совпадает с флажками)
def see():
    text.set(color.get())
    win.config(background=text.get())


    # if color.get() == 'black':
    #     text.set('выбран black')
    #     win.config(background='black')
    # if color.get() == 'green':
    #     text.set('выбран green')
    #     win.config(background='green')
    # if color.get() == 'yellow':
    #     win.config(background='yellow')
    #     text.set('выбран yellow')

color = tk.StringVar()
color.set('No')

text = tk.StringVar()

#кнопки radiobutton связаны при помощи переменной variable (все ссылаются на нее
#value -значение которое принимает переменная color при нажатии на именно этот фражок,
#команда - команда ктороая будет происходить при нажатии на эту кнопку
tk.Radiobutton(win, text='black screen', variable=color, value='black', command=see,font=('Arial',20),width=20).pack()
tk.Radiobutton(win, text='green screen', variable=color, value='green', command=see,font=('Arial',20),width=20).pack()
tk.Radiobutton(win, text='yellow screen', variable=color, value='yellow', command=see,font=('Arial',20),width=20).pack()

#просто пример как на экране отображать а не в консоле печатать что выбрано
#textvariable - переменная на которую ссылается пр-ма. меняется в режиме реального времнени если менять переменную
tk.Label(win, textvariable=text,font=('Arial',20)).pack(pady=100)

win.mainloop()
