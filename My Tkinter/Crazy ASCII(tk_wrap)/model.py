import random as rd
import tkinter as tk
import character as ch

import view





# main win
screen_x = 800
screen_y = 800

# character
all_sym = []



def move_all_letters_on_screen():
    if not pause:
        for i in all_sym:
            i.move()


def clear_all_letters():
    global var_letters, var_letters_tk
    all_sym.clear()
    view.redraw()




def add_new_letter():
    if len(all_sym) < 200:
        all_sym.append(ch.Character())
        view.redraw()


# gui
all_gui = None

# commands
pause = False
