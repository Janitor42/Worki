import wrap
import random
from wrap import sprite as sp
from random import randint as rd

#сделать класс который называется шар
#Когда я создаю обьект этого класса - на экране появляется шарик
wrap.world.create_world(500,500)


class Ball:
    def __init__(self):
        sp.add('pacman',rd(10,490),rd(10,490),'player3')

@wrap.on_key_up()
def act():
    Ball()


import wrap_py
wrap_py.app.start()
