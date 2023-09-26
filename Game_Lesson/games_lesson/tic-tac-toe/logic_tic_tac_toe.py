import random
import wrap
from wrap import sprite

game_match = True
miss_to_click = random.choice([True,False])

score_p=0
score_c=0

def create_field(name, x, y, field):
    old_x = x
    pos = 1
    for i in range(9):
        id = sprite.add(name, x, y)
        sprite.set_size(id, 10, 10)
        dici = {'name': id, 'pos': pos}
        field.append(dici)
        x += 100
        pos += 1
        if i == 2 or i == 5:
            y += 100
            x = old_x
            pos += 1


def run_player(field, pos_x, pos_y, player,picture,hand):
    global miss_to_click
    for i in field:
        if sprite.is_collide_point(i['name'], pos_x, pos_y) and hand:
            create_figure(i, player,picture)
            field.remove(i)
            miss_to_click = True
            break



def run_computer(field, computer,picture):
    global miss_to_click,game_match
    if len(field)<1:
        game_match = not  game_match
    elif game_match and miss_to_click:
        rd_choice = random.choice(field)
        computer.append(rd_choice['pos'])
        id=sprite.add('pacman', sprite.get_x(rd_choice['name']), sprite.get_y(rd_choice['name']), 'item_apple')
        picture.append(id)
        sprite.hide(rd_choice['name'])
        field.remove(rd_choice)
        miss_to_click = False



def create_figure(i, player,picture):
    id=sprite.add('mario-items', sprite.get_x(i['name']), sprite.get_y(i['name']), "mushroom_super")
    picture.append(id)
    sprite.hide(i['name'])
    player.append(i['pos'])


def checks(this):
    check_field(this, 1, 2)
    check_field(this, 4, 8)
    check_field(this, 3, 6)
    check_field(this, 5, 10)



def check_field(this, value_1, value_2):
    global game_match
    for i in this:
        if i + value_1 in this and i + value_2 in this:
            this.append(100)
            game_match = not game_match


def who_win(this,player,computer,other):
    if 100 in this and miss_to_click:
        global score_p,score_c
        score_p+=1
        wrap.sprite_text.set_text(player,'Your score '+str(score_p))
    if 100 in other:
        score_c+=1
        wrap.sprite_text.set_text(computer,'Him score  '+str(score_c))


def reset_all(picture,player,computer,field):
    global game_match
    for i in field:
        sprite.hide(i['name'])
    field.clear()
    for i in picture:
        sprite.hide(i)
    picture.clear()
    player.clear()
    computer.clear()
    game_match = not game_match
