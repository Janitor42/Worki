import random
import time
import wrap
from wrap import sprite,sprite_text,world

line_right=0
line_left=0
line3=0

def create_border():
    global line3,line_left,line_right
    line_right = sprite.add('pacman', 310, 300, 'dot')
    line_left= sprite.add('pacman', 1, 300, 'dot')
    line3= sprite.add('pacman', 150, 610, 'dot')
    sprite.set_height(line_right, 630)
    sprite.set_height(line_left, 630)
    sprite.set_width(line3, 320)
    sprite.set_height(line3,10)

