import tkinter as tk

from logic import card_factory, player

from gui.card_widget import CardWidget
from gui.player_panel import PlayerPanel

from controller.hand_controller import HandController
from controller.ai_controller import AIController

root = tk.Tk()
root.geometry("800x800+300+200")
root.resizable(width=False, height=False)
root.configure(background="gray60")

deck = card_factory.load_deck_from_json('data/cards_base.json')

# region bot
bot_model = player.Player(name='Бот', full_deck=deck)
bot_model.take_cards()

bot_gui = PlayerPanel(root=root, player_logic=bot_model)
bot_gui.place_container(x=10, y_hand=10, y_board=200)

bot_controller = HandController(player_model=bot_model, player_gui=bot_gui)
bot_controller.update_visual()

ai_boot=AIController(player_model=bot_model,player_controller=bot_controller)

# endregion

# region player
player_model = player.Player(name='Олег', full_deck=deck)
player_model.take_cards()

player_gui = PlayerPanel(root=root, player_logic=player_model)
player_gui.place_container(x=10, y_hand=590, y_board=400)

player_controller = HandController(player_model=player_model, player_gui=player_gui)
player_controller.update_visual()

# endregion

def end_turn_action():

    ai_boot.think()

    player_model.take_cards()
    player_controller.update_visual()


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
        player_controller.update_visual()

    else:

        label = tk.Label(root, text=f"Недостаточно энергии",
                         font=("Arial", 12), bg="yellow")
        label.place(x=380, y=400)
        label.lift()
        root.after(1000, label.destroy)


end_turn_btn = tk.Button(root, text="Конец хода", font=("Arial", 12, "bold"), bg="lightgray", command=end_turn_action)
end_turn_btn.place(x=25, y=530, width=120, height=40)

root.bind('<ButtonPress-1>', click)

root.mainloop()
