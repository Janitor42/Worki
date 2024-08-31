import tkinter as tk


class BouncingBall:
    def __init__(self, canvas):
        self.canvas = canvas
        self.radius = 20
        self.ball = self.canvas.create_oval(100, 100, 100 + 2 * self.radius, 100 + 2 * self.radius, fill="blue")

        self.dx = 3  # Скорость перемещения по оси X
        self.dy = 2  # Скорость перемещения по оси Y

        self.animate()

    def animate(self):
        # Получаем текущие координаты шарика
        x1, y1, x2, y2 = self.canvas.coords(self.ball)

        # Проверяем, нужно ли менять направление
        if x1 <= 0 or x2 >= self.canvas.winfo_width():  # Удар о левую или правую границу
            self.dx = -self.dx
        if y1 <= 0 or y2 >= self.canvas.winfo_height():  # Удар о верхнюю или нижнюю границу
            self.dy = -self.dy

        # Перемещаем шарик
        self.canvas.move(self.ball, self.dx, self.dy)

        # Запускаем следующий кадр анимации через 20 миллисекунд
        self.canvas.after(20, self.animate)


# Создаем главное окно
root = tk.Tk()
root.title("Полет шарика")

# Создаем Canvas
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Создаем и запускаем шарик
ball = BouncingBall(canvas)

# Запускаем главный цикл
root.mainloop()