import random
import wrap
import ball_three
from wrap import sprite as sp
from random import randint as rd

# При создании шарика мы указываем где будет его центр+
# Любой шарик который мы создали летит вправо+
# При создании мы можем указывать скорость по x и y+
# Добавить команду которая позволит заменить скорость у существующего шарика+


wrap.world.create_world(500, 500)
all_balls = []
pause = False

@wrap.on_key_down(wrap.K_LEFT)
def create_simple_ball():
    all_balls.append(ball_three.Ball('easy'))


@wrap.on_key_down(wrap.K_RIGHT)
def create_customized_ball():
    global pause
    pause = True
    all_balls.append(ball_three.Ball('hard'))


@wrap.on_key_down(wrap.K_SPACE)
def play():
    global pause
    pause = False


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def button_left(pos_x, pos_y):
    global pause
    for i in all_balls:
        if sp.is_collide_point(i.name, pos_x, pos_y):
            pause = True
            i.change_speed_ball()
            pause=False


def move_all():
    for i in all_balls:
        i.move_standard()


@wrap.always(25)
def act():
    if not pause:
        move_all()


import wrap_py

wrap_py.app.start()
