import wrap
import blocks
import ball
import level
import hand


import frame_main
@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def click(pos_x, pos_y):
    for i in blocks.Block.all_blocks:
        if wrap.sprite.is_collide_point(i.name, pos_x, pos_y, use_rect=True):
            i.change_block(hand.Hand.power)


@wrap.always(20)
def game():
    for i in ball.Ball.all_balls:
        i.move()
        i.effects()

    for i in blocks.Block.all_blocks:
        i.remove_block()

    level.check_level()
