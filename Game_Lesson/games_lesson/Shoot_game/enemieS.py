import wrap
from wrap import sprite, sprite_text
import random

l=50
h=300
def add_random_hp_enemies():
    hp = random.randint(50,150)
    return hp
def create(speed_enemies):
    global l,h
    id = sprite.add("mario-enemies", l, h, 'cloud')
    if l>=500:
        l=40
        h=h-50
    l+=40
    hp = add_random_hp_enemies()
    id2 = wrap.sprite.add_text(str(hp), wrap.sprite.get_x(id), wrap.sprite.get_y(id), bold=True, font_size=15)
    a={"Name": id, "Name_text": id2, "HP": hp, "speed ": speed_enemies}
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


def collision_enemie(enemies,bullet,bullets):
    for enemie in enemies:
        if sprite.is_collide_any_sprite(enemie["Name"],bullets):

            if sprite.is_visible(bullet)==True:
                sprite.hide(bullet)
                bullets.remove(bullet)
            hp_text=wrap.sprite_text.get_text(enemie["Name_text"])
            wrap.sprite_text.set_text(enemie["Name_text"],str(int(hp_text)-5))
            enemie["HP"]=int(hp_text)-5
            if enemie["HP"] <= 0:
                sprite.hide(enemie["Name"])
                sprite.hide(enemie["Name_text"])
                enemies.remove(enemie)





