import wrap
import random
wrap.world.create_world(600,600)
ship = {}
asteroids_list = []
bullet_list = []

bullet = {}
random_x1 = 0
random_x2 = 0
y = 0
choose_x = 0

switch = "stop"
number = 1
def create_ship():
    ship["name"] = wrap.sprite.add("battle_city_tanks", 300, 300,"tank_enemy_size1_green1")
    ship["lives"] = 3
    ship["shoot_speed"] = 1
    ship["score"] = 0
    ship["score_text"] = wrap.sprite.add_text(str(ship["score"]),550,20,text_color=(255,255,255))
    wrap.sprite.set_size(ship["name"], 50,50)

def choose_pos():
    global random_x1, random_x2,y, choose_x
    random_x1 = random.choice([-200,800])
    random_x2 = random.randint(-200,800)
    choose_x = random.choice([random_x1,random_x2])
    if choose_x == random_x1:
        y = random.randint(-200,800)
    if choose_x == random_x2:
        y = random.choice([-200, 800])
def create_asteroids():
    for i in range(3):
        choose_pos()
        asteroids = {"name" : wrap.sprite.add("pacman", choose_x, y, "player3"),
                     "size" : random.randint(30,100),
                     "pieces" : random.randint(2,5),
                     "speed" : random.randint(2,3),
                     "rotation": random.randint(0,360)}
        wrap.sprite.set_size(asteroids["name"],asteroids["size"],asteroids["size"])
        print(asteroids["size"])
        asteroids["x"] = wrap.sprite.get_x(asteroids["name"])
        asteroids["y"] = wrap.sprite.get_y(asteroids["name"])

        asteroids_list.append(asteroids)


def create_bullet():
    global number
    for i in range(3):
        bullet = {"name" : wrap.sprite.add("battle_city_items", 300,300, "bullet"),
                  "switch" :"stop"}
        bullet_list.append(bullet)
    print(bullet_list)
@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def bullet_move(pos_x, pos_y):
    global switch
    for i in bullet_list:
        if i["switch"] == "stop":
            i["switch"] = "fly"
            wrap.sprite.show(i["name"])
            wrap.sprite.set_angle_to_point(i["name"], pos_x,pos_y)
            i["angle"] = wrap.sprite.get_angle(i["name"])
            break




@wrap.on_mouse_move()
def move_ship(pos_x,pos_y):
    wrap.sprite.set_angle_to_point(ship["name"], pos_x,pos_y)

create_ship()
# create_asteroids()

create_bullet()
@wrap.always(20)
def game():
    global switch
    for i in asteroids_list:
        for a in bullet_list:
            if wrap.sprite.is_collide_sprite(a["name"], i["name"]):
                a["switch"] = "stop"

    for i in bullet_list:
        if i["switch"] == "stop":
            wrap.sprite.move_to(i["name"], 300, 300)


    for i in bullet_list:
        if i["switch"] == "fly":
            wrap.sprite.move_at_angle(i["name"], i["angle"], 4)

        for i in bullet_list:
            if wrap.sprite.get_x(i["name"]) >= 600:
                wrap.sprite.move_to(i["name"], 300, 300)
                i["switch"] = "stop"
            if wrap.sprite.get_x(i["name"]) <= 0:
                wrap.sprite.move_to(i["name"], 300, 300)
                i["switch"] = "stop"
            if wrap.sprite.get_y(i["name"]) >= 600:
                wrap.sprite.move_to(i["name"], 300, 300)
                i["switch"] = "stop"
            if wrap.sprite.get_y(i["name"]) <= 0:
                wrap.sprite.move_to(i["name"], 300, 300)
                i["switch"] = "stop"

    @wrap.always(100)
    def game2():
        for i in asteroids_list:
            wrap.sprite.move_at_angle_point(i["name"], 300, 300, i["speed"])
        for i in bullet_list:
            print(wrap.sprite.get_angle(i["name"]))
        print("ship", wrap.sprite.get_angle(ship["name"]))

import wrap_py
wrap_py.app.start()