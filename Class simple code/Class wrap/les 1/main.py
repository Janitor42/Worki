import random
import wrap
import ball_one
from wrap import sprite as sp
from random import randint as rd




#сделать класс который называется шар
#Когда я создаю обьект этого класса - на экране появляется шарик

wrap.world.create_world(500,500)

@wrap.on_key_up()
def act():
    ball_one.Ball()



import wrap_py
wrap_py.app.start()