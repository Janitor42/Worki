import wrap,random,time,math
from wrap import actions,sprite,world
import personage
b=None
a=0
my_choice=None
my_choice_copies=[]
world.create_world(950,700)
world.set_back_color(48, 48, 48)
line1=sprite.add("pacman",475,527,"dot")
line2=sprite.add("pacman",316,616,"dot")
line3=sprite.add("pacman",632,616,"dot")
sprite.add_text("Points",370,560)
sprite.set_width(line1,950)
sprite.set_height(line2,175)
sprite.set_height(line3,175)
personage.tanks_def(50)
personage.personage_list_add()
personage.clouds_def(113,50)
copy_personage=[]
play_list=[]

# list1=["mushroom_liveup"]
# list2=["turtle_stand"]
# list3=["flower1"]
# list4=["dragon_stand2"]
@wrap.always(1)
def go_right(pos_y,pos_x):
    global my_choice,a

    if my_choice!= None:
        sprite.move_at_angle_point(copy_personage[-1], pos_x, pos_y, 2)

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def down_mouse(pos_x,pos_y):
    global  my_choice,my_choice_copy
    for i in personage.personage_list:
        if sprite.is_collide_point(i["Name"],pos_x,pos_y):
            my_choice = i
            personage.create(my_choice,copy_personage)
            sprite.set_reverse_x(copy_personage[-1], True)
    if len(copy_personage) > 0:
        for i in personage.clouds:
            sprite.show(i)
        personage.show_param()

@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def up_mouse():
    global my_choice
    if len(copy_personage )>0:
        if sprite.is_collide_any_sprite(copy_personage[-1], personage.clouds):
            my_choice = None
            cloud=sprite.is_collide_any_sprite(copy_personage[-1], personage.clouds)
            sprite.move_to(copy_personage[-1],sprite.get_x(cloud),sprite.get_y(cloud))
            sprite.hide(sprite.is_collide_any_sprite(copy_personage[-1], personage.clouds))
            personage.clouds.remove(sprite.is_collide_any_sprite(copy_personage[-1], personage.clouds))
            sprite.remove(sprite.is_collide_any_sprite(copy_personage[-1], personage.clouds))
            text_Strange = sprite.add_text("Strange", 370, 620, visible=False)
            text_Reload = sprite.add_text("Reload", 370, 645, visible=False)
            text_Health = sprite.add_text("Health", 370, 670, visible=False)

            if personage.charge == 1:
                play_list.append({"Name": copy_personage[-1], "damage_second": 150, "Time": 5,
                                  "Health": 130,
                                  "Strange_text": sprite.add_text("Strange_poison", 370, 620),
                                  "Reload_text": sprite.add_text("Reload", 370, 645),
                                  "Health_text": sprite.add_text("Health", 370, 670),
                                  "Strange_count": sprite.add_text(str(150), 420, 620),
                                  "Reload_count": sprite.add_text(str(5), 420, 645),
                                  "Health_count": sprite.add_text(str(140), 420, 670),
                                  "Explanation_text1": sprite.add_text("Персонаж ударяет ", 550, 635, visible=False),
                                  "Explanation_text2": sprite.add_text("раз в 5 секунд", 550, 655, visible=False),
                                  "Explanation_text3": sprite.add_text("по 3 раза,по 50урона", 550, 675,
                                                                       visible=False)})
            if personage.charge == 2:
                play_list.append({"Name": copy_personage[-1], "strange": 230, "Time": 7,
                                  "Health": 145, "Strange_text": sprite.add_text("Strange", 370, 620),
                                  "Reload_text": sprite.add_text("Reload", 370, 645),
                                  "Health_text": sprite.add_text("Health", 370, 670),
                                  "Strange_count": sprite.add_text(str(230), 420, 620),
                                  "Reload_count": sprite.add_text(str(7), 420, 645),
                                  "Health_count": sprite.add_text(str(145), 420, 670)})
            if personage.charge == 3:
                play_list.append({"Name": copy_personage[-1], "point": 150, "Time": 3,
                                  "Health": 105, "Point_text": sprite.add_text("Point", 370, 620),
                                  "Reload_text": sprite.add_text("Reload", 370, 645),
                                  "Health_text": sprite.add_text("Health", 370, 670),
                                  "Point_count": sprite.add_text(str(50), 420, 620),
                                  "Reload_count": sprite.add_text(str(3), 420, 645),
                                  "Health_count": sprite.add_text(str(105), 420, 670)})
            if personage.charge == 4:
                play_list.append({"Name": copy_personage[-1], "strange": 80, "Time": 3,
                                  "Health": 145, "Strange_text": sprite.add_text("Strange", 370, 620),
                                  "Reload_text": sprite.add_text("Reload", 370, 645),
                                  "Health_text": sprite.add_text("Health", 370, 670),
                                  "Strange_count": sprite.add_text(str(80), 420, 620),
                                  "Reload_count": sprite.add_text(str(3), 420, 645),
                                  "Health_count": sprite.add_text(str(145), 420, 670)})
            copy_personage.clear()
            for i in personage.clouds:
                sprite.hide(i)
            personage.hide_param()


import wrap_py
wrap_py.app.start()
