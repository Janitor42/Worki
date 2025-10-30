import random
import wrap
import ball_two
from wrap import sprite as sp
from random import randint as rd

# При создании шарика мы указываем где будет его центр+
# Любой шарик который мы создали летит вправо+
# При создании мы можем указывать скорость по x и y+
# Добавить команду которая позволит заменить скорость у существующего шарика при касании его мышкой и левый щелчок

wrap.world.create_world(500, 500)
all_balls = []

@wrap.on_key_down(wrap.K_RIGHT)
def create_customized_ball():
    all_balls.append(ball_two.Ball(speed_x=rd(-5,5),speed_y=rd(5,5),x=rd(10,470),y=rd(10,470)))


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def button_left(pos_x, pos_y):
    for i in all_balls:
        if sp.is_collide_point(i.name, pos_x, pos_y):
            i.change_speed_ball(speed_x=rd(-5,5),speed_y=rd(-5,5))




@wrap.always(50)
def act():
    move_all()

def move_all():
    for i in all_balls:
        i.move_standard()

import wrap_py

wrap_py.app.start()
