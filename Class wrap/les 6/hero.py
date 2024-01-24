import random
import time
import wrap
from wrap import sprite as sp
from wrap import sprite_text as sp_t
from random import randint as rd

wrap.add_sprite_dir("C:/Users/i'm/PycharmProjects/Worki/Class wrap/les 6/images")

class Hero:
    def __init__(self):
        self.name=sp.add('ships',300,700,'spaceShips_001')


    def move(self,pos_x):
        sp.move_to(self.name,pos_x,700)