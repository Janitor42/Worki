import random
import time
import wrap
from wrap import sprite as sp
from wrap import sprite_text as sp_t
from random import randint as rd
import hero
import ground
import balls
win_x=600
win_y=800
wrap.world.create_world(win_x, win_y)

wall_block = ground.Ground()
player = hero.Hero()
ball=balls.Balls()

begin_time=time.time()

@wrap.always(15)
def game():
    ball.move_ball(wall_block)



@wrap.on_mouse_move()
def move_ship(pos_x):
    player.move(pos_x)




import wrap_py
wrap_py.app.start()
