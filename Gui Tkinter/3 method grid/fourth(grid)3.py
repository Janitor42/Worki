import tkinter as tk

win = tk.Tk()

win.geometry('500x500')
win.config(background='black')


#1 begin for идет по колонкам, 2 button по рядам
for i in range(5):
    for j in range(2):
        my_bn=(tk.Button(win,text=f'Hello{i} {j}'))#вызываем создание кнопки, при помощи f строки ложим в название слово Hello и значение переменных i и j
        my_bn.grid(row=i,column=j)# затем  вызываем метод grid который распологает кнопки на окне



# #тоже самое но в 1 begin строчку
# for i in range(5):
#     for j in range(2 button):
#         tk.Button(win,text=f'Hello{i} {j}').grid(row=i,column=j)#вызываем создание кнопки, при помощи f строки ложим в название
#         #слово Hello и значение переменных i и j затем здесь же вызываем метод grid который распологает кнопки на окне


win.grid_columnconfigure(0,minsize=10)#метод применяется к окну,указывается индекс колонки, задает минимальный размер
win.grid_columnconfigure(1,minsize=100)#метод применяется к окну,указывается индекс колонки, задает минимальный размер

win.mainloop()



