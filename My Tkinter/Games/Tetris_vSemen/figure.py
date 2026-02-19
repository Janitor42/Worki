import random as rd

import constants


from field import Field
from square import Square


class Figure:
    step_left_right = 26

    def __init__(self, win):

        self.color_figure = None
        self.win = win
        self.name_figure = None
        self.number_position = 0
        self.obj_figure = []
        self.obj_figure_next = []
        self.install_figure(*self.choice_figure())
        self.position_matrix = constants.START_POSITIONS[self.name_figure]

        self.win.bind("<Left>", self.move_left)
        self.win.bind("<Right>", self.move_right)

        self.win.bind("<Up>", self.rotate)

    """определение и создание фигуры"""

    # region
    def choice_figure(self):
        choice = rd.choice(list(constants.FIGURES))
        self.color_figure = constants.COLORS[choice]
        self.name_figure = choice
        row_column = constants.START_POSITIONS[self.name_figure]
        matrix_figure = constants.FIGURES[choice][self.number_position]
        return row_column, matrix_figure

    def install_figure(self, row_column, matrix_figure):
        place = row_column.copy()
        for row in matrix_figure:
            print(row)
            for part in row:
                if part == 1:
                    part_field = Field.set_place(start_place=list(place.values()))

                    x = Square(win=self.win, x=part_field.get_x(), y=part_field.get_y(),
                               row=place['row'], column=place['column'],
                               color=self.color_figure)
                    self.obj_figure.append(x)

                place['row'] += 1
            place['row'] = 4
            place['column'] += 1

    # endregion
    """логика движения лево право"""

    # region
    def move_left(self, event=None):
        if self.check_left_border(direction=-Figure.step_left_right):
            self.move_obj(direction=-Figure.step_left_right)

    def move_right(self, event=None):
        if self.check_right_border(direction=Figure.step_left_right):
            self.move_obj(direction=Figure.step_left_right)

    def check_left_border(self, direction):
        for i in self.obj_figure:
            i: Square
            if i.get_x() + direction < Field.LEFT_BORDER:
                return False
        return True

    def check_right_border(self, direction):
        for i in self.obj_figure:
            i: Square
            if i.get_x() + direction > Field.RIGHT_BORDER:
                return False
        return True

    def move_obj(self, direction):
        for i in self.obj_figure:
            i: Square
            i.move(dx=direction, dy=0)
        self.change_matrix_left_right(value=+1 if direction > 0 else -1)

    def change_matrix_left_right(self, value):
        self.position_matrix['row'] += value

    # endregion
    """логика поворота фигуры"""

    # region
    def rotate(self, event=None):
        next_position = self.check_index_position()

        if self.try_rotate():
            self.obj_figure.clear()
            self.obj_figure = self.obj_figure_next.copy()
            self.number_position = next_position

    def try_rotate(self):
        old_matrix = self.position_matrix.copy()
        next_matrix = constants.FIGURES[self.name_figure][self.number_position]
        self.obj_figure_next.clear()

        for row in next_matrix:
            for part in row:
                if part == 1 and self.part_field() is not None:
                    x = Square(win=self.win, x=self.part_field().get_x(), y=self.part_field().get_y(),
                               row=self.position_matrix['row'], column=self.position_matrix['column'],
                               color=self.color_figure)
                    self.obj_figure_next.append(x)
                elif part == 1 and self.part_field() is None:
                    self.position_matrix = old_matrix
                    self.obj_figure_next.clear()
                    return None

                self.position_matrix['row'] += 1
            self.position_matrix['row'] = old_matrix['row']
            self.position_matrix['column'] += 1
        self.position_matrix = old_matrix

        return True

    def part_field(self):
        return Field.set_place(start_place=list(self.position_matrix.values()))

    def check_index_position(self):
        count_position = len(list(constants.FIGURES[self.name_figure])) - 1
        next_position = self.number_position

        if next_position >= count_position:
            next_position = 0
        else:
            next_position += 1
        return next_position
