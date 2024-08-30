import tkinter as tk
import math


class GameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Коллизия круга и квадрата в Tkinter")
        self.canvas = tk.Canvas(master, width=400, height=400, bg='white')
        self.canvas.pack()

        # Создаем квадрат и круг
        self.square = self.canvas.create_rectangle(150, 150, 250, 250, fill='blue')
        self.circle = self.canvas.create_oval(50, 50, 100, 100, fill='red')

        # Обработчик событий для перемещения круга
        self.canvas.bind("<KeyPress>", self.move_circle)
        self.canvas.focus_set()

    def move_circle(self, event):
        # Получаем текущее положение круга
        coords = self.canvas.coords(self.circle)
        dx, dy = 0, 0

        if event.keysym == 'Up':
            dy = -1
        elif event.keysym == 'Down':
            dy = 1
        elif event.keysym == 'Left':
            dx = -1
        elif event.keysym == 'Right':
            dx = 1

        # Перемещаем круг
        self.canvas.move(self.circle, dx, dy)

        # Проверка коллизии
        if self.check_collision(self.circle, self.square):
            print("Коллизия обнаружена!")

    def check_collision(self, circle, square):
        # Получаем координаты круга
        x0, y0, x1, y1 = self.canvas.coords(circle)
        circle_center_x = (x0 + x1) / 2
        circle_center_y = (y0 + y1) / 2
        circle_radius = (x1 - x0) / 2

        # Получаем координаты квадрата
        square_coords = self.canvas.coords(square)
        square_x0, square_y0, square_x1, square_y1 = square_coords

        # Находим ближайшую точку на квадрате к центру круга
        closest_x = max(square_x0, min(circle_center_x, square_x1))
        closest_y = max(square_y0, min(circle_center_y, square_y1))

        # Вычисляем расстояние между центром круга и ближайшей точкой
        distance_x = circle_center_x - closest_x
        distance_y = circle_center_y - closest_y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        # Проверяем, происходит ли коллизия
        return distance < circle_radius


if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()