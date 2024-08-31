import tkinter as tk
import math


# Функция для проверки коллизии между шариком и прямоугольником
def check_collision(circle, rectangle):
    circle_x, circle_y, circle_radius = circle
    rect_x1, rect_y1, rect_x2, rect_y2 = rectangle

    # Находим ближайшую точку на прямоугольнике к окружности
    nearest_x = max(rect_x1, min(circle_x, rect_x2))
    nearest_y = max(rect_y1, min(circle_y, rect_y2))

    # Вычисляем расстояние между центром окружности и ближайшей точкой
    distance = math.sqrt((nearest_x - circle_x) ** 2 + (nearest_y - circle_y) ** 2)

    # Проверяем пересечение
    return distance < circle_radius


# Функция для отрисовки объектов на Canvas
def draw_objects():
    canvas.delete("all")  # Очистка Canvas
    canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, fill="red")  # Прямоугольник
    canvas.create_oval(circle_x - circle_radius, circle_y - circle_radius,
                       circle_x + circle_radius, circle_y + circle_radius, fill="blue")  # Шарик

    # Проверка коллизии
    if check_collision((circle_x, circle_y, circle_radius), (rect_x1, rect_y1, rect_x2, rect_y2)):
        print("Collision detected!")
    else:
        print("No collision.")


# Функция для движения шарика
def move_circle(dx, dy):
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


# Обработчик нажатий клавиш
def on_key_press(event):
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

# Параметры прямоугольника
rect_x1, rect_y1 = 150, 150
rect_x2, rect_y2 = 250, 250

# Параметры шарика
circle_x, circle_y = 200, 200  # Центр шарика
circle_radius = 30  # Радиус шарика

# Связывание обработчика событий клавиатуры
root.bind("<KeyPress>", on_key_press)

# Изначальная отрисовка объектов
draw_objects()

root.mainloop()