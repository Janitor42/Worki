import wrap,random,time,math
from wrap import actions,sprite,world
charge=0
texts=[]
clouds=[]
tanks=[]
personage_list=[]
def tanks_def(y):
    for i in range(6):
        tank = sprite.add("battle_city_tanks", 33, y, "tank_enemy_size1_yellow1")
        tanks.append(tank)
        sprite.set_width_proportionally(tanks[-1],50)
        sprite.set_angle(tanks[-1],90)
        y=y+75
def personage_list_add ():
    flower = sprite.add("mario-items", 50, 590, "flower1")
    personage_list.append({"Name": flower,"point":150, "Time": 3,
                      "Health": 105, "Point_text": sprite.add_text("Strange", 370, 620,visible=False),
                      "Reload_text": sprite.add_text("Reload", 370, 645,visible=False),
                      "Health_text": sprite.add_text("Health", 370, 670,visible=False),
                      "Point_count": sprite.add_text(str(150), 420, 620,visible=False),
                      "Reload_count": sprite.add_text(str(3), 420, 645,visible=False),
                      "Health_count": sprite.add_text(str(105), 420, 670,visible=False)})
    grip = sprite.add("mario-items", 150, 590, "mushroom_liveup")
    personage_list.append({"Name": grip, "damage_second": 150, "Time": 5,
                           "Health": 130, "Strange_text": sprite.add_text("Strange_poison", 370, 620, visible=False),
                           "Reload_text": sprite.add_text("Reload", 370, 645, visible=False),
                           "Health_text": sprite.add_text("Health", 370, 670, visible=False),
                           "Strange_count": sprite.add_text(str(150), 440, 620, visible=False),
                           "Reload_count": sprite.add_text(str(5), 440, 645, visible=False),
                           "Health_count": sprite.add_text(str(130), 440, 670, visible=False),
                           "Explanation_text1": sprite.add_text("Персонаж ударяет ", 550, 635, visible=False),
                           "Explanation_text2": sprite.add_text("раз в 5 секунд", 550, 655,
                                                                visible=False),
                           "Explanation_text3": sprite.add_text("по 3 раза,по 50урона", 550, 675, visible=False)})
    dragon = sprite.add("mario-enemies", 150, 670, "dragon_stand2")
    sprite.set_reverse_x(dragon, 180)
    sprite.set_size(dragon, 40, 40)
    personage_list.append({"Name": dragon, "strange": 80, "Time": 3,
                           "Health": 145, "Strange_text": sprite.add_text("Strange", 370, 620, visible=False),
                           "Reload_text": sprite.add_text("Reload", 370, 645, visible=False),
                           "Health_text": sprite.add_text("Health", 370, 670, visible=False),
                           "Strange_count": sprite.add_text(str(80), 420, 620, visible=False),
                           "Reload_count": sprite.add_text(str(3), 420, 645, visible=False),
                           "Health_count": sprite.add_text(str(145), 420, 670, visible=False)})
    turtle = sprite.add("mario-enemies", 250, 590, "turtle_stand")
    sprite.set_reverse_x(turtle, 180)
    personage_list.append({"Name": turtle, "strange": 230, "Time": 7,
                           "Health": 145, "Strange_text": sprite.add_text("Strange", 370, 620, visible=False),
                           "Reload_text": sprite.add_text("Reload", 370, 645, visible=False),
                           "Health_text": sprite.add_text("Health", 370, 670, visible=False),
                           "Strange_count": sprite.add_text(str(230), 420, 620, visible=False),
                           "Reload_count": sprite.add_text(str(7), 420, 645, visible=False),
                           "Health_count": sprite.add_text(str(145), 420, 670, visible=False)})



def clouds_def(x,y):
    for i in range(24):
        cloud = sprite.add("mario-scenery", x, y, "cloud1",visible=False)

        cloud_y=sprite.get_y(cloud)
        clouds.append(cloud)

        sprite.set_width_proportionally(clouds[-1], 50)
        sprite.set_angle(clouds[-1], 90)
        y=y+75
        if cloud_y==425:
            x=x+80
            y = 50
def create(my_choice,copy_personage):
    global charge
    if sprite.get_costume(my_choice["Name"])=="mushroom_liveup":
        copy_personage.append(
            sprite.add("mario-items",sprite.get_x(my_choice["Name"]) ,sprite.get_y(my_choice["Name"]),
                       sprite.get_costume(my_choice["Name"])))
        charge=1
    elif sprite.get_costume(my_choice["Name"])=="turtle_stand":
        copy_personage.append(
            sprite.add("mario-enemies",sprite.get_x(my_choice["Name"]) ,sprite.get_y(my_choice["Name"]),
                       sprite.get_costume(my_choice["Name"])))
        charge = 2
    elif sprite.get_costume(my_choice["Name"])=="flower1":
        copy_personage.append(
            sprite.add("mario-items",sprite.get_x(my_choice["Name"]) ,sprite.get_y(my_choice["Name"]),
                       sprite.get_costume(my_choice["Name"])))
        charge = 3
    elif sprite.get_costume(my_choice["Name"])=="dragon_stand2":
        copy_personage.append(
            sprite.add("mario-enemies",sprite.get_x(my_choice["Name"]) ,sprite.get_y(my_choice["Name"]),
                       sprite.get_costume(my_choice["Name"])))
        charge = 4
def show_param():
    for i in personage_list:
        if charge == 1:
            sprite.show(i["Strange_text"])
            sprite.show(i["Reload_text"])
            sprite.show(i["Health_text"])
            sprite.show(i["Reload_count"])
            sprite.show(i["Health_count"])
            sprite.show(i["Explanation_text1"])
            sprite.show(i["Explanation_text2"])
            sprite.show(i["Explanation_text3"])
        if charge == 3:
            sprite.show(i["Point_count"])
            sprite.show(i["Point_text"])
            sprite.show(i["Reload_text"])
            sprite.show(i["Health_text"])
            sprite.show(i["Reload_count"])
            sprite.show(i["Health_count"])
        if charge == 2 or charge == 4:
            sprite.show(i["Strange_text"])
            sprite.show(i["Reload_text"])
            sprite.show(i["Health_text"])
            sprite.show(i["Strange_count"])
            sprite.show(i["Reload_count"])
            sprite.show(i["Health_count"])
def hide_param():
    for i in personage_list:
        if charge == 1:
            sprite.hide(i["Strange_text"])
            sprite.hide(i["Reload_text"])
            sprite.hide(i["Health_text"])
            sprite.hide(i["Reload_count"])
            sprite.hide(i["Health_count"])
            sprite.hide(i["Explanation_text1"])
            sprite.hide(i["Explanation_text2"])
            sprite.hide(i["Explanation_text3"])
        if charge == 3:
            sprite.hide(i["Point_count"])
            sprite.hide(i["Point_text"])
            sprite.hide(i["Reload_text"])
            sprite.hide(i["Health_text"])
            sprite.hide(i["Reload_count"])
            sprite.hide(i["Health_count"])
        if charge == 2 or charge == 4:
            sprite.hide(i["Strange_text"])
            sprite.hide(i["Reload_text"])
            sprite.hide(i["Health_text"])
            sprite.hide(i["Strange_count"])
            sprite.hide(i["Reload_count"])
            sprite.hide(i["Health_count"])

