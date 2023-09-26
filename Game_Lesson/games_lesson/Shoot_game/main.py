import wrap
from wrap import sprite
import random
import enemieS
import playeR

wrap.world.create_world(800, 500)
wrap.world.set_back_color(105,110,110)
window = sprite.add("pacman", 600, 250, 'dot')
sprite.set_height(window, 500)
# Player
# region
player = sprite.add('pacman', 250, 450, 'player2')
hp_value=100
angle_player=0
player_hp=sprite.add_text(str(hp_value),sprite.get_x(player),sprite.get_y(player)+5,
                          font_size=20,bold=True,font_name="PostalShrift",text_color=(255,0,0))
target_player_1 = sprite.add("pacman", 0, 0, 'dot')
target_player_2 = sprite.add("pacman", 0, 0, 'dot', False)
sprite.set_height_proportionally(target_player_1, 5)
sprite.set_height_proportionally(target_player_2, 10)
sprite.set_angle(player, 0)
speed_player = 20
# endregion

# bullets
# region
bullets = []
pistols = False
machines = False
fractions = False
speed_bullets = 7
# endregion

# enemies
# region
dict_enemies={}
speed_enemies=5
waves=14
enemies=[]
# endregion

"""Поведение врагов"""
"""Волны?"""
#region
@wrap.always(50)
def move_enemies():
    global enemies
    for friend in enemies:
        enemieS.move_to_sprite(player, friend, enemies)
def wave(add):
    for i in range(0, add):
        enemies.append(enemieS.create(random.randint(3, 6)))
    enemieS.l=40
    enemieS.h=300
@wrap.always(10)
def shoots():
    global waves,hp_value
    for bullet in bullets:
        sprite.move_at_angle_dir(bullet, speed_bullets_func())
        if sprite.get_y(bullet) < 0 or sprite.get_y(bullet) > 500 or sprite.get_x(bullet) < 0 or sprite.get_x(bullet) > 600:
            sprite.hide(bullet)
            bullets.remove(bullet)
        enemieS.collision_enemie(enemies, bullet, bullets)
    if len(enemies)<1:
        wave(waves)
        waves+=14
    hp_value= playeR.damage_player(enemies, player, player_hp, hp_value)
    # if hp_value<=50:
    #     exit(0)

# endregion
"""Кнопки смены оружия"""
# region
@wrap.on_key_down(wrap.K_1)
def change():
    global machines, pistols, fractions
    pistols = True
    machines, fractions = False, False
@wrap.on_key_down(wrap.K_2)
def change():
    global machines, pistols, fractions
    machines = True
    pistols, fractions = False, False
@wrap.on_key_down(wrap.K_3)
def change():
    global machines, pistols, fractions
    fractions = True
    pistols, machines = False, False
# endregion
"""Управление прицелом"""
# region
@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def move_to_me():
    sprite.show(target_player_2)
@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def not_move_to_me():
    sprite.hide(target_player_2)
@wrap.on_mouse_move()
def calc_move(pos_x, pos_y):
    sprite.move_to(target_player_1, pos_x, pos_y)
    sprite.move_to(target_player_2, pos_x, pos_y)
@wrap.always(5)
def target():
    global angle_player,hp_value
    angle_player=sprite.get_angle(player)
    playeR.hp_move_to_player(player_hp, player, angle_player)
    if sprite.is_visible(target_player_2):
        wrap.sprite.set_angle_to_point(player, sprite.get_x(target_player_1), sprite.get_y(target_player_1))
# endregion
"""Клавиши управления"""
# region
@wrap.on_key_always(wrap.K_w)
def move_up():
    sprite.move(player, 0, -5)
@wrap.on_key_always(wrap.K_s)
def move_up():
    sprite.move(player, 0, 5)
@wrap.on_key_always(wrap.K_a)
def move_up():
    sprite.move(player, -5, 0)
@wrap.on_key_always(wrap.K_d)
def move_up():
    sprite.move(player, 5, 0)
#endregion
"""Поведение оружия"""
# region
@wrap.on_key_always(wrap.K_SPACE, delay=350)
def pistol():
    if pistols == True:
        bullets.append(sprite.add("pacman", 0, 0, 'dot'))
        sprite.move_to(bullets[-1], sprite.get_x(player), sprite.get_y(player))
        sprite.set_angle(bullets[-1], random_angle(4))
@wrap.on_key_always(wrap.K_SPACE, delay=100)
def machine():
    if machines == True:
        bullets.append(sprite.add("pacman", 0, 0, 'dot'))
        sprite.move_to(bullets[-1], sprite.get_x(player), sprite.get_y(player))
        sprite.set_angle(bullets[-1], random_angle(40))
@wrap.on_key_always(wrap.K_SPACE, delay=2000)
def fractions():
    if fractions == True:
        for i in range(30):
            bullets.append(sprite.add("pacman", 0, 0, 'dot'))
            sprite.set_angle(bullets[-1], random_angle(15))
            sprite.move_to(bullets[-1], sprite.get_x(player), sprite.get_y(player))
def random_angle(x):
    a = sprite.get_angle(player) - x
    b = sprite.get_angle(player) + x
    rand = random.randint(int(a), int(b))
    return rand
def speed_bullets_func():
    if pistols or machines:
        speed_bullets = 7
    else:
        speed_bullets = 7
    return speed_bullets

# endregion

import wrap_py
wrap_py.app.start()
