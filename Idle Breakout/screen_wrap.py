import threading

import wrap


x = 750
y = 500

wrap.world.create_world(x, y,600,300)
wrap.world.set_back_color(180, 185, 212)


from threading import Lock

lock=threading.Lock()#todo почитать
