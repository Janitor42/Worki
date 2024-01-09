import random
import wrap
import figure
import ball
import star
import time
from wrap import sprite as sp
from random import randint as rd

# На экране появляются 1 раз в секунду появляются звезды (звезда моргает (меняет размеры))+
# На звезде есть номер (номер указываем мы (от -5 до 5, 0 указать нельзя))+
# Когда шарик сталкивается со звездой, он ее поглощает звезда изчезает, шар меняет размер на число на звезде+
# Если размер шара стал 0 или меньше он изчезает
# Если размер стал больше 100 (шар делиться на 3 (они летят в разном направлении))

win_x = 500
win_y = 500

wrap.world.create_world(win_x, win_y)
wrap.world.set_back_color(255, 255, 255)

begin = time.time()
times_between = 1

all_balls = []
all_stars = []


def rd_not_zero(min, max):
    return random.choice([rd(1, max), rd(min, -1)])


def create_one_star():
    all_stars.append(star.Star(x=rd(50, 450), y=rd(50, 450), size=rd(20, 80),
                               number=rd(-20, -10)))


def slise_ball(x, y, size):
    for i in range(3):
        all_balls.append(ball.Ball(x=x, y=y, speed_x=rd_not_zero(-3, 3),
                                   speed_y=rd_not_zero(-3, 3), size=size // 3))


@wrap.on_key_down()
def create_ball_on_key():
    all_balls.append(ball.Ball(x=250, y=250, speed_x=rd_not_zero(-3, 3),
                               speed_y=rd_not_zero(-3, 3), size=rd(20, 80)))


@wrap.always(25)
def act():
    global begin

    for i in all_balls:
        i.move()
        i.collide(all_stars)
        if i.maybe_division():
            slise_ball(x=sp.get_x(i.name), y=sp.get_y(i.name), size=i.size)
            i.del_obj_ball()
            all_balls.remove(i)
        if i.size<=0:
            i.del_obj_ball()
            all_balls.remove(i)
            break



    if int(begin) + times_between <= int(time.time()):
        create_one_star()
        begin = time.time()

    for i in all_stars:
        i.light_star()
        if not i.live:
            i.del_obj_star()
            all_stars.remove(i)


import wrap_py

wrap_py.app.start()
