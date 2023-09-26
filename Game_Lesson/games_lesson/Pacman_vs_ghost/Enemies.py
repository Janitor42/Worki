import wrap
import time
import random
from wrap import sprite
from random import randint, choice, randrange

place_start_enemies_x = 900
def create():
    global place_start_enemies_x,h
    h=randrange(98,603,83)
    place_start_enemies_x+=10
    hp=100
    id = sprite.add("mario-enemies", place_start_enemies_x, h, 'cloud')
    text_name = wrap.sprite.add_text(str(hp), wrap.sprite.get_x(id), wrap.sprite.get_y(id), bold=True, font_size=15)
    a={"Name": id,  "HP": 100, "speed ": 3,'text_name':text_name}
    return a


def move_to_sprite(player,enemie,friend):
    global a,angle
    x=sprite.get_x(enemie["Name"])
    y=sprite.get_y(enemie["Name"])
    sprite.move_at_angle_point(enemie["Name"], sprite.get_x(player), sprite.get_y(player),3)
    for i in friend:
        if i is enemie:
            continue
        if sprite.is_collide_sprite(enemie["Name"],i["Name"]):
            sprite.move_at_angle_point(enemie["Name"],random.randint(-500,500),random.randint(-500,500),6)
    sprite.move_to(enemie["Name_text"], sprite.get_x(enemie["Name"]), sprite.get_y(enemie["Name"]))

    for i in friend:
        if i is enemie:
            continue
        if sprite.is_collide_sprite(enemie["Name"],i["Name"]):
            sprite.move_at_angle_point(enemie["Name"],x,y,10)
    sprite.move_to(enemie["Name_text"], sprite.get_x(enemie["Name"]), sprite.get_y(enemie["Name"]))

def move_enemies(enemie):
    for i in enemie:
        sprite.move(i['Name'],-0.1,0)
        sprite.move_to(i['text_name'],sprite.get_x(i['Name']),sprite.get_y(i['Name']))
