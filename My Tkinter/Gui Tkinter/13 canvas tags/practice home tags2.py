import tkinter as tk
import random

def create_colored_circles(canvas, num_circles=10):
    colors = ['red', 'green', 'blue']
    for _ in range(num_circles):
        x, y = random.randint(50, 350), random.randint(50, 350)
        r = 20
        color = random.choice(colors)
        canvas.create_oval(x - r, y - r, x + r, y + r,
                           fill=color, outline='black',
                           tags=(color, 'circle'))

def show_red():
    canvas.itemconfigure('red', state='normal')
    canvas.itemconfigure('green', state='hidden')
    canvas.itemconfigure('blue', state='hidden')

def show_green():
    canvas.itemconfigure('red', state='hidden')
    canvas.itemconfigure('green', state='normal')
    canvas.itemconfigure('blue', state='hidden')

def show_blue():
    canvas.itemconfigure('red', state='hidden')
    canvas.itemconfigure('green', state='hidden')
    canvas.itemconfigure('blue', state='normal')

# --- GUI setup ---
root = tk.Tk()
root.title("Сортировка по цвету")

canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

# Кнопки без lambda
tk.Button(frame, text="Показать красные", command=show_red).pack(side='left', padx=5)
tk.Button(frame, text="Показать зеленые", command=show_green).pack(side='left', padx=5)
tk.Button(frame, text="Показать синие", command=show_blue).pack(side='left', padx=5)

create_colored_circles(canvas)

root.mainloop()
