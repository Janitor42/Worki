import inspect
import random
import time
import wrap
from wrap import sprite
import logic_tic_tac_toe

wrap.world.create_world(600, 600)
wrap.world.set_back_color(105, 110, 110)

field = []
player = []
computer = []
picture = []
logic_tic_tac_toe.create_field('pacman', 200, 200, field)


score_player=sprite.add_text('Your score 0',150,100,font_size=40)
score_computer=sprite.add_text('Him score 0',400,500,font_size=40)


hand = False
@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def click():
    global hand
    hand = not hand


@wrap.always()
def action(pos_x, pos_y):
    global hand
    if logic_tic_tac_toe.game_match:

        logic_tic_tac_toe.run_player(field, pos_x, pos_y, player, picture,hand)
        logic_tic_tac_toe.checks(player)

        logic_tic_tac_toe.run_computer(field, computer, picture)
        logic_tic_tac_toe.checks(computer)
        hand = False
    else:
        logic_tic_tac_toe.who_win(player,score_player,score_computer,computer)
        logic_tic_tac_toe.reset_all(picture, player, computer, field)
        logic_tic_tac_toe.create_field('pacman', 200, 200, field)



import wrap_py
wrap_py.app.start()
