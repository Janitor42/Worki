
import tkinter as tk, random, time
from tkinter import ttk

win = tk.Tk()
win.title("First")
win.geometry("470x420+740+250")
win.minsize(200, 200)
win.maxsize(1000, 1000)
win.config(background="green")
game_field = []
x_block = -47
y_block = 30
start = time.time()
finish = time.time()
time1 = finish - start
time1 = int(time1)
counts_bomb = 0
counts_for_index = [11, 10, 9, 1, 1, 9, 10, 11]
value_flags = 10

counts0to80 = []
difficulty = ["Простой", "Нормальный", "Сложный"]





def place_blocks(event):
    global relative_x

    cursor_x, cursor_y = win.winfo_pointerxy()

    # Получаем координаты окна
    window_x = win.winfo_rootx()
    window_y = win.winfo_rooty()

    # Вычисляем позицию курсора относительно окна
    relative_x = cursor_x - window_x
    relative_y = cursor_y - window_y
    block = find_block(relative_x, relative_y)
    print(block,relative_x,relative_y)
    if block:
        find_neighbours(block)


def find_neighbours(block):
    all = bokovie_blockes(block)
    for i in all:
        index = block + i
        if 0 <= index <= 120:
            game_field[index].config(background='yellow')

def bokovie_blockes(block):
    a=20
    if block==a:
        return [ -10, -9, 1, 10, 11]
    else:
        return [-13, -12, -11, -1, 1, 11, 12, 13]


def find_block(relative_x, relative_y):
    x1 = 1-47
    x2 = 40-47
    y1 = 73-40
    y2 = 113-40
    number = 0
    for i in range(120):
        if relative_x > x1 and relative_x < x2 and relative_y > y1 and relative_y < y2:
            return number-1
            break
        number = number + 1
        x1 = x1 + 43
        x2 = x2 + 43
        if x2 > 470:
            y1 = y1 + 47
            y2 = y2 + 47
            x1 = 1-47
            x2 = 40-47

index=0

for i in range(120):
    if x_block >= 497:
        x_block = -47
        y_block = y_block + 43
    a = tk.Button(win, text="    ", background="green", foreground="gray2", font=("Arial", 15), relief=tk.RAISED,
                  activebackground="red")

    index_label=tk.Label(win, text=index, background="green", foreground="gray2", font=("Arial", 15), relief=tk.RAISED)
    index_label.place(x=x_block,y=y_block)
    index=index+1
    a.place(x=x_block, y=y_block)
    x_block = x_block + 47
    game_field.append(a)
    print(i,x_block,y_block,)



inv_label = tk.Label(win, text="                                                                                                                     ", background="black", foreground="white", font=("Arial", 10))
inv_label.place(x=0,y=30)
frame_inf = tk.Frame(win, background="dark green")
frame_inf.place(x=0, y=-10, )
box = ttk.Combobox(frame_inf, values=difficulty, state="readonly", background="dark green")
box.grid(row=0, column=0, padx=30)
flag = tk.Label(frame_inf, text=value_flags, background="dark green", foreground="white", font=("Arial", 10))
flag.grid(row=0, column=1, padx=30)
timer = tk.Label(frame_inf, text=time1, background="dark green", foreground="white", font=("Arial", 10))
timer.grid(row=0, column=2, padx=(0, 210), pady=(30, 30))
win.bind('<ButtonPress>', place_blocks)

while counts_bomb != 10:
    a = random.randint(0, 79)

    if a in counts0to80:
        continue
    else:
        counts0to80.append(a)
        counts_bomb = counts_bomb + 1
        game_field[a].config(background="black")

while True:
    finish = time.time()
    time1 = finish - start
    time1 = int(time1)
    timer.config(text=time1)
    win.update()