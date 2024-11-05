import time
import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Полет шарика")

# Создаем Canvas
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Создаем шарик (овал)
ball = canvas.create_oval(10, 10, 50, 50, fill="blue")

# Задаем начальные параметры движения
dx = 2  # Скорость по горизонтали
dy = 2  # Скорость по вертикали

# Основной цикл анимации
while True:
    # Получаем текущие координаты шарика
    x1, y1, x2, y2 = canvas.coords(ball)
    #
    # # Изменяем координаты шарика
    # if x2 + dx > 400 or x1 + dx < 0:  # Проверка на столкновение с границами по горизонтали
    #     dx = -dx  # Меняем направление
    # if y2 + dy > 400 or y1 + dy < 0:  # Проверка на столкновение с границами по вертикали
    #     dy = -dy  # Меняем направление

    # Обновляем позицию шарика
    canvas.move(ball, dx, dy)

    # Обновляем интерфейс
    root.update()  # Обновление окна
    time.sleep(0.1)
    
# Запускаем главный цикл
root.mainloop()