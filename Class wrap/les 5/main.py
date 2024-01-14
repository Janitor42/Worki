import random
import wrap
import square_five
import ball_five
import star
import time
from wrap import sprite as sp
from random import randint as rd


win_x = 800
win_y = 800

wrap.world.create_world(win_x, win_y)
wrap.world.set_back_color(255, 255, 255)

all_square = []

def rd_not_zero(min, max):
    return random.choice([i for i in range(min, max + 1) if i != 0])

@wrap.on_key_down()
def create_square():
    all_square.append(square_five.Square(size=200,
                                         x=rd(50, win_x-50),
                                         y=rd(50, win_y-50),
                                         count_ball=rd(2, 5),
                                         list_square=all_square))


@wrap.always(15)
def act():
    for i in all_square:
        i.move_all()



import wrap_py
wrap_py.app.start()
