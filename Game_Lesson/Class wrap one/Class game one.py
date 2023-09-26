import wrap
import ball
from wrap import sprite

wrap.world.create_world(500,500)
wrap.world.set_back_color(100,100,100)
# platform = sprite.add("mario-items", 30, 420, "moving_platform2")
# target = sprite.add("mario-items",250,50,"coin")


b= ball.Ball(3,100,100)
b.add_five()
print(b)

c=ball.Ball(7,200,200)

c.add_five()
c.add(10)
print(c)

@wrap.always()
def goo():
    b.goo()
    c.goo()

import wrap_py
wrap_py.app.start()
