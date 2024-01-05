import tkinter as tk

win = tk.Tk()

win.geometry('500x500')
win.config(background='black')

buttons = []


def create_calendar():
    count = 0
    for i in range(5):
        for j in range(7):
            count += 1
            if count > 31:
                pass
            else:
                if j >= 5:
                    my_bn = tk.Button(win, text=count,
                                      background='green')
                    buttons.append(my_bn)
                    my_bn.grid(row=i, column=j, stick='we')
                else:
                    my_bn = tk.Button(win, text=count)
                    buttons.append(my_bn)
                    my_bn.grid(row=i, column=j, stick='we')


def customize_calendar():
    for i in range(7):
        win.grid_columnconfigure(i, minsize=50)


create_calendar()
customize_calendar()

win.mainloop()
