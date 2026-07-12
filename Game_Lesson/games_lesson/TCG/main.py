import tkinter as tk

from gui.card_widget import CardWidget
from gui.player_board import PlayerBoard
from logic import card_factory, player
from gui import player_board, player_panel

from controller.hand_controller import HandController

root = tk.Tk()
root.geometry("800x800+300+200")
root.resizable(width=False, height=False)
root.configure(background="gray60")

deck = card_factory.load_deck_from_json('data/cards_base.json')


# region бот
bot_model = player.Player(name='Бот', full_deck=deck)
bot_model.take_four_cards()

bot_gui = player_panel.PlayerPanel(root=root, player_logic=bot_model)
bot_gui.place_container(x=10, y=10)
bot_board = player_board.PlayerBoard(root=root)
bot_board.place_table(x=170, y=220)


bot_controller = HandController(player_model=bot_model, player_gui=bot_gui)
bot_controller.update_hand_view()

# endregion

player_model = player.Player(name='Олег', full_deck=deck)
player_model.take_four_cards()

player_gui = player_panel.PlayerPanel(root=root, player_logic=player_model)
player_gui.place_container(x=10, y=590)
player_board = player_board.PlayerBoard(root=root)
player_board.place_table(x=170, y=400)


player_controller = HandController(player_model=player_model, player_gui=player_gui)
player_controller.update_hand_view()


def end_turn_action():
    print("Контроллер: Ход передан!")


def click(event):
    target = event.widget
    hand_widgets = [x for x in player_gui.hand_widgets]
    card_widget = False

    for hand_widget in hand_widgets:
        hand_widget: CardWidget
        if target in hand_widget.get_draw_obj():
            card_widget = hand_widget
            break

    if not card_widget:
        return

    card_widget: CardWidget

    if player_model.check_card_to_play(obj=card_widget):
        player_gui.update_visual()
        player_controller.update_hand_view()
    else:
        print('мало энергии')


end_turn_btn = tk.Button(root, text="Конец хода", font=("Arial", 12, "bold"), bg="lightgray", command=end_turn_action)
end_turn_btn.place(x=25, y=530, width=120, height=40)

root.bind("<ButtonPress-1>", click)

root.mainloop()
