import random
import time
import wrap
from wrap import sprite,sprite_text,world

line1=0
line2=0
line3=0

def create_border():
    global line3,line2,line1
    line1 = sprite.add('pacman', 310, 300, 'dot')
    line2= sprite.add('pacman', 1, 300, 'dot')
    line3= sprite.add('pacman', 150, 610, 'dot')
    sprite.set_height(line1, 630)
    sprite.set_height(line2, 630)
    sprite.set_width(line3, 320)
    borders=[line1,line2,line3]


