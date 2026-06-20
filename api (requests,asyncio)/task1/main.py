# В основном потоке запустите wrap в дополнительном же tk
# на экране wrap летает и отбивается 1 шарик
# на экране тк ведется статистика по шарику - сколько раз столкнулся с каждой из стен

# *** шариков 25 и статистик тоже 25
# *** вырубая окно тк ничего не ломается
# ***** вырубая окно wrap тоже ничего не ломается шариков нет а счет идет дальше

import threading

import wrap
from wrap import world

import ball
import gui_tk

win = world.create_world(500, 500)
world.set_back_color(100, 200, 100)

ball.make_balls(35)


@wrap.always(5)
def action():
    for i in ball.balls:
        i.change_position()


thread = threading.Thread(target=gui_tk.create_gui_tk, daemon=True, args=(ball.balls,))
thread.start()

import wrap_py

wrap_py.app.start()
