import random
import time
import wrap
from wrap import sprite,sprite_text,world
import menu
import object
import field


world.create_world(800,612)
menu.create_border()

this=object.Figure(1)
they=field.Field()


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

@wrap.always(50)
def game():
    this.Work_platform(they.work_fields)
    they.Add_field(this.names)
    this.Remove_figure_and_add_up()
    they.Remove_and_add_work_field()




import wrap_py
wrap_py.app.start()
