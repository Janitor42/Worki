import random
from wrap import sprite
import wrap
import picture
angle = 45

width = 1100
long = 900
wrap.world.create_world(width, long)

#Указываем абсолютный путь к папке с файлами (в основе проекта)
# wrap.add_sprite_dir("C:/Users/i'm/PycharmProjects/Worki/picture")



#Как добавить спрайт(указываем подпапку(костюмы) х,у, а затем имя файла
# wrap.sprite.add("pik",500,500,"images")

#фоновая картинка - абсолютный путь к файлу со всеми папками включая название картинки и расширение
# wrap.world.set_back_image("C:/Users/i'm/PycharmProjects/Worki/picture/pik/Ra.jpg")




import wrap_py
wrap_py.app.start()
