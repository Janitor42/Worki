import wrap
import blocks
import ball
import level
import hand
import creator_balls
import screen_wrap


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def click(pos_x, pos_y):
    for i in blocks.Block.all_blocks:
        if wrap.sprite.is_collide_point(i.name, pos_x, pos_y, use_rect=True):
            i.change_block(hand.Hand.power)



@wrap.on_key_down(wrap.K_UP)
def move_faster():
    for i in ball.Ball.all_balls:
        i.speed_time=0.001
    print(1111)

@wrap.always(20)
def game():
    for i in ball.Ball.all_balls:
        i.move()
        i.add_actions()

    for i in blocks.Block.all_blocks:
        i.remove_block()

    level.check_level()

    creator_balls.add_new_balls()
