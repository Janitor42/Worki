import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import wrap_engine


a=wrap_engine.world.World()
wrap_engine.world.World.create_world(a,500,500)








import wrap_py
wrap_py.app.start()