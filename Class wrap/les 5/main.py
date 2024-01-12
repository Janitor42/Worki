import random
import wrap
import square
import ball
import star
import time
from wrap import sprite as sp
from random import randint as rd

#на экране должен быть квадрат шарики болтаются внутри квадрата
#квадрат это класс
#Можем сделать много таких квадратов, указываем коо-ты создания
#указываем сколько шариков должно быть внутри него(при создании класса создаем кучу шариков в его границах)

win_x = 500
win_y = 500

wrap.world.create_world(win_x, win_y)
wrap.world.set_back_color(255, 255, 255)

begin = time.time()
times_between = 0.1

all_balls = []
all_stars = []
all_square = []

def rd_not_zero(min, max):
    return random.choice([i for i in range(min, max + 1) if i != 0])


def create_one_star():
    all_stars.append(star.Star(x=rd(50, 450), y=rd(50, 450), size=rd(20, 80),
                               number=rd(-20, 20),list_star=all_stars))

@wrap.on_key_down(wrap.K_UP)
def create_square():
    all_square.append(square.Square(100))


@wrap.on_key_down(wrap.K_DOWN)
def create_ball_on_key():
    all_balls.append(ball.Ball(x=250, y=250, speed_x=rd_not_zero(-3, 3),
                               speed_y=rd_not_zero(-3, 3), size=rd(20, 80),list_ball=all_balls))


@wrap.always(15)
def act():
    global begin

    for i in all_balls:
        i.move()
        i.collide(all_stars)


    if float(begin) + times_between <= float(time.time()):
        create_one_star()
        begin = time.time()


    for i in all_stars:
        i.light_and_remove_star(i)



import wrap_py

wrap_py.app.start()
