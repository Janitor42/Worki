
import tkinter as tk

def draw_segments(canvas):
    # Определяем координаты рамки, в которой будет рисоваться круг
    x1, y1, x2, y2 = 50, 50, 250, 250
    # Определяем свойства сегментов
    colors = ['red', 'green', 'blue', 'yellow']
    start_angles = [0, 90, 180, 270]
    extent = 90  # Угол для каждого сегмента

    # Рисуем 4 сегмента
    for i in range(4):
        canvas.create_arc(x1, y1, x2, y2, start=start_angles[i], extent=extent,
                          fill=colors[i], outline='black', width=2)

# Создаем основное окно
root = tk.Tk()
root.title("Круг из 4 сегментов")

# Создаем канвас
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Рисуем сегменты
draw_segments(canvas)

# Запускаем главный цикл
root.mainloop()