import tkinter as tk
import random
import time


class Field:
    # ===================== КЛАССОВЫЕ АТРИБУТЫ =====================
    my_field = {}  # Словарь всех ячеек поля, где ключ - номер ячейки
    animate_speed = 0.004  # Скорость анимации перемещения
    collapse = False  # Флаг, были ли изменения на поле (падения или схлопывания)

    # ===================== КЛАССОВЫЕ МЕТОДЫ =====================
    # region Классовые методы

    @classmethod
    def find_place_down(cls, next_place_cube):
        obj_field = cls.my_field[next_place_cube]
        return obj_field

    @classmethod
    def rewrite_place(cls, obj_cube):
        number_on_desk = obj_cube.get_cube_place_on_desk()
        if number_on_desk >= 1:
            obj_field = cls.my_field[number_on_desk]
            obj_field.create_play_square(cube=obj_cube)

    @classmethod
    def fall_all_play_squares(cls):
        # Находим все занятые ячейки
        play_square = cls.find_all_play_squares()

        # Перебираем каждую занятую ячейку
        for obj_field in play_square:
            obj_field: Field

            # Номер ячейки снизу (текущий номер + 5, так как поле 5 колонок)
            place_down = obj_field.get_number_on_desk() + 5

            # Проверяем: существует ли ячейка снизу и свободна ли она
            if place_down in cls.my_field.keys() and cls.my_field[place_down].state == 'open':
                neighbor = cls.my_field[place_down]
                # Запускаем анимацию падения
                obj_field.animate_cube_to_cube(neighbor=neighbor)

                # Переносим значение в нижнюю ячейку
                neighbor.set_new_value(old_value=obj_field.play_square['text'])
                # Очищаем текущую ячейку
                obj_field.reset_play_square()
                Field.collapse = True
                # Рекурсивно продолжаем проверять падения (чтобы обработать цепочку падений)
                return cls.fall_all_play_squares()

        return False

    @classmethod
    def find_all_play_squares(cls):
        play_square = []

        # Перебираем все ячейки поля
        for im in cls.my_field:
            obj_field = cls.my_field[im]
            obj_field: Field
            # Если ячейка не открыта (занята) - добавляем в список
            if obj_field.get_state() != 'open':
                play_square.append(obj_field)

        return play_square

    @classmethod
    def connect_all_play_squares(cls):
        # Находим все занятые ячейки
        play_square = cls.find_all_play_squares()

        # Перебираем каждую занятую ячейку
        for obj_field in play_square:
            obj_field: Field

            # Находим соседей для текущей ячейки
            neighbors = Field.find_him_neighbors(obj_field.number_on_desk)
            # Проверяем, есть ли среди соседей ячейка с таким же значением
            if Field.check_him_neighbors(neighbors=neighbors, obj_field=obj_field):
                Field.collapse = True
                # Рекурсивно продолжаем проверять схлопывания (так как после схлопывания могут появиться новые комбинации)
                return Field.connect_all_play_squares()

        return False

    @staticmethod
    def find_him_neighbors(im):
        # ВНИМАНИЕ: Сложная логика определения соседей в зависимости от позиции на поле
        # Поле имеет нумерацию:
        # 1   2   3   4   5
        # 6   7   8   9   10
        # 11  12  13  14  15
        # 16  17  18  19  20
        # 21  22  23  24  25
        # 26  27  28  29  30

        # top side (номера 1-5) - верхний ряд, соседи только справа, слева и снизу
        if im <= 5:
            if im == 1:  # левый верхний угол - только справа и снизу
                return [im + 1, im + 5]
            elif im == 5:  # правый верхний угол - только слева и снизу
                return [im - 1, im + 5]
            else:  # верхний ряд, не углы - справа, слева и снизу
                return [im + 1, im - 1, im + 5]

        # right side (правый край) - номера 5,10,15,20,25,30
        elif im % 10 in [0, 5]:
            if im == 30:  # правый нижний угол - только слева и сверху
                return [im - 1, im - 5]
            # правый край, не углы - слева, сверху и снизу
            return [im + 5, im - 1, im - 5]

        # left side (левый край) - номера 1,6,11,16,21,26
        elif im % 10 in [6, 1]:
            if im == 26:  # левый нижний угол - только справа и сверху
                return [im + 1, im - 5]
            # левый край, не углы - справа, сверху и снизу
            return [im + 1, im + 5, im - 5]

        # default side (середина поля) - все остальные ячейки
        else:
            if im in [27, 28, 29]:  # нижний ряд, не углы - справа, слева и сверху (снизу нет)
                return [im + 1, im - 1, im - 5]
            # стандартная ячейка в середине - все 4 стороны
            return [im + 1, im + 5, im - 1, im - 5]

    @classmethod
    def check_him_neighbors(cls, neighbors, obj_field):
        # Перебираем всех соседей
        for number in neighbors:
            neighbor = cls.my_field[number]
            neighbor: Field

            # Если соседняя ячейка занята И значения совпадают
            if neighbor.get_state() != 'open' and obj_field.get_value() == neighbor.get_value():
                # Запускаем анимацию схлопывания (текущая ячейка перемещается в соседнюю)
                obj_field.animate_cube_to_cube(neighbor=neighbor)
                # Удваиваем значение в соседней ячейке
                neighbor.set_new_value()
                # Очищаем текущую ячейку
                obj_field.reset_play_square()
                return True

        return False

    # endregion

    # ===================== КОНСТРУКТОР =====================
    def __init__(self, screen, x, y, number):
        self.screen = screen

        self.number_on_desk = number  # Номер ячейки на поле (1-30)
        self.x = x  # Координата X на экране
        self.y = y  # Координата Y на экране
        self.pos = [x, y]  # Позиция для удобства

        self.state = "open"  # Состояние: open - свободно, close - занято

        # Подложка под игровой квадрат (визуальный элемент)
        self.label = tk.Label(self.screen, width=9, height=4)
        self.label.place(x=self.x, y=self.y)

        # Сам игровой квадрат (изначально скрыт)
        self.play_square = tk.Label(self.screen, width=7, height=3, font=('arial', 13))
        self.play_square.place_forget()

        self.animate_square = None  # Временный квадрат для анимации

        # Добавляем ячейку в общий словарь класса
        Field.my_field[self.number_on_desk] = self

    # ===================== SET МЕТОДЫ =====================
    # region set methods

    def create_play_square(self, cube):
        # Создает игровой квадрат в этой ячейке на основе падающего куба
        self.play_square.config(text=cube.cube['text'], background='yellow')
        self.play_square.place(x=cube.get_x(), y=cube.get_y())
        self.close_state()

    def close_state(self):
        # Делает ячейку занятой
        self.state = "close"

    def open_state(self):
        # Делает ячейку свободной
        self.state = 'open'

    def reset_play_square(self):
        # Очищает ячейку (убирает квадрат)
        self.open_state()
        self.play_square.config(text='')
        self.play_square.place_forget()

    def set_new_value(self, old_value=None):
        # Устанавливает новое значение для квадрата
        if self.play_square['text'] != '':
            # Если значение уже есть - удваиваем (схлопывание)
            self.play_square.config(text=int(self.play_square['text']) * 2)
        else:
            # Если значения нет - берем из old_value (падение)
            self.play_square.config(text=int(old_value))
            self.close_state()
            self.play_square.place(x=self.x, y=self.y)

    # endregion

    # ===================== GET МЕТОДЫ =====================
    # region get methods

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_pos(self):
        return [self.x, self.y]

    def get_number_on_desk(self):
        return self.number_on_desk

    def get_state(self):
        return self.state

    def get_value(self):
        return self.play_square['text']

    # endregion

    # ===================== АНИМАЦИЯ =====================
    # region Анимация

    def animate_cube_to_cube(self, neighbor):
        # ВНИМАНИЕ: Сложная логика анимации перемещения квадрата
        # Прячем оригинальный квадрат
        self.play_square.lower()

        # Создаем временный квадрат для анимации
        self.animate_square = tk.Label(self.screen, width=7, height=3,
                                       text=self.play_square['text'],
                                       font=('arial', 13), background=self.play_square['background'])

        # Размещаем его на месте оригинального
        self.animate_square.place(x=self.get_x(), y=self.get_y())

        self.screen.update_idletasks()

        # Засекаем время для контроля скорости анимации
        t_start = time.time()

        # Цикл анимации - пока временный квадрат не достигнет целевой позиции
        while [self.animate_square.winfo_x(), self.animate_square.winfo_y()] != neighbor.get_pos():
            t_run = time.time()
            # Двигаем только через определенные интервалы времени (для плавности)
            if t_run > t_start + Field.animate_speed:
                self.move_square_to_square(neighbor=neighbor)
                t_start = time.time()

            # Обновляем экран на каждой итерации
            self.screen.update()

        # Анимация завершена - удаляем временный квадрат и показываем оригинальный
        self.animate_square.destroy()
        self.play_square.lift()

    def move_square_to_square(self, neighbor):
        # ВНИМАНИЕ: Логика пошагового перемещения квадрата к цели
        neighbor: Field

        # Движение по вертикали
        if self.animate_square.winfo_y() > neighbor.get_y():
            # Если выше цели - двигаем вниз
            self.animate_square.place(x=self.animate_square.winfo_x(), y=self.animate_square.winfo_y() - 1)
        if self.animate_square.winfo_y() < neighbor.get_y():
            # Если ниже цели - двигаем вверх
            self.animate_square.place(x=self.animate_square.winfo_x(), y=self.animate_square.winfo_y() + 1)

        # Движение по горизонтали
        if self.animate_square.winfo_x() > neighbor.get_x():
            # Если правее цели - двигаем влево
            self.animate_square.place(x=self.animate_square.winfo_x() - 1, y=self.animate_square.winfo_y())
        if self.animate_square.winfo_x() < neighbor.get_x():
            # Если левее цели - двигаем вправо
            self.animate_square.place(x=self.animate_square.winfo_x() + 1, y=self.animate_square.winfo_y())

    # endregion


# ===================== ФУНКЦИЯ СОЗДАНИЯ ПОЛЯ =====================
def make_fields(screen):
    number = 0
    x = 0
    y = 0
    # Создаем поле 6 строк по 5 ячеек
    for i in range(6):
        x = 100  # Сброс X для новой строки
        y += 70  # Увеличиваем Y для новой строки
        for a in range(5):
            number += 1  # Увеличиваем номер ячейки
            Field(screen, x, y, number)
            x += 73  # Сдвиг по горизонтали для следующей ячейки