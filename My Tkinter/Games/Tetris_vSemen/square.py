import tkinter as tk

from field import Field


class Square:
    """
    Класс для отдельного квадрата фигуры
    Каждый квадрат - это Label с цветом
    """

    def __init__(self, win, x, y, row, column, color):
        """
        :param win: главное окно
        :param x: позиция X в пикселях
        :param y: позиция Y в пикселях
        :param color: цвет квадрата
        """
        self.win = win
        self.x = x
        self.y = y
        self.row = row
        self.column = column

        self.color = color

        # Создаем Label для этого квадрата
        self.label = tk.Label(win, text=f"", background=color,
                              foreground=color, font=("Arial", 13),
                              height=1, width=2)
        self.place_on_field()



    def __del__(self):
        self.label.destroy()



    def say(self):
        print(self.__dict__)

    def place_on_field(self):
        """Размещает квадрат на поле"""
        self.label.place(x=self.x, y=self.y)

    def move(self, dx, dy):
        """Перемещает квадрат на dx, dy пикселей
        """
        self.x += dx
        self.y += dy
        self.step_left_right(direction=dx)
        self.place_on_field()

    def step_left_right(self, direction):
        if direction > 0:
            self.row += 1
        else:
            self.row -= 1

    def move_to(self, x, y):
        """Перемещает квадрат в абсолютные координаты"""
        self.x = x
        self.y = y
        self.place_on_field()

    def destroy(self):
        """Удаляет квадрат с поля"""
        if self.label:
            self.label.destroy()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_position(self):
        """Возвращает текущую позицию в пикселях"""
        return self.x, self.y

    def get_color(self):
        """Возвращает цвет квадрата"""
        return self.color
