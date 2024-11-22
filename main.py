import tkinter as tk

win = tk.Tk()

win.geometry('400x500+100+200')
win.config(background='black')

entry = tk.Entry(win, justify='right', width=18, font=('Arial', 30))
entry.place(x=0, y=0)
list_of_buttons = []
list_of_singles = []
list_of_singles2 = ['+', '-', '/', '*', '=']
x = 0
y = 50
text = 9
click = 'False'

for i in range(10):
    button = tk.Button(win, width=3, height=1,
                       relief="ridge", bd=10,
                       text=text, font=('Arial', 20, 'bold'),
                       )
    def tx():
        print(text)



    text -= 1
    list_of_buttons.append(button)
    button.place(x=x, y=y)
    x += 75
    if x >= 225:
        y += 70
        x = 0

    # def pri(event):
    #     print(button)
    #
    #
    # button.bind('<Enter>', pri)

# todo запуск с одной фун-ции


a = tk.Button(win, width=3, height=1, relief="ridge", bd=10, text=',', font=('Arial', 20, 'bold'))
list_of_buttons.append(a)
a.place(x=x, y=y)

win.mainloop()
