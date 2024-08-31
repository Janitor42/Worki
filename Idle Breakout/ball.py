import screen
import tkinter as tk


def buy_ball():
    Ball()


def live_ball():
    for i in Ball.all_ball:
        Ball.move_ball(i)


class Ball:
    all_ball = []
    all = []

    def __init__(self):
        self.radius = 8
        self.x_1 = (int(screen.x) // 2) - self.radius
        self.x_2 = (int(screen.x) // 2) + self.radius
        self.y_1 = (int(screen.y) // 2) - self.radius
        self.y_2 = (int(screen.y) // 2) + self.radius

        self.can = screen.can
        self.name = self.can.create_oval(self.x_1, self.y_1, self.x_2, self.y_2, fill='yellow')
        self.power = 1

        self.dx = 1  # Скорость перемещения по оси X
        self.dy = 1  # Скорость перемещения по оси Y

        Ball.all_ball.append(self.name)
        Ball.all.append(self)
        # !!!!!!!!!!!!!!!!!!
        # for i in Ball.all:
        #     print(i.name)

    # def move_ball(self):
    #     x1, y1, x2, y2 = screen.can.coords(self.name)
    #
    #     # Проверяем, нужно ли менять направление
    #     if x1 <= 0 or x2 >= screen.can.winfo_width():  # Удар о левую или правую границу
    #         self.dx = -self.dx
    #     if y1 <= 0 or y2 >= screen.can.winfo_height():  # Удар о верхнюю или нижнюю границу
    #         self.dy = -self.dy
    #
    #     self.can.move(self.name, self.dx, self.dy)
