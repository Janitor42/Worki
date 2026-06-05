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
        self.position_matrix = constants.START_POSITIONS[self.name_figure].copy()

        self.win.bind("<Left>", self.move_left)
        self.win.bind("<Right>", self.move_right)
        self.win.bind("<Up>", self.rotate)

        self.speed = 1
        self.offset = 0
        self.win.after(self.speed, self.fall)

    """методы set, get и т.д."""

    # region
    def set_offset(self, value):
        self.offset += value

    def get_offset(self):
        return self.offset

    def set_position_matrix_column(self, value):
        self.position_matrix['column'] += value

    # endregion

    """определение и создание фигуры"""

    # region
    def choice_figure(self):
        choice = 'O'  # rd.choice(list(constants.FIGURES))
        self.color_figure = constants.COLORS[choice]
        self.name_figure = choice
        row_column = constants.START_POSITIONS[self.name_figure]
        matrix_figure = constants.FIGURES[choice][self.number_position]
        return row_column, matrix_figure

    def install_figure(self, row_column, matrix_figure):
        place = row_column.copy()
        for row in matrix_figure:
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
            Square.change_row(self.obj_figure, -1)

    def move_right(self, event=None):
        if self.check_right_border(direction=Figure.step_left_right):
            self.move_obj(direction=Figure.step_left_right)
            Square.change_row(self.obj_figure, 1)

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
        if self.name_figure == 'O':
            return
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
                    x = Square(win=self.win, x=self.part_field().get_x(),
                               y=self.part_field().get_y() + self.get_offset(),
                               row=self.position_matrix['row'], column=self.position_matrix['column'],
                               color=self.color_figure)
                    x.place_on_field()
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

    # endregion

    """логика падения фигуры"""

    # region
    def fall(self):


        for i in self.obj_figure:
            i: Square
            i.move_down()
        self.place_figure(obj=self.obj_figure, num=1)
        if self.check_end(self.obj_figure):
            return
        self.win.after(self.speed, self.fall)

    def place_figure(self, obj, num):
        self.set_offset(num)
        if self.get_offset() == 26:
            Square.change_column(obj)
            self.set_position_matrix_column(1)
            self.set_offset(-26)

    def check_end(self, obj):
        for i in self.obj_figure:
            i: Square
            if i.get_column() == constants.MAX_COLUMN_FIELD:
                self.check(obj)
                return True
            column = i.get_column() + 1
            next_block = Field.find_field(i.get_row(), i.get_column() + 1)
            next_block: Field
            if next_block.state == "close":
                self.check(obj)
                return True

    def check(self, obj):
        self.record_figure(obj)
        Field.check_fill_columns()
        Figure(win=self.win)

    def record_figure(self, obj):
        for i in obj:
            block: Field
            block = Field.find_field(i.get_row(), i.get_column())
            block.play_square.config(background=i.color)
            block.state = "close"
            block.play_square.place(x=block.x, y=block.y)
            block.play_square.lift()
        obj.clear()
    # endregion
