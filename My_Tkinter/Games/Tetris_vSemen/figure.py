import random as rd
import constants
from field import Field
from square import Square


class Figure:

    # region Инициализация
    def __init__(self, win):
        self.color_figure = None
        self.win = win
        self.name_figure = None
        self.number_position = 0
        self.obj_figure = []
        self.x_start = constants.START_X
        self.y_start = constants.START_Y
        self.install_figure(self.choice_figure())
    # endregion

    # region Отладка и информация
    def say_figure(self):
        """Вывод информации о фигуре"""
        for square in self.obj_figure:
            square: Square
            square.say()
        print(60 * '___')
    # endregion

    # region Движение вниз
    def can_move_down(self):
        for square in self.obj_figure:
            square: Square
            if square.check_down_place():
                return False
        return True

    def move_down(self):
        """Движение фигуры вниз"""
        for square in self.obj_figure:
            square.move(dx=0, dy=1)
        self.y_start += 1
    # endregion

    # region Создание и отрисовка фигуры
    def draw_figure(self, figure):
        """Отрисовка фигуры по матрице"""
        x = self.x_start
        y = self.y_start

        for row in figure:
            for part in row:
                if part == 1:
                    sq = Square(win=self.win, x=x, y=y, color=self.color_figure)
                    self.obj_figure.append(sq)
                x += 26
            x = self.x_start
            y += 26

    def choice_figure(self):
        """Выбор случайной фигуры"""
        choice = rd.choice(list(constants.FIGURES))
        self.color_figure = constants.COLORS[choice]
        self.name_figure = choice
        matrix_figure = constants.FIGURES[choice][self.number_position]
        return matrix_figure

    def install_figure(self, matrix_figure):
        """Установка фигуры"""
        self.destroy_old_figure()
        self.draw_figure(figure=matrix_figure)
    # endregion

    # region Движение влево-вправо
    def move_left(self, event=None):
        """Движение влево"""
        if self.check_left_border(direction=-constants.STEP):
            self.move_obj(direction=-constants.STEP)
            self.x_start -= constants.STEP

    def move_right(self, event=None):
        """Движение вправо"""
        if self.check_right_border(direction=constants.STEP):
            self.move_obj(direction=constants.STEP)
            self.x_start += constants.STEP

    def check_left_border(self, direction):
        """Проверка левой границы"""
        for square in self.obj_figure:
            square: Square
            if square.get_x() + direction < constants.LEFT_BORDER:
                return False
        return True

    def check_right_border(self, direction):
        """Проверка правой границы"""
        for square in self.obj_figure:
            square: Square
            if square.get_x() + direction > constants.RIGHT_BORDER:
                return False
        return True

    def move_obj(self, direction):
        """Перемещение всех квадратов фигуры"""
        for square in self.obj_figure:
            square: Square
            square.move(dx=direction, dy=0)
    # endregion

    # region Поворот фигуры
    def rotate(self, event=None):
        """Поворот фигуры"""
        next_position = self.check_index_position()
        next_matrix = constants.FIGURES[self.name_figure][next_position]

        if self.try_rotate(next_matrix=next_matrix):
            self.destroy_old_figure()
            self.draw_figure(figure=next_matrix)
            self.number_position = next_position

    def try_rotate(self, next_matrix):
        """Проверка возможности поворота"""
        x = self.x_start
        y = self.y_start

        for row in next_matrix:
            for part in row:
                if part == 1 and self.check_borders_x(x=x):
                    return False
                x += 26
            x = self.x_start
            y += 26
        return True

    def check_index_position(self):
        """Получение следующей позиции поворота"""
        count_position = len(list(constants.FIGURES[self.name_figure])) - 1
        next_position = self.number_position

        if next_position >= count_position:
            next_position = 0
        else:
            next_position += 1
        return next_position

    def check_borders_x(self, x):
        """Проверка границ по X"""
        if x > constants.RIGHT_BORDER or x < constants.LEFT_BORDER:
            return True
        return False
    # endregion

    # region Уничтожение фигуры
    def destroy_old_figure(self):
        """Уничтожение старой фигуры"""
        for square in self.obj_figure:
            square: Square
            square.destroy()
        self.obj_figure.clear()
    # endregion

    # region Фиксация фигуры на поле
    def record_figure_on_field(self):
        """Запись фигуры на игровое поле"""
        for square in self.obj_figure:
            square: Square
            Field.record_field(square=square)
    # endregion

    # region Создание новой фигуры
    def make_new_figure(self):
        """Создание новой фигуры"""
        self.number_position = 0
        self.name_figure = None
        self.x_start = constants.START_X
        self.y_start = constants.START_Y
        self.install_figure(self.choice_figure())
    # endregion