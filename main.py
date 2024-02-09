import random
from wrap import sprite
import wrap
import wrap_py
import random

width = 600
long = 800
wrap.world.create_world(width, long)
wrap.world.set_back_color(25, 25, 112)


moving_platform = sprite.add("mario-items", 300, 750, "moving_platform3")

name = ["enemy_blue_down1", "enemy_ill_blue1", "enemy_ill_white1", "enemy_pink_down2", "enemy_red_down1"]




value = 20
y=100
print(value)
def row(min_long,max_long,costume,x):
    global y
    if min_long<=i<=max_long:
        sprite.add('pacman',x,y,name[costume])
        y+=30
    if i==4 or i ==9 or i == 17 or i == 23:
        y=100


for i in range(value):
    row(min_long=0,max_long=4,costume=0,x=100)
    row(min_long=4,max_long=9,costume=1,x=140)
    row(min_long=11, max_long=16, costume=2, x=180)
    row(min_long=17, max_long=23, costume=4, x=260)






import wrap_py

wrap_py.app.start()