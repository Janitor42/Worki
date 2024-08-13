import model
import random as rd
import wrap
import character as ch

def clear_all_letters():
    model.clear_all_letters()

def add_one_letter():
    model.add_new_letter()

def add_five_letter():
    model.add_new_letter()

def add_twenty_five_letter():
    model.add_new_letter()

@wrap.on_key_always(wrap.K_UP)
def add_new():
    model.add_new_letter()




@wrap.on_key_up(wrap.K_SPACE)
def pause_scene():
    model.pause = not model.pause


@wrap.always(10)
def actions():
    model.move_all_letters_on_screen()

