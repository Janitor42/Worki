import wrap, random, time, math
from wrap import actions, sprite, world, sprite_text

world.create_world(500, 600)
world.set_back_color(128, 171, 226)

wrap.add_sprite_dir("C:/Users/i'm/PycharmProjects/Worki/semen")
hero = wrap.sprite.add("Anim", 100, 430, "run1")
sprite.set_width_proportionally(hero, 300)

state = "run"

a = 0
b = 0
run = 1

frame = 12
jump = False
start = time.time()
on_off = True


@wrap.always(5)
def game():
    global a, jump, b
    if state == "run":
        b = b + 1
        switch_costume_run()
    if state == "jump":
        switch_costume_jump()
        if a < 50 and jump == True:
            a = a + 1
            sprite.move(hero, 0, -2)
        if a > 49 and jump == True:
            a = a + 1
            sprite.move(hero, 0, 2)
        if a >= 100 and jump == True:
            jump = False
            a = 0


@wrap.on_key_down(wrap.K_SPACE)
def jump():
    global a, jump, on_off, state, b
    jump = True
    state = "jump"
    b = 119


def switch_costume_jump():
    global a, hero, on_off, frame, b, state
    frame = 0
    if a == 16:
        sprite.set_costume(hero, "jump1")
    if a == 32:
        sprite.set_costume(hero, "jump2")
    if a == 49:
        sprite.set_costume(hero, "jump3")

    if a == 50:
        sprite.set_costume(hero, "fall1")
    if a == 62:
        sprite.set_costume(hero, "fall2")
    if a == 73:
        sprite.set_costume(hero, "fall3")
    if a == 85:
        sprite.set_costume(hero, "fall4")
    if a == 99:
        sprite.set_costume(hero, "run1")
        state = "run"


def change_costume():
    global frame, run, b
    if b == frame:
        frame = frame + 12
        costume = "run" + str(run)
        sprite.set_costume(hero, costume)
        run = run + 1


def switch_costume_run():
    global frame, run, b, on_off

    change_costume()
    if b == 120:
        b = 0
        frame = 12
        run = 1
    # if on_off==False:
    #     b=0


import wrap_py

wrap_py.app.start()



# import wrap, random, time, math
# from wrap import actions, sprite, world, sprite_text
#
# world.create_world(500, 600)
# world.set_back_color(128, 171, 226)
# wrap.add_sprite_dir("C:/Users/Петр/PycharmProjects/ProjectSemyon/Dino/picture")
# hero = wrap.sprite.add("Anim", 100, 430, "run1")
# sprite.set_width_proportionally(hero, 300)
#
# state = "run"
#
# a = 0
# b = 0
# run = 1
#
# frame = 12
# jump = False
# start = time.time()
# on_off = True
#
#
# @wrap.always(5)
# def game():
#     global a, jump, b
#     if state == "run":
#         b = b + 1
#         switch_costume_run()
#     if state == "jump":
#         switch_costume_jump()
#         if a < 50 and jump == True:
#             a = a + 1
#             sprite.move(hero, 0, -2)
#         if a > 49 and jump == True:
#             a = a + 1
#             sprite.move(hero, 0, 2)
#         if a >= 100 and jump == True:
#             jump = False
#             a = 0
#
#
# @wrap.on_key_down(wrap.K_SPACE)
# def jump():
#     global a, jump, on_off, state, b
#     jump = True
#     state = "jump"
#     b = 119
#
#
# def switch_costume_jump():
#     global a, hero, on_off, frame, b, state
#     frame = 0
#     if a == 16:
#         sprite.set_costume(hero, "jump1")
#     if a == 32:
#         sprite.set_costume(hero, "jump2")
#     if a == 49:
#         sprite.set_costume(hero, "jump3")
#
#     if a == 50:
#         sprite.set_costume(hero, "fall1")
#     if a == 62:
#         sprite.set_costume(hero, "fall2")
#     if a == 73:
#         sprite.set_costume(hero, "fall3")
#     if a == 85:
#         sprite.set_costume(hero, "fall4")
#     if a == 99:
#         sprite.set_costume(hero, "run1")
#         state = "run"
#
#
# def change_costume():
#     global frame, run, b
#     if b == frame:
#         frame = frame + 12
#         costume = "run" + str(run)
#         sprite.set_costume(hero, costume)
#         run = run + 1
#
#
# def switch_costume_run():
#     global frame, run, b, on_off
#
#     change_costume()
#     if b == 120:
#         b = 0
#         frame = 12
#         run = 1
#     # if on_off==False:
#     #     b=0
#
#
# import wrap_py
#
# wrap_py.app.start()
