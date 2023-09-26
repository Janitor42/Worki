import wrap
from wrap import sprite
import random
wrap.world.create_world(500,500)
wrap.world.set_back_color(100,100,100)

#snake_head

snake_head = sprite.add("pacman",250,250,"dot")
sprite.set_height_proportionally(snake_head, 15)
speed_snake=20

#Target
target=sprite.add("pacman",450,250,"dot")
sprite.set_height_proportionally(target, 15)

list_body=[target]

#Score_text
score_text=0
sprite.add_text("score: ",50,50)
score=sprite.add_text(str(score_text),90,50)
list_boby2=[]

#controler
# region
@wrap.on_key_down(wrap.K_d)
def go_right():
        sprite.set_angle(snake_head,90)



@wrap.on_key_down(wrap.K_a)
def go_left():
        sprite.set_angle(snake_head, 270)


@wrap.on_key_down(wrap.K_s)
def go_down():
        sprite.set_angle(snake_head, 180)



@wrap.on_key_down(wrap.K_w)
def go_up():
        sprite.set_angle(snake_head, 360)


# endregion

def Game_over():
        sprite.add_text("Game Over", 250, 100, font_size=60)
        sprite.add_text("You score is ", 250, 200, font_size=60)
        sprite.add_text(str(score_text), 280, 300, font_size=60)

@wrap.always(300)
def move():
        global list_body,list_boby2,score_text,score,speed_snake

        x_head=sprite.get_x(snake_head)
        y_head=sprite.get_y(snake_head)
        sprite.move_at_angle_dir(snake_head,speed_snake)
        if sprite.get_x(snake_head)<0 or sprite.get_y(snake_head)<0 or sprite.get_x(snake_head)>500 or sprite.get_y(snake_head)>500:
                Game_over()
                speed_snake=0
        if sprite.is_collide_any_sprite(snake_head,list_body)==list_body[0]:
                sprite.remove(list_body[0])
                list_body.insert(0,sprite.add("pacman",random.randint(20,480),random.randint(20,480),"dot"))
                sprite.set_height_proportionally(list_body[0],15)
                score_text=score_text+1
                sprite.remove(score)
                score=sprite.add_text(str(score_text),90,50)
                list_boby2.append(sprite.add("pacman",0,0,"dot"))

        if score_text>0:
                for i in range(len(list_boby2)):
                        sprite.set_height_proportionally(list_boby2[i],15)
                        x_head_old=sprite.get_x(list_boby2[i])
                        y_head_old=sprite.get_y(list_boby2[i])
                        sprite.move_to(list_boby2[i], x_head, y_head)
                        x_head = x_head_old
                        y_head = y_head_old
                        if sprite.is_collide_any_sprite(snake_head,list_boby2)!=None:
                                Game_over()
                                speed_snake=0

import wrap_py
wrap_py.app.start()