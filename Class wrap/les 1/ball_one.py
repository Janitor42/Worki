import wrap

from wrap import sprite as sp
from random import randint as rd
class Ball:
    def __init__(self):
        sp.add('pacman',rd(10,490),rd(10,490),'player3')