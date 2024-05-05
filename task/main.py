import wrap, random, time, math
from wrap import actions, sprite, world
import personage

b = None
a = 0
my_choice = None
my_choice_copies = []
world.create_world(950, 700)
world.set_back_color(48, 48, 48)
line1 = sprite.add("pacman", 475, 527, "dot")
line2 = sprite.add("pacman", 316, 616, "dot")
line3 = sprite.add("pacman", 632, 616, "dot")
sprite.add_text("Points", 370, 560)
sprite.set_width(line1, 950)
sprite.set_height(line2, 175)
sprite.set_height(line3, 175)
personage.tanks_def(50)
personage.personage_list_add()
personage.clouds_def(113, 50)
copy_personage = []
play_list = []
start_x=None
start_y=None

# list1=["mushroom_liveup"]
# list2=["turtle_stand"]
# list3=["flower1"]
# list4=["dragon_stand2"]
@wrap.always(1)
def go_right(pos_y, pos_x):
    global my_choice, a

    if my_choice != None:
        sprite.move_to(my_choice['Name'], pos_x, pos_y)

    for i in play_list:
        if sprite.is_collide_point(i['Name'],pos_x,pos_y):
            print(i)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def down_mouse(pos_x, pos_y):
    global my_choice,start_x,start_y
    for i in personage.personage_list:
        if sprite.is_collide_point(i["Name"], pos_x, pos_y):
            my_choice = i
            start_x=sprite.get_x(my_choice['Name'])
            start_y=sprite.get_y(my_choice['Name'])
            sprite.set_reverse_x(my_choice['Name'], True)
            for i in personage.clouds:
                sprite.show(i)
            personage.show_param(my_choice)


@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def up_mouse():
    global my_choice
    if my_choice != None:

        if sprite.is_collide_any_sprite(my_choice['Name'], personage.clouds):
            cloud = sprite.is_collide_any_sprite(my_choice['Name'], personage.clouds)

            personage.create(my_choice,play_list)
            param=my_choice.copy()

            print(param)
            print(play_list)

            print(play_list[-1]['Name'])

            param['Name']=play_list[-1]['Name']
            play_list[-1]=param
            print(play_list)

            for i in personage.clouds:
                sprite.hide(i)

            personage.hide_param(my_choice)
            sprite.move_to(my_choice['Name'],start_x,start_y)
            my_choice = None


        else:
            sprite.move_to(my_choice['Name'],start_x,start_y)
            my_choice = None




import wrap_py

wrap_py.app.start()
