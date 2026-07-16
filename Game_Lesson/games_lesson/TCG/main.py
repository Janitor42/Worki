import tkinter as tk

from logic import card_factory, player

from gui.player_panel import PlayerPanel
from gui.game_field import GameField

from controller.game_controller import GameController

root = tk.Tk()
root.geometry("800x800+300+200")
root.resizable(width=False, height=False)
root.configure(background="gray60")

deck = card_factory.load_deck_from_json('data/cards_base.json')

# region bot
bot_model = player.Player(name='Бот', full_deck=deck)
bot_model.begin_round()

bot_gui = PlayerPanel(root=root, player_logic=bot_model)
bot_gui.place_container(x=10, y_hand=10, y_board=200)
# endregion

# region player
player_model = player.Player(name='Олег', full_deck=deck)
player_model.begin_round()

player_gui = PlayerPanel(root=root, player_logic=player_model)
player_gui.place_container(x=10, y_hand=590, y_board=400)
# endregion

# region game_director
general_widgets = GameField(parent=root)
views = GameController.Views(player_gui=player_gui, bot_gui=bot_gui, game_field=general_widgets)
game_director = GameController(player_model=player_model, bot_model=bot_model, views=views)
# endregion



root.mainloop()
