# как добавить персонажа не из wrap

import wrap
wrap.world.create_world(1000,600)
wrap.world.set_back_color(139,78,158)
#Добавление персонажа не из коллекции wrap
wrap.add_sprite_dir("..")
wrap.sprite.add("picture",300,300,"orange")

import wrap_py
wrap_py.app.start()