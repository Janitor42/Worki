import tkinter as tk
import math

def check_collision(circle, square):
    """Проверка коллизии между кругом и квадратом."""
    circle_x, circle_y, circle_r = circle
    square_x1, square_y1, square_x2, square_y2 = square

    # Найти ближайшую точку на квадрате к окружности
    nearest_x = max(square_x1, min(circle_x, square_x2))
    nearest_y = max(square_y1, min(circle_y, square_y2))

    # Рассчитать расстояние между центром окружности и ближайшей точкой
    distance = math.sqrt((nearest_x - circle_x) ** 2 + (nearest_y - circle_y) ** 2)

    # Проверить пересечение
    return distance < circle_r

def draw_objects():
    """Отрисовка объекта на Canvas."""
    canvas.delete("all")  # Очистить Canvas
    canvas.create_rectangle(square_x1, square_y1, square_x2, square_y2, fill="red")  # Квадрат
    canvas.create_oval(circle_x - circle_radius, circle_y - circle_radius,
                       circle_x + circle_radius, circle_y + circle_radius, fill="blue")  # Шарик

    # Проверка коллизии
    if check_collision((circle_x, circle_y, circle_radius), (square_x1, square_y1, square_x2, square_y2)):
        print("Collision detected!")
    else:
        print("No collision.")

def move_circle(dx, dy):
    """Движение шарика."""
    global circle_x, circle_y

    circle_x += dx
    circle_y += dy

    # Проверка границ Canvas
    if circle_x - circle_radius < 0:  # Левый край
        circle_x = circle_radius
    if circle_x + circle_radius > canvas.winfo_width():  # Правый край
        circle_x = canvas.winfo_width() - circle_radius
    if circle_y - circle_radius < 0:  # Верхний край
        circle_y = circle_radius
    if circle_y + circle_radius > canvas.winfo_height():  # Нижний край
        circle_y = canvas.winfo_height() - circle_radius

    draw_objects()

def on_key_press(event):
    """Обработчик нажатия клавиши."""
    if event.keysym == "Up":
        move_circle(0, -5)
    elif event.keysym == "Down":
        move_circle(0, 5)
    elif event.keysym == "Left":
        move_circle(-5, 0)
    elif event.keysym == "Right":
        move_circle(5, 0)

# Создание главного окна
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Параметры квадрата
square_x1, square_y1 = 150, 150
square_x2, square_y2 = 250, 250

# Параметры шарика
circle_x, circle_y = 200, 200  # Центр шара
circle_radius = 30              # Радиус шара

# Связываем обработчик событий клавиатуры
root.bind("<KeyPress>", on_key_press)

# Изначальная отрисовка объектов
draw_objects()

root.mainloop()