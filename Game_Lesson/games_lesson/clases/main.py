import wrap
from wrap import sprite, sprite_text
import random
import shar

wrap.world.create_world(800, 500)
wrap.world.set_back_color(105,110,110)


shariki=[]
a=shar.Shar(200,200,50,shariki)
# a.add_five()
q=shar.Shar(100,100,100,shariki)
w=shar.Shar(100,100,100,shariki)
q.b=100
q.add_five()
shariki+=[a,q,w]

@wrap.always(25)
def game():
    for i in shariki:
        i.go()

#pygame - создание окна
#работа с прямоугольниками
#работа с картинкой
#работа с событиями 

import wrap_py
wrap_py.app.start()
