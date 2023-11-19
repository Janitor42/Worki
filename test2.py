import wrap

wrap.world.create_world(800,600)
wrap.world.set_back_color(140,200,140)

speed_x = 17
listik = []
hero = False

def create_hero():
    x = 30
    y = 75
    for a in range(0,3):
        pacman = wrap.sprite.add("pacman", x, y, "enemy_red_down1" )
        listik.append(pacman)
        x = x + 35



@wrap.always()
def move_hero():
    global speed_x, hero
    if hero == False:
        create_hero()
        hero = not hero
        
    for i in listik:
        wrap.sprite.move(i, speed_x, 7)
        if wrap.sprite.get_right(i) >= 790:
            speed_x = - speed_x
            listik.reverse()
        elif wrap.sprite.get_left(i) <=10:
            speed_x = -speed_x
            listik.reverse()

        elif wrap.sprite.get_bottom(i) >350:
            for q in listik:
                wrap.sprite.remove(q)
            listik.clear()
            hero = False

import wrap_py
wrap_py.app.start()



