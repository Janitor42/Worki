import wrap
from wrap import sprite, sprite_text
import random


def hp_move_to_player(player_hp,player,angle):
    if abs(angle) <=90:
        sprite.move_to(player_hp,sprite.get_x(player),sprite.get_y(player)+5)
    else:
        sprite.move_to(player_hp,sprite.get_x(player),sprite.get_y(player)-5)

def damage_player(enemies,player,text,hp):
    for i in enemies:
        if sprite.is_collide_sprite(i["Name"],player):
            hp = hp - 5
            sprite_text.set_text(text, str(hp))
            sprite.hide(i["Name"])
            sprite.hide(i["Name_text"])
            enemies.remove(i)
    return hp