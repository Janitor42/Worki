import random

import wrap
from wrap import sprite

wrap.world.create_world(1000, 500)

letters = []
angle_letters = []


used_words = []
angle_letters.append(180)

first_sprite=sprite.add_text("you", 500, 250, text_color=(255,0,0))
letters.append(first_sprite)


def move(words):
    for i in range(len(words)):
        sprite.move_at_angle(words[i], angle_letters[i], 3)


def invisible_wall(words):
    for i in words:
        if sprite.get_x(i) >= 950 or sprite.get_x(i) <= 50 or sprite.get_y(i) >= 450 or sprite.get_y(i) <= 50:
            return i





def remove_and_replace_words(words, this_word):
    for i in words:
        if i == this_word:
            used_words.append(i)
            words.remove(i)




def remove_old_angle(words,this_word):

    for i in range(len(angle_letters)):
        index=words.index(this_word)
        if i is index:
            return angle_letters.pop(i)


def check_more_count(count):
    if len(used_words)>count-1:
        hide_first_sprite()
    if len(used_words)>count:
        used_words.remove(used_words[0])
        sprite.hide(used_words[0])
        sprite.remove(used_words[0])

def hide_first_sprite():
    if sprite.is_visible(first_sprite):
        sprite.hide(first_sprite)

def whose_text(this_word):
    if wrap.sprite_text.get_text(this_word)=='you':
        return 'i_m'
    else:
        return 'you'

def whose_color(this_word):
    if wrap.sprite_text.get_text(this_word)=='you':
        return (255,255,255)
    else:
        return (255,0,0)



def add_two_new_words(words,text,color,this_word):



    for i in range(2):
        name = sprite.add_text(text, sprite.get_x(this_word),sprite.get_y(this_word),text_color=color)
        words.append(name)
        sprite.move_at_angle_point(letters[-1],500,250,10)


def create_new_angles(angle):
    positive = 30
    negative = -30
    for i in range(2):
        if angle > 180:
            angle_letters.append(angle - 180 + positive)
            positive += 30
        else:
            angle_letters.append(angle + 180 + negative)
            negative += 30

@wrap.always(25)
def action():

    move(letters)
    this_word = invisible_wall(letters)

    if this_word is not None:

        text=whose_text(this_word)
        color=whose_color(this_word)

        add_two_new_words(letters, text,color,this_word)

        angle=remove_old_angle(letters,this_word)
        create_new_angles(angle)

        remove_and_replace_words(letters, this_word)

    check_more_count(5)


import wrap_py
wrap_py.app.start()
