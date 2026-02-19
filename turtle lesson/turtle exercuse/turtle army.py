import turtle
import time

# Настройка экрана
screen = turtle.Screen()
screen.title("20 черепах РИСУЮТ ОДНОВРЕМЕННО")
screen.bgcolor("white")
screen.tracer(0)  # Отключаем автообновление для ручного управления анимацией

# Создаем список для хранения всех черепах
turtles = []

# Настройки сетки
rows = 4  # 4 ряда
cols = 5  # 5 колонок (всего 20 черепах)
start_x = -250  # Начальная позиция X
start_y = 200  # Начальная позиция Y
spacing = 120  # Расстояние между черепахами

print("Создаю 20 черепах в сетке 4x5...")

# Создаем черепах в сетке (ряды и колонки)
for row in range(rows):
    for col in range(cols):
        # Вычисляем позицию для каждой черепахи
        x = start_x + col * spacing
        y = start_y - row * spacing

        # Создаем черепаху
        t = turtle.Turtle()
        t.color("black")
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.speed(0)
        t.pensize(2)

        # Поворачиваем каждую черепаху для начала рисования с правой стороны
        t.setheading(0)  # Все смотрят вправо

        # Добавляем черепаху в список
        turtles.append(t)

print("Все черепахи готовы к одновременному рисованию!")
screen.update()  # Показываем всех черепах
time.sleep(1)

# Параметры анимации
square_size = 60  # Размер квадрата
steps = square_size  # Количество шагов анимации (1 шаг = 1 пиксель)

print("Начинаем одновременное рисование квадратов...")

# АНИМАЦИЯ: рисуем первую сторону квадрата (вправо)
for step in range(steps):
    for t in turtles:
        t.forward(1)  # Все делают маленький шаг
    screen.update()  # Обновляем экран после ВСЕХ шагов
    time.sleep(0.01)  # Задержка для плавности

print("Первая сторона готова!")

# Поворачиваем всех для второй стороны
for t in turtles:
    t.right(90)

# АНИМАЦИЯ: рисуем вторую сторону квадрата (вниз)
for step in range(steps):
    for t in turtles:
        t.forward(1)
    screen.update()
    time.sleep(0.01)

print("Вторая сторона готова!")

# Поворачиваем всех для третьей стороны
for t in turtles:
    t.right(90)

# АНИМАЦИЯ: рисуем третью сторону квадрата (влево)
for step in range(steps):
    for t in turtles:
        t.forward(1)
    screen.update()
    time.sleep(0.01)

print("Третья сторона готова!")

# Поворачиваем всех для четвертой стороны
for t in turtles:
    t.right(90)

# АНИМАЦИЯ: рисуем четвертую сторону квадрата (вверх)
for step in range(steps):
    for t in turtles:
        t.forward(1)
    screen.update()
    time.sleep(0.01)

print("Четвертая сторона готова!")

# Замыкаем квадрат - последний поворот
for t in turtles:
    t.right(90)

print("Все 20 квадратов нарисованы ОДНОВРЕМЕННО!")

# Добавляем информационный текст
info = turtle.Turtle()
info.hideturtle()
info.penup()
info.goto(0, -300)
info.color("black")
info.write("20 черепах нарисовали квадраты ОДНОВРЕМЕННО!",
           align="center", font=("Arial", 16, "bold"))

info.goto(0, -330)
info.write("Каждый шаг анимации: все черепахи двигаются синхронно",
           align="center", font=("Arial", 10, "normal"))

# Номера черепах
for i, t in enumerate(turtles):
    t.penup()
    t.goto(t.xcor() + square_size / 2 + 10, t.ycor() - square_size / 2 - 20)
    t.write(f"№{i + 1}", align="center", font=("Arial", 8, "normal"))

screen.update()
turtle.done()