import tkinter as tk
import constants


class Field:

    all_fields = []
    all_fields_to_pos = {}


    # region Методы класса (фабричные методы)
    @classmethod
    def make_field(cls, win):
        y = 620
        column = 23
        place = 1
        for i in range(23):
            y -= 26
            x = 120

            row = 1

            for j in range(10):
                Field(win=win, x=x, y=y, row=row, column=column, place=place)
                place += 1
                x += 26
                row += 1
            column -= 1

    @classmethod
    def record_field(cls, square):
        for field in reversed(cls.all_fields):
            field: Field

            if field.get_pos() == square.get_pos():
                field.show_play_block(color=square.label['background'])


    @classmethod
    def get_position(cls, place):
        for part in Field.all_fields:
            part: Field

            if part.get_pos() == place and not part.get_state():
                return part
        return None

    # endregion

    # region Логика заполнения строк
    @classmethod
    def action_field(cls):
        y = constants.Y_LAST_FIELD
        count = 0
        full_column = []

        y_full = []
        for field in reversed(cls.all_fields):
            field: Field
            my_y = field.get_y()

            if my_y != y:
                y = my_y
                count = 0
                full_column.clear()

            if not field.get_state():
                full_column.append(field)
                count += 1

            if count == 10:
                y_full.append(y)
                cls.destroy_full_column(full_column=full_column)
                full_column.clear()

        if y_full:
            cls.move_fields_down(y_full=y_full)

    # endregion

    # region Перемещение полей
    @classmethod
    def move_fields_down(cls, y_full):
        direction = len(y_full) * constants.STEP
        y_lower = y_full[0]

        new_field = {}
        for field in reversed(cls.all_fields):
            field: Field

            if y_lower > field.get_y() and not field.get_state():
                new_x = field.get_x()
                new_y = field.get_y() + direction
                new_color = field.play_block['background']
                field.hide_play_block()

                new_field[f'{new_x}{new_y}'] = new_color

        for field in cls.all_fields:
            field: Field

            str_pos = f'{field.get_x()}{field.get_y()}'
            if str_pos in new_field:
                color = new_field[str_pos]
                obj: Field

                field.aaa(color=color)

    @classmethod
    def destroy_full_column(cls, full_column):
        for field in full_column:
            field: Field
            field.hide_play_block()

    @classmethod
    def down_all_field(cls, full_column):
        direction = len(full_column) * constants.STEP
        down_y = full_column[0]

    # endregion

    # region Инициализация экземпляра
    def __init__(self, win, x, y, row, column, place):
        self.win = win

        self.state = True
        self.row = row
        self.column = column
        self.x = x
        self.y = y
        self.row_column = [row, column]
        self.place = place

        self.play_block = tk.Label(win, text=f"", font=("Arial", 10),
                                   background="blue4",
                                   height=1, width=2)
        self.play_block.place_forget()

        self.field_block = tk.Label(win, text=f"", background="azure4",
                                    foreground="white", font=("Arial", 10),
                                    height=1, width=2)
        self.field_block.place(x=self.x, y=self.y)

        Field.all_fields.append(self)
        Field.all_fields_to_pos[f'{self.x}{self.y}'] = self

    # endregion

    # region Геттеры
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_pos(self):
        return [self.x, self.y]

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def get_state(self):
        return self.state

    # endregion

    # region Управление блоками
    def show_play_block(self, color='red'):
        self.change_state()
        self.play_block.config(background=color)
        self.play_block.place(x=self.x, y=self.y)
        self.play_block.lift()

    def hide_play_block(self):
        self.change_state()
        self.play_block.place_forget()

    def aaa(self, color):
        self.state = False
        self.play_block.config(background=color)
        self.play_block.place(x=self.x, y=self.y)
        self.play_block.lift()

    # endregion

    # region Вспомогательные методы
    def say(self):
        print(self.__dict__)

    def change_state(self):
        self.state = not self.state
        return self.state
    # endregion
