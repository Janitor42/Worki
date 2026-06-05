import tkinter as tk




class Square:
    """
    Класс для отдельного квадрата фигуры
    Каждый квадрат - это Label с цветом
    """

    @staticmethod
    def change_column(obj):
        for i in obj:
            i.set_column(1)

    @staticmethod
    def change_row(obj, num):
        for i in obj:
            i.set_row(num)

    def __init__(self, win, x, y, row, column, color):
        """
        + win: главное окно
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
                              foreground=color, font=("Arial", 10),
                              height=1, width=2)

    def __del__(self):
        self.label.destroy()

    def set_column(self, column):
        self.column += column

    def set_row(self, row):
        self.row += row

    def say(self):
        print(self.__dict__)

    def place_on_field(self):
        """Размещает квадрат на поле"""
        self.label.place(x=self.x, y=self.y)

    def move(self, dx=0, dy=0):
        """Перемещает квадрат на dx, dy пикселей"""
        self.x += dx
        self.y += dy

    def step_left_right(self, direction):
        if direction > 0:
            self.row += 1
        else:
            self.row -= 1

    def move_down(self,):
        """Перемещает вниз"""
        self.move(dy=1)
        self.place_on_field()
    # def move_to(self, x, y):
    #     """Перемещает квадрат в абсолютные координаты"""
    #     self.x = x
    #     self.y = y
    #     self.place_on_field()

    def destroy(self):
        """Удаляет квадрат с поля"""
        if self.label:
            self.label.destroy()

    def get_x(self):
        """Возвращает x"""
        return self.x

    def get_y(self):
        """Возвращает y"""
        return self.y

    def get_column(self):
        """Возвращает колонну"""
        return self.column

    def get_row(self):
        """Возвращает ряд"""
        return self.row

    def get_position(self):
        """Возвращает текущую позицию в пикселях"""
        return [self.x, self.y]

    def get_color(self):
        """Возвращает цвет квадрата"""
        return self.color
