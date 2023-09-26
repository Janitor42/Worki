import wrap
import time
a=560
wrap.world.create_world(600,600)
samsung=wrap.sprite.add_text("Samsung",40,20,text_color=(255, 0, 0))
samsung_x1=2
samsung_y1=2
while True:
    samsung_x=wrap.sprite.get_x(samsung)
    samsung_y=wrap.sprite.get_y(samsung)
    wrap.sprite.move(samsung,samsung_x1,samsung_y1)
    print(samsung_x,samsung_y)
    if samsung_x>=560:
        samsung_x1 = -2
    if samsung_y>=580:
        samsung_y1=-2
    if samsung_x<=40:
        samsung_x1 = 2
    if samsung_y <= 20:
        samsung_y1 = 2