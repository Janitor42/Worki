import tkinter as tk
from logic import card_factory, player
from gui import game_board, player_panel

root = tk.Tk()
root.geometry("800x800+300+200")
root.resizable(width=False, height=False)
root.configure(background="gray60")

deck = card_factory.load_deck_from_json('data/cards_base.json')
bot_model = player.Player(name='Бот', full_deck=deck)
player_model = player.Player(name='Олег', full_deck=deck)

bot_model.take_four_cards()
player_model.take_four_cards()

board = game_board.GameBoard(root=root)

bot_gui = player_panel.PlayerPanel(root=root, player_logic=bot_model)
bot_gui.place_container(x=10, y=10)

player_gui = player_panel.PlayerPanel(root=root, player_logic=player_model)
player_gui.place_container(x=10, y=590)


def end_turn_action():
    print("Контроллер: Ход передан!")
    # Здесь в будущем пойдет вызов ИИ бота


end_turn_btn = tk.Button(root,text="Конец хода",font=("Arial", 12, "bold"),bg="lightgray",command=end_turn_action)
end_turn_btn.place(x=25, y=530, width=120, height=40)

root.mainloop()
