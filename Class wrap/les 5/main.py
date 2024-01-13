import random
import wrap
import square_five
import ball_five
import star
import time
from wrap import sprite as sp
from random import randint as rd

# на экране должен быть квадрат шарики болтаются внутри квадрата+
# квадрат это класс+
# Можем сделать много таких квадратов, указываем коо-ты создания+
# указываем сколько шариков должно быть внутри него(при создании класса создаем кучу шариков в его границах)+

win_x = 500
win_y = 500

wrap.world.create_world(win_x, win_y)
wrap.world.set_back_color(255, 255, 255)

all_square = []

def rd_not_zero(min, max):
    return random.choice([i for i in range(min, max + 1) if i != 0])

@wrap.on_key_down()
def create_square():
    all_square.append(square_five.Square(size=rd(150, 250),
                                         x=rd(50, 450), y=rd(50, 450),
                                         count_ball=rd(2, 5)))

@wrap.always(15)
def act():
    for i in all_square:
        i.move_all()


import wrap_py
wrap_py.app.start()
