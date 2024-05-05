import wrap
from wrap import sprite
import random


wrap.world.create_world(500, 500)
wrap.world.set_back_color(137, 193, 204)

# Препядствие игрока
let_1 = {}
let_2 = {}
def add_blocks(let, x):
    block_up = random.randint(20, 300)
    for i in range(-50, block_up, 30):
        let[i] = sprite.add("mario-items", x, i, "block_empty")
    for i in range(block_up + 150, 550, 30):
        let[i] = sprite.add("mario-items", x, i, "block_empty")
speed_let=-3

add_blocks(let_1, 1000)
add_blocks(let_2, 1350)

# Создание списков(трубы и песок) и размещение их на экране
imitation_line = {}
imitation_block = {}
x_pos_imitation_line = 0
for i in range(7):
    imitation_line[i] = sprite.add("mario-items", x_pos_imitation_line, 450, "moving_platform2")
    imitation_block[i] = sprite.add("battle_city_items", x_pos_imitation_line, 480, "block_snow")
    sprite.set_width(imitation_line[i], 100)
    sprite.set_width(imitation_block[i], 100)
    sprite.set_height(imitation_block[i], 50)
    x_pos_imitation_line = x_pos_imitation_line + 100
speed_imitation=-10

# Игрок
player = sprite.add("mario-1-big", 250, 250, "duck")
player_on_game = False
pos_x_player = 1
angle_mario = -3
angle_triger = True
speed_player=5
speed_click=-50


#Score
count=0
text_score=sprite.add_text(str(int(count)),250,100,font_size=50)
@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def start_game():
    global player_on_game, angle_triger
    sprite.move(player, 0, speed_click)
    player_on_game = True
    angle_triger = True


# Угол персонажа во время нажатия мышки
def change_angle():
    global angle_triger
    if sprite.get_angle(player) > 45 and angle_triger == True:
        sprite.set_angle(player, 45)
        if sprite.get_angle(player) < 50:
            angle_triger = False
    elif sprite.get_angle(player) < 180:
        sprite.set_angle(player, sprite.get_angle(player) + abs(angle_mario))


# функция проверяет пересоздает блоки за экраном
def func():
    for i in imitation_block:
        if sprite.get_x(imitation_line[i]) < -100:
            imitation_line[i] = sprite.add("mario-items", 590, 450, "moving_platform2")
            sprite.set_width(imitation_line[i], 100)
        if sprite.get_x(imitation_block[i]) < -100:
            imitation_block[i] = sprite.add("battle_city_items", 590, 480, "block_snow")
            sprite.set_width(imitation_block[i], 100)
            sprite.set_height(imitation_block[i], 50)

# Работа с движением удалением и новыми let
def actions_let(let, y_pos):
    for i in let:
        sprite.move(let[i], speed_let, 0)
        if sprite.get_x(let[i]) < 0:
            for i in let:
                sprite.hide(let[i])
            let.clear()
            break
    if let == {}:
        add_blocks(let, y_pos)

def collide ():
    if sprite.is_collide_all(player,let_1.values()) or sprite.is_collide_all(player,let_2.values())\
        or sprite.is_collide_all(player,imitation_line.values()) :
            stop_game()

@wrap.always(50)
# Имитация скорости движения по экрану
def imitation_moution():
    for i in imitation_line:
        sprite.move(imitation_line[i], speed_imitation, 0)
        sprite.move(imitation_block[i], speed_imitation, 0)
        func()

@wrap.always(30)
# Движение персонажа в игре
def game():
    global pos_x_player, player_on_game
    if player_on_game == False:
        sprite.move(player, 0, pos_x_player)
        if sprite.get_y(player) > 260:
            pos_x_player = -pos_x_player
        if sprite.get_y(player) < 240:
            pos_x_player = -pos_x_player
    else:
        sprite.move(player, 0, speed_player)
        change_angle()
        collide()
        score()
        actions_let(let_1, 650)
        actions_let(let_2, 650)

@wrap.always(25)
def game():
    # Поворот персонажа в игре
    global player_on_game
    if player_on_game == True:
        change_angle()

def stop_game():
    global speed_player,speed_imitation,speed_let,speed_click
    speed_let=0
    speed_imitation=0
    speed_player=0
    speed_click=0
def score():
    global count,logic_score1,logic_score2,text_score
    for i in let_1:
        if sprite.get_x(player)>sprite.get_x(let_1[i]) and logic_score1==True:
            count=count+1
            logic_score1=False
            wrap.sprite_text.set_text(text_score,str(count))
            break
        if sprite.get_x(let_1[i])>490:
            logic_score1=True
    for i in let_2:
        if sprite.get_x(player)>sprite.get_x(let_2[i]) and logic_score2==True:
            count=count+1
            wrap.sprite_text.set_text(text_score, str(count))
            logic_score2=False
            break
        if sprite.get_x(let_2[i])>490:
            logic_score2=True



import wrap_py
wrap_py.app.start()