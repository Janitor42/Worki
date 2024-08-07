import wrap
import random as rd
# import string as st
from wrap import sprite as sp
import character as ch
import tkinter as tk
from threading import Thread
import test
import model

# буквы и знаки летают вращаются и отбиваются по экрану, потом эффекты, все через классы



wrap.world.create_world(model.screen_x, model.screen_y)
text_name = sp.add_text(f'Now we are watching  0 symbols', 180, 10, text_color=(255, 255, 255))



def clear_all():
    model.all_sym.clear()


def rd_not_zero(mini, maxi):
    return rd.choice([i for i in range(mini, maxi + 1) if i != 0])


@wrap.on_key_always(wrap.K_UP)
def add_new():
    if len(model.all_sym) < 200:
        model.all_sym.append(ch.Character(
            speed_x=rd_not_zero(-5, 5),
            speed_y=rd_not_zero(-5, 5)))


@wrap.on_key_always(wrap.K_DOWN)
def add_new():
    if len(model.all_sym) > 0:
        model.all_sym.remove(rd.choice(model.all_sym))


@wrap.on_key_up(wrap.K_SPACE)
def pause_scene():
    model.pause = not model.pause


@wrap.always(10)
def actions():
    if not model.pause:
        wrap.sprite_text.set_text(text_name, f'Now we are watching  {ch.Character.count} symbols')
        ch.Character.move_all(model.all_sym)


Thread(target=test.create_tk).start()
import wrap_py

wrap_py.app.start()
