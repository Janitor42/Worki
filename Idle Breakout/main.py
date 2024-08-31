import screen
import events
import level
import mouse
import ball
import gui
import blocks
import time

can = screen.can
win = screen.win

gui.Gui(win)

while True:
    # a = time.time()
    level.leveling()
    ball.live_ball()
    # blocks.check_collision()

    can.update()
    # print(a - time.time())
