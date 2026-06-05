from form.main_window import Main_window
from model.player import Player

my_table = Main_window()
im = Player(screen=my_table.screen)

my_table.mainloop()
