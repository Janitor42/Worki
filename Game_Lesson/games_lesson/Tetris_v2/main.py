import wrap
from wrap import world

import field
import figure
import menu

world.create_world(800, 612)
menu.create_border()

this = figure.Figure()
they = field.Field()


@wrap.on_key_down(wrap.K_w)
def turn():
    this.Turn(they.work_fields)


@wrap.on_key_down(wrap.K_a)
def left():
    this.left(they.work_fields)


@wrap.on_key_down(wrap.K_d)
def right():
    this.right(they.work_fields)


@wrap.on_key_down(wrap.K_s)
def down():
    this.down()


@wrap.always(40)
def game():
    this.move_figure(they.work_fields)
    they.add_field(this)
    this.remove_figure_and_add_up()
    they.rewrite_and_work_fields(this.check)


import wrap_py
wrap_py.app.start()
