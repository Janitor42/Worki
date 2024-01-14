import wrap
from wrap import sprite as sp
from random import randint as rd
import random
import ball_five

win_x = 800
win_y = 800
wrap.add_sprite_dir("C:/Users/i'm/PycharmProjects/Worki/Class wrap/les 5")

save_size = 20


class Square:
    place = 1
    save_size = 20
    def __init__(self, size, x, y, count_ball, list_square):

        if self._find_place():
            self.min_save = Square.save_size
            self.max_save = self.min_save + 20
            Square.save_size += 20
        else:
            self.__x = x
            self.__y = y
            self.min_save = self.rd_randrange()
            self.max_save = self.min_save + 20

        self.list_square = list_square
        self.balls = []
        self.__size = size

        self.pos_x = []
        self.pos_y = []
        self.square_number=Square.place
        self.create_pos_square_in_win()
        self.__count_ball = count_ball
        self.__create_ball()

        self.name = sp.add('picture', self.__x, self.__y, costume='square_five')
        sp.set_width_proportionally(self.name, self.__size)

        self.name_setting = sp.add_text('шары от ' + str(self.min_save) + ' и до ' + str(self.max_save), self.__x,
                                        self.__y - 0.6 * self.__size)

        Square.place += 1

    def create_pos_square_in_win(self):
        self.pos_x.append((self.__x - self.__size // 2) + 40)
        self.pos_x.append((self.__x + self.__size // 2) - 40)
        self.pos_y.append((self.__y - self.__size // 2) + 40)
        self.pos_y.append((self.__y + self.__size // 2) - 40)

    def __create_ball(self):
        for i in range(self.__count_ball):
            self.balls.append(ball_five.Ball(x=self.__x, y=self.__y, speed_x=self.rd_not_zero(-3, 3),
                                             speed_y=self.rd_not_zero(-3, 3), size=rd(20, 99)))

    def move_all(self):
        for i in self.balls:
            i.check_window( self.name,self.max_save,self.min_save)
            i.move()








    def _find_place(self):
        if Square.place < 5:
            x = 200
            y = 200
            for i in range(1, 5):
                if Square.place == i:
                    if i == 2:
                        x = 500
                    elif i == 3:
                        y = 500
                    elif i == 4:
                        x, y = 450, 450
                    self.__x, self.__y = x, y
                    return True
        else:
            return False
    @staticmethod
    def rd_not_zero(min, max):
        return random.choice([i for i in range(min, max + 1) if i != 0])

    @staticmethod
    def rd_randrange():
        return random.randrange(20, 100, 20)
