import time

import wrap
from wrap import sprite
import random
wrap.world.create_world(500,500)
wrap.world.set_back_color(100,100,100)
platform = sprite.add("mario-items", 30, 420, "moving_platform2")
target= sprite.add("mario-items",250,50,"coin")


score_text = 0
sprite.add_text("score:",410,449)
score = sprite.add_text(str(score_text),450,450)

lives_text=3
sprite.add_text("lives:",50,449)
lives= sprite.add_text(str(lives_text),80,450)

speed = 5
speed_platform=10

@wrap.on_key_always(wrap.K_a)
def go_right():
        sprite.move(platform,-speed_platform, 0)

@wrap.on_key_always(wrap.K_d)
def go_right():
        sprite.move(platform, speed_platform, 0)

@wrap.always(50)
def move_target():
        global speed,score_text,score,speed_platform
        global lives,lives_text
        sprite.move(target,0,speed)#???
        if sprite.is_collide_sprite(platform,target):
                sprite.move_to(target,random.randint(20,480),20)
                speed=speed+0.5
                sprite.remove(score)
                score_text=score_text+1
                score=sprite.add_text(str(score_text),450,450)
        if sprite.get_y(target)>450:
                sprite.remove(lives)
                lives_text = lives_text - 1
                lives = sprite.add_text(str(lives_text), 80, 450)
                sprite.move_to(target, random.randint(20, 480), 20)
        if lives_text==0:
                sprite.add_text("Game Over",250,250,font_size = 60)
                sprite.hide(target)
                speed=0
                speed_platform=0

import wrap_py
wrap_py.app.start()

