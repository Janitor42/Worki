import wrap
import blocks
import balls
import screen_wrap
import level
import finance
import screen_tk


def giv_money():
    finance.Finance.money -= 100#сколько денег стоит шар (каждый по разному)
    screen_tk.all_tk.label_money['text']=f'$\n{finance.Finance.money}'

def redraw_text(all_damage):
    screen_tk.all_tk.label_damage['text'] = f'Bricks damage \n{all_damage}'
    screen_tk.all_tk.label_money['text']=f'$\n{finance.Finance.money}'


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def click(pos_x, pos_y):
    for i in blocks.Block.all_blocks:
        if wrap.sprite.is_collide_point(i.name, pos_x, pos_y, use_rect=True):
            print(i.name)


@wrap.on_key_down(wrap.K_UP)
def add():
    balls.Balls(screen_wrap.x // 2, screen_wrap.y // 2)


@wrap.always(20)
def game():
    for i in balls.Balls.all_balls:
        i.move()

    for i in blocks.Block.all_blocks:
        i.remove_block()

    level.check_level()
    # print(len(blocks.Block.all_blocks))
