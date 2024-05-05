import random
import wrap
import square_five
import ball_five
from random import randint as rd

win_x = 800
win_y = 800

wrap.world.create_world(win_x, win_y)
wrap.world.set_back_color(255, 255, 255)

all_square = []
all_balls = []
group=0

def rd_not_zero(min, max):
    return random.choice([i for i in range(min, max + 1) if i != 0])


@wrap.on_key_down()
def create_square():
    global group
    group+=1
    all_square.append(square_five.Square(size=200,
                                         x=rd(50, win_x - 50),
                                         y=rd(50, win_y - 50),
                                         list_square=all_square,
                                         list_balls=all_balls))
    rd_balls=rd(2,5)

    for i in range(rd_balls):
        all_balls.append(ball_five.Ball(x=all_square[-1].x, y=all_square[-1].y,
                                        speed_x=rd_not_zero(-3,3),
                                        speed_y=rd_not_zero(-3,3),
                                        size=rd(10,90)))



@wrap.always(15)
def act():

    #проверка и переопределение куда лететь
    for square in all_square:
        square.test()


        #просто полет шариков (по заданным координатам)
    for ball in all_balls:
        ball.move()


import wrap_py
wrap_py.app.start()
