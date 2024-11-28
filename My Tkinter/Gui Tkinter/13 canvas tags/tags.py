import tkinter as tk

win = tk.Tk()
x = '500'
y = '500'
win.geometry(x + 'x' + y)
win.config(background='black')

can = tk.Canvas(bg='white', width=int(x) - 300, height=int(y) - 300)  # канвас
can.pack(expand=True)

# tags=['создание тега в момент создания элемента']]
line = can.create_line(0, 100, 200, 100, width=10, fill='orange', tags=['one','just line'])
first = can.gettags(line)  # получение тега - через канвас
print(first)

line2 = can.create_line(0, 150, 200, 150, width=10, fill='blue')
can.addtag('one', 'withtag', line2)
# добавление тега через метод addtag Первый параметр - добавляемый тег,
# второй параметр - команда, обычно "withtag".
# Третий параметр - идентификатор элемента, для которого добавляется тег:

first = can.gettags(line2)  # получение тега - через канвас
print(first)


# так же можно получить идентификаторы элементов по определенному
# тегу с помощью метода find_withtag(), в который передается имя тега.
# по тегу ищем номера(идентификаторы элементов)
for i in can.find_withtag('one'):

    print(i.conjugate())


#удаление tag через dtags()
can.dtag(line,'just line')
first = can.gettags(line)


#Конфигурация через тег
#С помощью метода itemconfigure() для элементов с определенным тегом можно установить различные опции
#Первый параметр - тег или идентификатор элемента, а второй - набор устанавливаемых опций. Например:
can.itemconfig('one',fill='pink',width=5)#поменял всем у кого tag one цвет на pink и width


win.mainloop()
