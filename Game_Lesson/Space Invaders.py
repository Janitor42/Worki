import time
import wrap
from wrap import sprite,sprite_text
import random
wrap.world.create_world(500,500)


# region
#создание врагов
enemy_list=[]
enemy_name=["enemy_blue_down1","enemy_blue_down1","enemy_yellow_down1","enemy_pink_down1","enemy_red_down1"]
position_enemy_x=50
position_enemy_y=200
proportions= 30
count=0
for g in range(len(enemy_name)):
    for i in range(10):
        enemy_list.append(sprite.add("pacman",position_enemy_x,position_enemy_y,enemy_name[g]))
        sprite.set_height_proportionally(enemy_list[count],proportions)
        count+=1
        position_enemy_x+=40
        if count==20:
            proportions=25
        elif count==30:
            proportions=23
    position_enemy_y-=30
    position_enemy_x=50
#скорось движение врагов
direction=2

# endregion

#Создание игрока
player = sprite.add('pacman',250,450,'player2')
sprite.set_angle(player,0)
speed_player=20

#Пуля
bullet= sprite.add("pacman",sprite.get_x(player),sprite.get_y(player),"dot",False)
sprite.set_height(bullet,15)

#Счет и его методы расчета
sprite.add_text("Score ",30,20,text_color=(255,255,255))
score=0
score_text=sprite.add_text(str(score),100,20,text_color=(255,255,255))
def calculation_score():
    global score
    if sprite.is_collide_any_sprite(bullet,enemy_list)<=19:
        score=score+5
        sprite_text.set_text(score_text, str(score))
    elif 29>=sprite.is_collide_any_sprite(bullet,enemy_list)>19:
        score = score + 10
        sprite_text.set_text(score_text, str(score))
    elif 39>=sprite.is_collide_any_sprite(bullet,enemy_list)>29:
        score = score + 15
        sprite_text.set_text(score_text, str(score))
    else:
        score = score + 30
        sprite_text.set_text(score_text, str(score))
#Управление игроком
# region
@wrap.on_key_always(wrap.K_a)
def go_right():
    sprite.move(player,-speed_player, 0)
@wrap.on_key_always(wrap.K_d)
def go_right():
    sprite.move(player, speed_player, 0)

@wrap.on_key_down(wrap.K_SPACE)
def show_bullet():
    sprite.show(bullet)
# endregion

"""Работа с врагами"""
@wrap.always(50)
def move():
    global direction,select_costume
    height=0
    #касание левой или правой границы экрана
    for i in range(len(enemy_list)):
        if sprite.get_x(enemy_list[i]) >= 480:
            direction = -direction
            height=4
            break
        elif sprite.get_x(enemy_list[i]) <= 20:
            direction = abs(direction)
            height=4
            break
#Перемещение списка врагов по экрану
    for i in range(len(enemy_list)):
        sprite.move(enemy_list[i], direction, height)
        #Работа с костумами (движение)
        if sprite.get_costume(enemy_list[i]) == "enemy_blue_down1" or sprite.get_costume(
            enemy_list[i]) == "enemy_yellow_down1" \
            or sprite.get_costume(enemy_list[i]) == "enemy_pink_down1" or sprite.get_costume(
            enemy_list[i]) == "enemy_red_down1":

            sprite.set_costume_next(enemy_list[i])
        else:
            sprite.set_costume_prev(enemy_list[i])

"""Работа с пулей"""
@wrap.always(7)
def move_bullet():
    global direction
    #Полет пули
    if sprite.is_visible(bullet)==True:
        sprite.move(bullet,0,-5)
        #Пуля достигает y = 0
        if sprite.get_y(bullet)<=0:
            sprite.move_to(bullet,sprite.get_x(player),sprite.get_y(player))
            sprite.hide(bullet)
        #Удаление элемента списка, перемещение пули, прячем пулю до след выстрела
        if sprite.is_collide_any_sprite(bullet,enemy_list)!=None:
            calculation_score()
            sprite.hide(sprite.is_collide_any_sprite(bullet,enemy_list))
            enemy_list.remove(sprite.is_collide_any_sprite(bullet,enemy_list))
            sprite.move_to(bullet,sprite.get_x(player), sprite.get_y(player))
            sprite.hide(bullet)
            #Увеличение скорости врага
            if direction>0:
                direction=direction+0.25
            else:
                direction=direction-0.25
    else:
            #Пуля всегда двигается за игроком (когда не летит)
            sprite.move_to(bullet, sprite.get_x(player), sprite.get_y(player))


import wrap_py
wrap_py.app.start()


