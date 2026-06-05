import tkinter as tk

from field import Field
import constants


class Square:
    """
    Класс для отдельного квадрата фигуры
    Каждый квадрат - это Label с цветом
    """

    # region Инициализация
    def __init__(self, win, x, y, color):
        """
        :param win: главное окно
        :param x: позиция X в пикселях
        :param y: позиция Y в пикселях
        :param color: цвет квадрата
        """
        self.win = win
        self.x = x
        self.y = y

        self.color = color

        # Создаем Label для этого квадрата
        self.label = tk.Label(win, text=f"", background=color,
                              foreground=color, font=("Arial", 10),
                              height=1, width=2, relief="raised", bd=2)

        self.place_on_field()

    def __del__(self):
        self.label.destroy()
    # endregion

    # region Отладка и информация
    def say(self):
        print(self.__dict__)
    # endregion

    # region Позиционирование и перемещение
    def place_on_field(self):
        """Размещает квадрат на поле"""
        self.label.place(x=self.x, y=self.y)

    def move(self, dx, dy):
        """Перемещает квадрат на dx, dy пикселей"""
        self.x += dx
        self.y += dy
        self.place_on_field()

    def move_to(self, x, y):
        """Перемещает квадрат в абсолютные координаты"""
        self.x = x
        self.y = y
        self.place_on_field()

    def destroy(self):
        """Удаляет квадрат с поля"""
        if self.label:
            self.label.destroy()
    # endregion

    # region Геттеры
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_pos(self):
        """Возвращает текущую позицию в пикселях"""
        return [self.x, self.y]

    def get_color(self):
        """Возвращает цвет квадрата"""
        return self.color
    # endregion

    # region Проверка столкновений
    def check_down_place(self):
        """Проверяет, можно ли двигаться вниз"""
        my_next_pos = [self.x, self.y + constants.STEP]
        field_down = Field.get_position(place=my_next_pos)
        if field_down:
            return True

        if self.check_under_border():
            return True

        return False

    def check_under_border(self):
        """Проверяет достижение нижней границы"""
        if self.get_y() >= constants.Y_LAST_FIELD:
            return True
        return False
    # endregion