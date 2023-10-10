import wrap
import random
from wrap import world,sprite
wrap.world.create_world(1300,700)
wrap.world.set_back_color(239,88,158)
bird=sprite.add("mario-enemies",250,350,"fish_red")
sprite.set_reverse_x(bird,True)



#cubes enemies
cubes1=[]
cubes2=[]
def instruction(pos_x,cubes):
    number_cube = 1
    y = 0
    #cubes platform 1
    for i in range(27):
        cubes.append(sprite.add("battle_city_items",pos_x,y,"block_brick"))
        y=y+30

    print(cubes)
    #gap in the cubes
    random_cube=random.randint(3,20)
    print(random_cube)
    # for i in range(5):
    sprite.hide(cubes[(random_cube)])
        # number_cube=number_cube+1
#asking for the functions to happen
instruction(700,cubes1)
instruction(1200,cubes2)

angle=-90
switch=False
ground=[]
x=20
for i in range(7):
    ground.append(sprite.add("mario-items",x,670,"moving_platform3"))
    x+=95
number=0
@wrap.always()
def moving_platforms():
    global number,ground,angle
    # sprite.move(ground[number],-5,0)
    # number=number+1
    # if number>=7:
    #     number=0
    for i in ground:
        sprite.move(i,-5,0)
        if sprite.get_x(i) <= -95:
            sprite.move_to(i,570,670)

    if switch==True:
        fall()
        sprite.set_angle(bird,angle)
        if angle == 0:
            angle = 0
        else:
            angle=angle+10

#bird jumps
@wrap.on_key_down(wrap.K_UP)
def jump():
    global angle
    sprite.move(bird,0,-40)
    angle=-90

#bird falling
@wrap.on_key_down(wrap.K_SPACE)
def fall():
    global switch
    sprite.move(bird,0,7)
    switch=True


import wrap_py

wrap_py.app.start()