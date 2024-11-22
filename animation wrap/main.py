import wrap, random, time, math
from wrap import actions, sprite, world, sprite_text

world.create_world(500, 600)
world.set_back_color(128, 171, 226)

wrap.add_sprite_dir("/animation wrap")
hero = wrap.sprite.add("picture", 100, 430, "HeroKnight_Run_0")
sprite.set_width_proportionally(hero, 300)

state = "run"
frame = -1
next_costume = 0


@wrap.on_key_down(wrap.K_SPACE)
def jump():
    global frame, state, next_costume
    if state == 'run':
        frame = -1
        state = 'jump'
        next_costume = 0


def anim_run():
    global next_costume, frame
    if frame > 89:
        frame = 0
        next_costume = 0

    if frame == next_costume:
        next_costume += 10
        text_costume = 'HeroKnight_Run_' + str(next_costume // 10)
        sprite.set_costume(hero, text_costume)


def anim_jump():
    global frame, state, next_costume
    if frame > 59:
        frame = -1
        state = 'run'
        next_costume = 0
    if frame == next_costume and state == 'jump':
        next_costume += 10
        text_costume = 'HeroKnight_Jump_' + str(next_costume // 10)
        sprite.set_costume(hero, text_costume)


@wrap.always(10)
def game():
    global frame
    frame += 1
    if state == 'run':
        anim_run()

    elif state == 'jump':
        anim_jump()


import wrap_py

wrap_py.app.start()
