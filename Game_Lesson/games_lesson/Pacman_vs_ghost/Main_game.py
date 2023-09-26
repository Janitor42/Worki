import wrap
import time
import random
from wrap import sprite
from random import randint, choice, randrange
import Shoot_towers
import Towers
import Enemies

wrap.world.create_world(1500, 900)
wrap.world.set_back_color(105, 110, 110)


"""Рамки экрана"""
line1=sprite.add('pacman',500,700,'dot')
line2=sprite.add('pacman',300,800,'dot')
line3=sprite.add('pacman',700,800,'dot')
sprite.set_height(line2,200)
sprite.set_height(line3,200)
sprite.set_width(line1,1000)
coins=sprite.add_text('You points '+str(Towers.points),780,750)
"""Трубы"""
pine = []
def create_pines():
    for i in range(0, 500, 83):
        pine.append(sprite.add('mario-items', 30, i + 100, 'pipe'))
        sprite.set_angle(pine[-1], 180)
    Towers.add_clouds()
create_pines()
"""Сознание башен"""
Towers.create_tower('sun',Towers.towers_on_the_shop)
Towers.create_tower('mushroom',Towers.towers_on_the_shop)
Towers.create_tower('star',Towers.towers_on_the_shop)
Towers.create_tower('plain',Towers.towers_on_the_shop)
Towers.create_tower('head',Towers.towers_on_the_shop)

"""Прочее"""
target = sprite.add('pacman', 0, 0, 'dot')
text_sprite=sprite.add_text('0',500,500,False)
button_l=True

"""Текстовые спрайты"""
name_text=sprite.add_text('Name',450,720,)
price_name=sprite.add_text('None',500,720,)
texts={'Xp': 'None','Speed':'None','Power':'None'}
text_l=[]

y=780
for i in texts:
    text_l.append(sprite.add_text(i,440,y))
    y+=40

price_xp=sprite.add_text('0',600,780)
price_speed=sprite.add_text('0',600,820)
price_power=sprite.add_text('0',600,860)
expl_text=sprite.add_text('None',150,820)


"""Все что относиться к сцене"""
scene_count=1
scene=sprite.add_text('Wave '+str(scene_count),400,400,text_color=(255,0,0),font_size=80,bold=True,font_name='Comic Sans MS')
wait_scene=True
long_wave=150


"""Враги"""
enemies=[]

def create_enemies():
    if len(enemies) < 1:
        for i in range(1, long_wave):
            enemies.append(Enemies.create())


@wrap.on_mouse_move()
def mouse_move(pos_x, pos_y):
    sprite.move_to(target, pos_x, pos_y)
    if Towers.this_tower['Hand'] is True:
        sprite.move_to(Towers.this_tower['this_tower'],sprite.get_x(target),sprite.get_y(target))
    Towers.backlight_three(target,price_xp,price_speed,price_power)
    Towers.explan(target,expl_text)

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def button_left():
    global wait_scene
    wait_scene=False
    global button_l
    Towers.collide(Towers.towers_on_the_shop,target)
    Towers.test_pos(Towers.clouds)
    Towers.test_clouds()
    button_l = not button_l
    Towers.buy_upgrade(target,price_xp,button_l,price_speed,price_power,coins)
@wrap.on_mouse_down(wrap.BUTTON_RIGHT)
def button_right():
    Towers.selections(target)

def next_wave():
    global long_wave, wait_scene, scene_count
    long_wave += 4
    scene_count += 1
    wrap.sprite_text.set_text(scene, 'Wave ' + str(scene_count))
    wait_scene = True
    sprite.show(scene)
    for i in Towers.towers_on_the_game:
        sprite.hide(i['Name'])
    Towers.towers_on_the_game.clear()
    for i in Shoot_towers.bullet_list:
        sprite.hide(i['Name'])
    Shoot_towers.bullet_list.clear()
    for i in pine:
        sprite.hide(i)
        pine.clear()
    create_pines()
    Enemies.place_start_enemies_x=900



@wrap.always(15)
def game():

    if wait_scene==True:
        create_enemies()
        wrap.sprite.set_angle(scene, sprite.get_angle(scene) + 1)
    if wait_scene==False:
        sprite.hide(scene)
        Shoot_towers.make_actions(coins)
        Shoot_towers.move_bullets()
        Shoot_towers.collisions_enemies(enemies)
        Towers.looks_settings_tower(price_xp,price_speed,price_power,price_name)
        Enemies.move_enemies(enemies)
    if len(enemies)<1:
        next_wave()







import wrap_py
wrap_py.app.start()
