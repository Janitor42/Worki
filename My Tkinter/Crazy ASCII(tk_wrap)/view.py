import model
import tkinter as tk
import wrap
import gui

wrap.world.create_world(model.screen_x, model.screen_y,
                        100, 100)


def redraw():
    gui.a.set(f'Now we see {len(model.all_sym)} letters')


